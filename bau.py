#!/usr/bin/env python3
"""Setzt index.html aus dem K64-Stamm und den eigenen Folien zusammen.

Kopf, Stylesheet und Skript kommen unverändert aus cbl-aufgeweckt (80/20-Stamm),
nur Titel, Meta und der Folienblock sind neu. Aufruf: python3 bau.py
"""
import pathlib, re
HIER = pathlib.Path(__file__).parent
STAMM = HIER.parent / "cbl-aufgeweckt" / "index.html"
html = STAMM.read_text(encoding="utf-8")
folien = (HIER / "folien.html").read_text(encoding="utf-8")

html = html.replace("<title>Aufgeweckt. KI-Klartext zum Frühstück | EDGE Digital x LTM</title>",
                    "<title>Den Überblick behalten. KI-Impulse über den Dächern von Lübeck | EDGE Digital x Convention Bureau Lübeck</title>")
html = html.replace("""   AUFGEWECKT. KI-KLARTEXT ZUM FRÜHSTÜCK
   Netzwerkfrühstück der LTM im K64, Lübeck, 20.08.2026""",
"""   DEN ÜBERBLICK BEHALTEN. KI-IMPULSE ÜBER DEN DÄCHERN VON LÜBECK
   Lübeck.lokal des Convention Bureau, Atlantic Hotel, 09.09.2026
   Stamm: das K64-Deck (cbl-aufgeweckt), nur Folien und Bilder sind neu.""")

# Zusatzstil: Logos auf dem Titel unten links, Datum bleibt oben in der Label-Zeile
zusatz = """
/* ---------- Titel: beide Logos unten links ---------- */
.titel-logos { position: absolute; left: 130px; bottom: 96px; display: flex; align-items: center; gap: 34px; }
.titel-logos img { height: 54px; display: block; }
.titel-x { font-size: 36px; color: var(--w-45); font-weight: 500; }
/* Text rechts, wenn das Motiv links steht */
.slide.rechts { align-items: flex-end; text-align: right; }
.slide.rechts .titel-logos { left: auto; right: 130px; }
.slide.rechts .bild-quelle { left: auto; right: 130px; }
.reveal .slide-background[data-schleier="seite-rechts"]::after {
  background:
    linear-gradient(270deg, rgba(3, 3, 9, .97) 0%, rgba(3, 3, 9, .88) 38%, rgba(3, 3, 9, .35) 78%, rgba(3, 3, 9, .55) 100%),
    linear-gradient(0deg, rgba(3, 3, 9, .7) 0%, transparent 45%);
}
/* Titelbild: die Stadt bleibt sichtbar, links liegt genug Dunkel für die
   große Headline. Kräftiger als "seite", weil die Gebäude hell leuchten. */
.reveal .slide-background[data-schleier="titel"]::after {
  background:
    linear-gradient(90deg, rgba(3, 3, 9, .97) 0%, rgba(3, 3, 9, .94) 34%, rgba(3, 3, 9, .72) 58%, rgba(3, 3, 9, .3) 88%, rgba(3, 3, 9, .5) 100%),
    linear-gradient(0deg, rgba(3, 3, 9, .78) 0%, transparent 42%);
}
/* Zettel: Inhalt so groß, dass der Kasten neben dem Fragezeichen nicht leer wirkt */
.zettel ul { font-size: 0; }
.zettel li { font-size: 31px; line-height: 1.9; }

/* ---------- Der Kompass im Raum ----------
   Eine Scheibe, um 58 Grad nach hinten gekippt, zwei Ringe darunter für die
   Tiefe, eine Nadel, die von Frage zu Frage wandert. Alles CSS-3D, kein
   WebGL: läuft im Standbild ebenso wie im Vortrag, und ohne box-shadow. */
.kompass-buehne { flex: 0 0 620px; height: 640px; position: relative; perspective: 1700px; }
.kompass {
  position: absolute; left: 50%; top: 46%; width: 540px; height: 540px;
  transform: translate(-50%, -50%) rotateX(58deg) rotateZ(-14deg);
  transform-style: preserve-3d;
  animation: kompass-schweben 7s ease-in-out infinite alternate;
}
@keyframes kompass-schweben {
  from { transform: translate(-50%, -52%) rotateX(58deg) rotateZ(-16deg); }
  to   { transform: translate(-50%, -48%) rotateX(56deg) rotateZ(-11deg); }
}
.kompass-ring {
  position: absolute; inset: 0; border-radius: 50%;
  border: 1px solid rgba(244, 246, 255, .18); background: rgba(6, 8, 18, .9);
}
.kompass-ring.r1 { transform: translateZ(-14px); }
.kompass-ring.r2 { transform: translateZ(-28px); background: rgba(3, 4, 12, .95); }
.kompass-ring::before {
  content: ""; position: absolute; inset: -3px; border-radius: 50%;
  background: conic-gradient(var(--purple), var(--blau) 38%, var(--cyan) 62%, var(--purple));
  z-index: -1; opacity: .55;
}
.kompass-scheibe { position: absolute; inset: 0; transform: translateZ(2px); }
.kompass-scheibe svg { width: 100%; height: 100%; display: block; }
.kompass-buchstabe { font-family: var(--font); font-weight: 700; font-size: 25px; text-anchor: middle; }
.kompass-nadel {
  position: absolute; left: 50%; top: 50%; width: 28px; height: 400px;
  margin: -200px 0 0 -14px; transform-style: preserve-3d;
  animation: nadel-wandern 16s cubic-bezier(.5, 0, .2, 1) infinite;
}
.kompass-nadel i {
  position: absolute; left: 0; width: 28px; height: 200px;
  clip-path: polygon(50% 0, 100% 100%, 0 100%);
}
.kompass-nadel i:first-child { top: 0; background: linear-gradient(180deg, var(--cyan), var(--blau)); }
.kompass-nadel i:last-child { top: 200px; transform: rotate(180deg); background: linear-gradient(180deg, rgba(244,246,255,.7), rgba(244,246,255,.25)); }
.kompass-achse {
  position: absolute; left: 50%; top: 50%; width: 38px; height: 38px; margin: -19px 0 0 -19px;
  border-radius: 50%; background: #F4F6FF; border: 4px solid #070a14; transform: translateZ(6px);
}
/* Die Nadel hält auf jeder Richtung an: Rolle, Aufgabe, Kontext, Förmchen */
@keyframes nadel-wandern {
  0%, 20%   { transform: rotate(0deg); }
  25%, 45%  { transform: rotate(90deg); }
  50%, 70%  { transform: rotate(180deg); }
  75%, 95%  { transform: rotate(270deg); }
  100%      { transform: rotate(360deg); }
}
.kompass-schatten {
  position: absolute; left: 50%; bottom: 6px; width: 520px; height: 84px; transform: translateX(-50%);
  border-radius: 50%; background: radial-gradient(50% 50% at 50% 50%, rgba(0, 226, 226, .22), transparent 70%);
}
@media (prefers-reduced-motion: reduce) { .kompass, .kompass-nadel { animation: none; } }

/* Die vier Fragen neben dem Kompass */
.kompass-zeile { display: grid; grid-template-columns: 210px 1fr; column-gap: 28px; padding: 32px 6px; }
.kompass-zeile .baustein-kopf { margin: 8px 0 0; font-size: 23px; }
.kompass-zeile b { font-size: 40px; font-weight: 700; display: block; line-height: 1.2; }
.kompass-zeile span:last-child { grid-column: 2; font-size: 28px; color: var(--w-70); margin-top: 6px; }

/* Drei Antworten: Frage klein, Antwort groß, nichts sonst */
.antwort { padding: 40px 6px; }
.antwort .label { display: block; margin-bottom: 14px; }
.antwort p { font-size: 44px; font-weight: 600; line-height: 1.3; margin: 0; }
/* ---------- Kapitel-Marker: wo sind wir gerade? ----------
   Ein farbiger Punkt in der Farbe des jeweiligen Werkzeugs, oben über der
   Headline. Vier Farben, den ganzen Vormittag dieselben. */
.kapitel { display: flex; align-items: center; gap: 12px; margin: 0 0 14px;
  font-weight: 600; font-size: 20px; letter-spacing: .16em; text-transform: uppercase; color: var(--w-45); }
.kapitel i { width: 10px; height: 10px; border-radius: 50%; display: block; }
.slide.podcast-buehne .kapitel { position: relative; z-index: 1; }

/* ---------- Agenda: was heute passiert ---------- */
.agenda-zeile { display: grid; grid-template-columns: 26px 340px 1fr; align-items: baseline; column-gap: 22px; padding: 26px 6px; }
.agenda-zeile .punkt { width: 12px; height: 12px; border-radius: 50%; display: block; }
.agenda-zeile b { font-size: 38px; font-weight: 700; }
.agenda-zeile span:last-child { font-size: 29px; color: var(--w-70); }

/* ---------- Bildreihe: ein Foto, drei Schritte ----------
   Jede Station zeigt ihr Ergebnis als Bild, Schritt 1 trägt das Ausgangsfoto
   als kleines Bild in der Ecke, damit der Vorher-Nachher-Sprung sichtbar ist. */
.demo-bild { position: relative; border-radius: 18px; overflow: hidden; border: 1px solid var(--hairline-stark); margin-bottom: 18px; }
.demo-bild img { width: 100%; aspect-ratio: 16 / 9; object-fit: cover; display: block; }
.demo-bild .vorher {
  position: absolute; left: 14px; bottom: 14px; width: 31%; aspect-ratio: 16 / 9;
  border: 2px solid rgba(244, 246, 255, .85); border-radius: 10px;
}
.demo-bild .vorher + .vorher-label, .demo-bild::after { content: none; }
/* ---------- Videofenster: der Roboter spricht ----------
   Start nur per Klick oder Leertaste. Der Knopf verschwindet beim Abspielen. */
.video-fenster {
  position: relative; width: 1500px; border-radius: 28px; overflow: hidden;
  border: 1px solid var(--hairline-stark); background: #06080f;
}
.video-fenster video { width: 100%; display: block; }
.video-start {
  position: absolute; left: 50%; top: 50%; width: 150px; height: 150px; margin: -75px 0 0 -75px;
  border-radius: 50%; border: 1px solid var(--hairline-stark); background: rgba(8, 11, 22, .72);
  color: var(--weiss); cursor: pointer; display: grid; place-items: center; transition: opacity .25s;
}
.video-start svg { width: 64px; height: 64px; margin-left: 8px; }
.video-fenster.laeuft .video-start { opacity: 0; pointer-events: none; }
/* Vollbild-Video: füllt die ganze Folie, kein Rahmen, kein Radius */
.video-fenster.voll { position: absolute; inset: 0; width: 1920px; height: 1080px; border: 0; border-radius: 0; background: #030309; }
.video-fenster.voll video { width: 1920px; height: 1080px; object-fit: cover; }
.video-fenster.voll .video-start { width: 170px; height: 170px; margin: -85px 0 0 -85px; }
</style>"""
html = html.replace("</style>", zusatz, 1)
# Podcast-Bühne: Stylesheet, Importmap für Three.js (lokal, offline) und das Modul
html = html.replace("</head>", """<link rel="stylesheet" href="assets/podcast.css">
<script type="importmap">{ "imports": { "three": "./assets/vendor/three/three.module.js", "three/addons/": "./assets/vendor/three/addons/" } }</script>
</head>""", 1)
html = html.replace("</body>", """<script type="module">
/* Podcast-Folie: Wellenfeld läuft nur, solange die Folie steht; Leertaste startet und hält an. */
import { podcastBuehne } from "./assets/podcast-wellen.js";
var buehnen = [];
document.querySelectorAll(".podcast-buehne").forEach(function (el) {
  var b = podcastBuehne(el); el.__buehne = b; buehnen.push([el, b]);
  el.addEventListener("click", b.umschalten);
});
function pruefen() {
  var aktuell = Reveal.getCurrentSlide();
  buehnen.forEach(function (paar) {
    if (aktuell && aktuell.contains(paar[0])) paar[1].start(Reveal.getScale()); else paar[1].stop();
  });
}
function start() { pruefen(); Reveal.on("slidechanged", pruefen); Reveal.on("resize", function () { buehnen.forEach(function (p) { p[1].resize(Reveal.getScale()); }); }); }
if (Reveal.isReady && Reveal.isReady()) start(); else Reveal.on("ready", start);
document.addEventListener("keydown", function (e) {
  if (e.code !== "Space") return;
  var el = Reveal.getCurrentSlide() && Reveal.getCurrentSlide().querySelector(".podcast-buehne");
  if (!el) return;
  e.preventDefault(); e.stopPropagation(); el.__buehne.umschalten();
}, true);
</script>
</body>""", 1)

# Reveal baut seine Hintergrund-Elemente bei jedem configure() neu, dann ist
# der kopierte Schleier weg. Deshalb bei jedem Folienwechsel nachkopieren.
html = html.replace("""Reveal.on('ready', function () {
  document.querySelectorAll('.reveal .slides section[data-schleier]').forEach(function (s) {
    var bg = Reveal.getSlideBackground(s);
    if (bg) bg.dataset.schleier = s.dataset.schleier;
  });
});""", """function schleierKopieren() {
  document.querySelectorAll('.reveal .slides section[data-schleier]').forEach(function (s) {
    var bg = Reveal.getSlideBackground(s);
    if (bg) bg.dataset.schleier = s.dataset.schleier;
  });
}
Reveal.on('ready', schleierKopieren);
Reveal.on('slidechanged', schleierKopieren);""")

html = html.replace("<script src=\"kosmos.js\"></script>", "<script>" + "\n/* Videos: Klick auf das Fenster oder Leertaste auf der Folie startet, ein\n   zweiter Klick hält an. Beim Verlassen der Folie wird zurückgespult. */\ndocument.querySelectorAll('.video-fenster').forEach(function (f) {\n  var v = f.querySelector('video');\n  function umschalten() { if (v.paused) { v.play(); } else { v.pause(); } }\n  f.addEventListener('click', umschalten);\n  v.addEventListener('play', function () { f.classList.add('laeuft'); });\n  v.addEventListener('pause', function () { f.classList.remove('laeuft'); });\n  v.addEventListener('ended', function () { f.classList.remove('laeuft'); v.currentTime = 0; });\n});\ndocument.addEventListener('keydown', function (e) {\n  if (e.code !== 'Space') return;\n  var v = Reveal.getCurrentSlide().querySelector('.video-fenster video');\n  if (!v) return;\n  e.preventDefault(); e.stopPropagation();\n  if (v.paused) v.play(); else v.pause();\n}, true);\nReveal.on('slidechanged', function (e) {\n  if (e.previousSlide) e.previousSlide.querySelectorAll('video').forEach(function (v) { v.pause(); v.currentTime = 0; });\n});\n" + "</script>\n<script src=\"kosmos.js\"></script>")

anfang = html.index('<div class="slides">') + len('<div class="slides">')
ende = html.index('</div>\n</div>\n\n<script src="vendor/reveal/reveal.js">')
html = html[:anfang] + "\n\n" + folien.strip() + "\n\n" + html[ende:]
(HIER / "index.html").write_text(html, encoding="utf-8")
print("index.html gebaut:", html.count("<section"), "Folien")
