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
/* Zettel: Inhalt so groß, dass der Kasten neben dem Fragezeichen nicht leer wirkt */
.zettel ul { font-size: 0; }
.zettel li { font-size: 31px; line-height: 1.9; }
</style>"""
html = html.replace("</style>", zusatz, 1)

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

anfang = html.index('<div class="slides">') + len('<div class="slides">')
ende = html.index('</div>\n</div>\n\n<script src="vendor/reveal/reveal.js">')
html = html[:anfang] + "\n\n" + folien.strip() + "\n\n" + html[ende:]
(HIER / "index.html").write_text(html, encoding="utf-8")
print("index.html gebaut:", html.count("<section"), "Folien")
