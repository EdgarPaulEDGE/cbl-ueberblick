/**
 * Prüft die Karte zum Mitnehmen auf Überlauf und legt beide Seiten als PNG ab.
 * Aufruf: node pruefe-karte.mjs <bildordner> [adresse]
 */
import puppeteer from "puppeteer";
const adresse = process.argv[3] || "http://localhost:8080";
const browser = await puppeteer.launch();
const seite = await browser.newPage();
await seite.setViewport({ width: 1000, height: 1400, deviceScaleFactor: 2 });
await seite.goto(`${adresse}/karte.html`, { waitUntil: "networkidle0" });
await seite.evaluate(() => document.fonts.ready);
// Läuft der Inhalt über die Kartenkante? Auf Papier fällt das sonst erst
// nach dem Druck auf.
const mass = await seite.evaluate(() =>
  [...document.querySelectorAll(".karte")].map((k) => {
    const kante = k.getBoundingClientRect().bottom;
    let tiefstes = 0, text = "";
    k.querySelectorAll("*").forEach((el) => {
      const r = el.getBoundingClientRect();
      if (r.height > 0 && r.bottom > tiefstes) {
        tiefstes = r.bottom;
        text = (el.textContent || "").trim().replace(/\s+/g, " ").slice(0, 40);
      }
    });
    return { ueber: Math.round(tiefstes - kante), text };
  })
);
const karten = await seite.$$(".karte");
for (let i = 0; i < karten.length; i++) {
  await karten[i].screenshot({ path: `${process.argv[2]}/karte-${i + 1}.png` });
}
await browser.close();
mass.forEach((m, i) =>
  console.log(
    m.ueber > 0
      ? `Karte ${i + 1}: ${m.ueber}px ÜBER die Kante  "${m.text}"`
      : `Karte ${i + 1}: passt (${-m.ueber}px Luft bis zur Kante)`
  )
);
