import puppeteer from "puppeteer";
const ZIEL = process.argv[2];
const b = await puppeteer.launch({ protocolTimeout: 180000 });
const s = await b.newPage();
// zweifache Auflösung: 3840x2160 je Seite, damit der Text auch beim Zoomen trägt
await s.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 2 });
await s.goto("http://localhost:8151/?nofrag&v=" + Date.now(), { waitUntil: "networkidle0" });
await new Promise((r) => setTimeout(r, 2500));
/* Im PDF bewegt sich nichts und es klingt nichts: ein eingefrorenes Video ist
   dort wertlos. Deshalb drei Eingriffe.
   1. Folien mit data-pdf="weglassen" bestehen nur aus dem Video und fallen ganz raus.
   2. Auf den übrigen Folien verschwindet das Videofenster, der Text daneben
      nimmt die frei werdende Breite.
   3. Sätze, die aufs Video zeigen, tragen in data-pdf ihren Ersatztext. */
await s.addStyleTag({ content: `
  .video-fenster, .video-start, .podcast-start, .podcast-balken, .podcast-zeit { display: none !important; }
` });
const weglassen = await s.evaluate(() => {
  document.querySelectorAll("video").forEach((v) => { v.pause(); v.currentTime = 0; });
  document.querySelectorAll("[data-pdf]").forEach((el) => {
    if (el.dataset.pdf !== "weglassen") el.textContent = el.dataset.pdf;
  });
  const raus = [];
  document.querySelectorAll(".reveal .slides > section").forEach((sec, i) => {
    if (sec.dataset.pdf === "weglassen") raus.push(i);
  });
  return raus;
});
await new Promise((r) => setTimeout(r, 1200));
const anz = await s.evaluate(() => Reveal.getTotalSlides());
let seite = 0;
for (let i = 0; i < anz; i++) {
  if (weglassen.includes(i)) continue;
  await s.evaluate((n) => Reveal.slide(n), i);
  await new Promise((r) => setTimeout(r, 700));
  seite++;
  await s.screenshot({ path: `${ZIEL}/s-${String(seite).padStart(2, "0")}.png` });
}
console.log("Seiten fotografiert:", seite, "| Videofolien ausgelassen:", weglassen.map((n) => n + 1).join(", "));
await b.close();
/* Aufruf: node export-pdf.mjs <zielordner>
   Danach die PNGs mit Pillow zu einem PDF binden (Qualität 88 landete bei
   9,2 MB für 23 Seiten). decktape scheidet hier aus: es rendert über
   page.pdf() im Print-Medium, dort kollabiert Reveals Bühne und die Kästen
   schneiden ihren Text ab. */
