/* Podcast-Bühne: Cover, Titel und ein 3D-Wellenfeld, das live aus dem Ton
   gerechnet wird (Web Audio Analyser). Läuft im Deck (Folie 19) und auf der
   Karte, immer in der Bühnengröße 1920 x 1080 und per Transform skaliert,
   der Zeichenpuffer folgt der echten Bildschirmauflösung: darum scharf. */
import * as THREE from "three";
import { EffectComposer } from "three/addons/postprocessing/EffectComposer.js";
import { RenderPass } from "three/addons/postprocessing/RenderPass.js";
import { UnrealBloomPass } from "three/addons/postprocessing/UnrealBloomPass.js";
import { Line2 } from "three/addons/lines/Line2.js";
import { LineMaterial } from "three/addons/lines/LineMaterial.js";
import { LineGeometry } from "three/addons/lines/LineGeometry.js";

const W = 1920, H = 1080;
const BAENDER = 64, ROWS = 34, COLS = 150, XW = 58, YB = -4.6;
const VERLAUF = 90; // gemerkte Frames für den Nachlauf der hinteren Reihen

// Kamera und Blickpunkt stehen fest, deshalb lässt sich ausrechnen, wo eine
// Reihe im Bild landet: Blickwinkel = atan(Höhe über der Ebene / Abstand).
const CAM = { y: 9.5, z: 12 }, BLICK = { y: -4.5, z: -5 };
const HOEHE = CAM.y - YB;                                   // 14.1
// Reihen NICHT gleichmäßig in der Tiefe verteilen: perspektivisch klaffen sie
// dann genau vorne auseinander und das Feld endet sichtbar über dem unteren
// Bildrand. Stattdessen den Winkel gleichmäßig teilen und z zurückrechnen.
const grad = (g) => (g * Math.PI) / 180;
const PHI_VORN = grad(61.4), PHI_HINTEN = grad(40.6);       // unterer Rand liegt bei 60,5°
const reiheZ = (t) => CAM.z - HOEHE / Math.tan(PHI_VORN + (PHI_HINTEN - PHI_VORN) * t);
const Z0 = reiheZ(0), ZD = reiheZ(1);

export function podcastBuehne(buehne) {
  const canvas = buehne.querySelector("canvas");
  const audio = buehne.querySelector("audio");
  const balken = buehne.querySelector(".podcast-balken i");
  const zeit = buehne.querySelector(".podcast-zeit");
  const knopf = buehne.querySelector(".podcast-start");

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, powerPreference: "high-performance", preserveDrawingBuffer: true });
  renderer.setClearColor(0x000000, 0);
  const scene = new THREE.Scene();
  scene.fog = new THREE.FogExp2(0x04050d, 0.055);
  const camera = new THREE.PerspectiveCamera(42, W / H, 0.1, 200);

  const purple = new THREE.Color("#C15DE6"), blau = new THREE.Color("#009FF4"), cyan = new THREE.Color("#00E2E2");
  const lines = [], rowPos = [], rowCol = [], colBuf = [], mats = [];
  const rowZ = [];
  for (let r = 0; r < ROWS; r++) {
    const t = r / (ROWS - 1);
    const z = reiheZ(t);
    rowZ.push(z);
    const pos = new Float32Array(COLS * 3), col = new Float32Array(COLS * 3);
    for (let c = 0; c < COLS; c++) {
      const u = c / (COLS - 1);
      pos[c * 3] = -XW / 2 + u * XW; pos[c * 3 + 1] = YB; pos[c * 3 + 2] = z;
      const k = u < 0.5 ? purple.clone().lerp(blau, u * 2) : blau.clone().lerp(cyan, (u - 0.5) * 2);
      col[c * 3] = k.r; col[c * 3 + 1] = k.g; col[c * 3 + 2] = k.b;
    }
    const geo = new LineGeometry(); geo.setPositions(pos); geo.setColors(col);
    const mat = new LineMaterial({ vertexColors: true, linewidth: 2.8 - t * 1.5, transparent: true, opacity: 1 - t * 0.8, worldUnits: false });
    const line = new Line2(geo, mat);
    scene.add(line); lines.push(line); rowPos.push(pos); rowCol.push(col); colBuf.push(new Float32Array(COLS * 3)); mats.push(mat);
  }
  // Dunkle Fläche unter den Linien: vordere Berge verdecken hintere Reihen.
  // Ihr Raster muss auf denselben z-Werten sitzen wie die Linien, sonst
  // schiebt sie sich zwischen sie und frisst die vordersten Reihen weg.
  const surfGeo = new THREE.PlaneGeometry(XW, 1, COLS - 1, ROWS - 1);
  surfGeo.rotateX(-Math.PI / 2);
  const surfPos = surfGeo.attributes.position;
  for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLS; c++) {
      const i = (r * COLS + c) * 3;
      surfPos.array[i] = -XW / 2 + (c / (COLS - 1)) * XW;
      surfPos.array[i + 2] = rowZ[r];
    }
  }
  surfPos.needsUpdate = true;
  const surf = new THREE.Mesh(surfGeo, new THREE.MeshBasicMaterial({ color: 0x04060e, transparent: true, opacity: 0.92, side: THREE.DoubleSide }));
  scene.add(surf);

  const composer = new EffectComposer(renderer);
  composer.addPass(new RenderPass(scene, camera));
  const bloom = new UnrealBloomPass(new THREE.Vector2(W, H), 0.6, 0.35, 0.45);
  composer.addPass(bloom);

  // ---------- Ton ----------
  let ctx = null, analyser = null, daten = null, bandIdx = null;
  const glatt = new Float32Array(BAENDER);
  const verlauf = Array.from({ length: VERLAUF }, () => new Float32Array(BAENDER));
  let kopf = 0;
  function tonAn() {
    if (ctx) { if (ctx.state === "suspended") ctx.resume(); return; }
    ctx = new (window.AudioContext || window.webkitAudioContext)();
    const quelle = ctx.createMediaElementSource(audio);
    analyser = ctx.createAnalyser(); analyser.fftSize = 2048; analyser.smoothingTimeConstant = 0.6;
    quelle.connect(analyser); analyser.connect(ctx.destination);
    daten = new Uint8Array(analyser.frequencyBinCount);
    const sr = ctx.sampleRate, binHz = sr / analyser.fftSize;
    bandIdx = [];
    for (let b = 0; b < BAENDER; b++) {
      const f0 = 60 * Math.pow(6500 / 60, b / BAENDER), f1 = 60 * Math.pow(6500 / 60, (b + 1) / BAENDER);
      const i0 = Math.max(1, Math.floor(f0 / binHz)), i1 = Math.max(i0 + 1, Math.ceil(f1 / binHz));
      bandIdx.push([i0, i1]);
    }
  }
  function messen() {
    const neu = verlauf[kopf];
    if (analyser && !audio.paused) {
      analyser.getByteFrequencyData(daten);
      for (let b = 0; b < BAENDER; b++) {
        const [i0, i1] = bandIdx[b]; let s = 0;
        for (let i = i0; i < i1; i++) s += daten[i];
        let v = (s / (i1 - i0)) / 255;
        v = Math.pow(Math.min(1, v * 1.35), 1.4);
        glatt[b] = Math.max(v, glatt[b] * 0.84);
        neu[b] = glatt[b];
      }
    } else {
      // Ruhezustand: leises Atmen, damit das Feld nie tot wirkt
      const t = performance.now() / 1000;
      for (let b = 0; b < BAENDER; b++) neu[b] = glatt[b] = Math.max(glatt[b] * 0.96, 0.16 + 0.10 * Math.sin(t * 0.8 + b * 0.25) * Math.sin(t * 0.37 + b * 0.05));
    }
    kopf = (kopf + 1) % VERLAUF;
  }
  function bandwert(lag, u) {
    const g = verlauf[(kopf - 1 - lag + VERLAUF * 2) % VERLAUF];
    const x = u * (BAENDER - 1), i = Math.floor(x), f = x - i;
    return g[i] + (g[Math.min(i + 1, BAENDER - 1)] - g[i]) * f;
  }

  // ---------- Bild ----------
  let pr = 1;
  function groesse(scale) {
    pr = Math.min((window.devicePixelRatio || 1) * scale, 2.2);
    renderer.setPixelRatio(pr); renderer.setSize(W, H, false);
    composer.setSize(W * pr, H * pr);
    for (const m of mats) m.resolution.set(W * pr, H * pr);
  }
  function zeichnen() {
    messen();
    const t = performance.now() / 1000;
    for (let r = 0; r < ROWS; r++) {
      const rt = r / (ROWS - 1);
      const lag = Math.min(VERLAUF - 1, Math.round(r * 1.9));
      const amp = 3.0 * (1 - rt * 0.4);
      const pos = rowPos[r], col = rowCol[r], cb = colBuf[r];
      for (let c = 0; c < COLS; c++) {
        const u = c / (COLS - 1);
        const v = bandwert(lag, Math.abs(u - 0.5) * 2);
        const drift = 0.16 * Math.sin(u * 9 + t * 0.9 + r * 0.35) + 0.09 * Math.sin(u * 23 - t * 1.3 + r * 0.8);
        const y = YB + v * v * amp + drift * (0.35 + v);
        pos[c * 3 + 1] = y;
        const hell = 0.5 + 0.9 * v;
        cb[c * 3] = Math.min(1, col[c * 3] * hell); cb[c * 3 + 1] = Math.min(1, col[c * 3 + 1] * hell); cb[c * 3 + 2] = Math.min(1, col[c * 3 + 2] * hell);
        surfPos.array[(r * COLS + c) * 3 + 1] = y - 0.22;
      }
      lines[r].geometry.setPositions(pos); lines[r].geometry.setColors(cb);
    }
    surfPos.needsUpdate = true;
    camera.position.set(Math.sin(t * 0.11) * 0.8, 9.5 + Math.sin(t * 0.17) * 0.3, 12);
    camera.lookAt(0, -4.5, -5);
    composer.render();
    if (balken && audio.duration) {
      balken.style.width = (100 * audio.currentTime / audio.duration).toFixed(2) + "%";
      const s = Math.floor(audio.currentTime), g = Math.floor(audio.duration);
      zeit.textContent = `${Math.floor(s / 60)}:${String(s % 60).padStart(2, "0")} / ${Math.floor(g / 60)}:${String(g % 60).padStart(2, "0")}`;
    }
  }
  let raf = 0, aktiv = false;
  function schleife() { if (!aktiv) return; zeichnen(); raf = requestAnimationFrame(schleife); }

  // Knopf, Zustand
  function umschalten() { if (audio.paused) { tonAn(); audio.play(); } else { audio.pause(); } }
  knopf && knopf.addEventListener("click", (e) => { e.stopPropagation(); umschalten(); });
  audio.addEventListener("play", () => { tonAn(); buehne.classList.add("laeuft"); });
  audio.addEventListener("pause", () => buehne.classList.remove("laeuft"));
  audio.addEventListener("ended", () => { buehne.classList.remove("laeuft"); audio.currentTime = 0; });

  return {
    start(scale = 1) { groesse(scale); if (!aktiv) { aktiv = true; schleife(); } },
    stop() { aktiv = false; cancelAnimationFrame(raf); audio.pause(); audio.currentTime = 0; },
    resize(scale = 1) { groesse(scale); zeichnen(); },
    umschalten, audio,
  };
}
