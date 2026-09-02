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

/* ---------- Der Kompass im Raum ----------
   Eine Scheibe, um 58 Grad nach hinten gekippt, zwei Ringe darunter für die
   Tiefe, eine Nadel, die von Frage zu Frage wandert. Alles CSS-3D, kein
   WebGL: läuft im Standbild ebenso wie im Vortrag, und ohne box-shadow. */
.kompass-buehne { flex: 0 0 560px; height: 520px; position: relative; perspective: 1400px; }
.kompass {
  position: absolute; left: 50%; top: 46%; width: 440px; height: 440px;
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
.kompass-buchstabe { font-family: var(--font); font-weight: 700; font-size: 26px; text-anchor: middle; }
.kompass-nadel {
  position: absolute; left: 50%; top: 50%; width: 22px; height: 300px;
  margin: -150px 0 0 -11px; transform-style: preserve-3d;
  animation: nadel-wandern 16s cubic-bezier(.5, 0, .2, 1) infinite;
}
.kompass-nadel i {
  position: absolute; left: 0; width: 22px; height: 150px;
  clip-path: polygon(50% 0, 100% 100%, 0 100%);
}
.kompass-nadel i:first-child { top: 0; background: linear-gradient(180deg, var(--cyan), var(--blau)); }
.kompass-nadel i:last-child { top: 150px; transform: rotate(180deg); background: linear-gradient(180deg, rgba(244,246,255,.7), rgba(244,246,255,.25)); }
.kompass-achse {
  position: absolute; left: 50%; top: 50%; width: 30px; height: 30px; margin: -15px 0 0 -15px;
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
  position: absolute; left: 50%; bottom: 10px; width: 420px; height: 70px; transform: translateX(-50%);
  border-radius: 50%; background: radial-gradient(50% 50% at 50% 50%, rgba(0, 226, 226, .22), transparent 70%);
}
@media (prefers-reduced-motion: reduce) { .kompass, .kompass-nadel { animation: none; } }

/* Die vier Fragen neben dem Kompass */
.kompass-zeile { display: grid; grid-template-columns: 190px 1fr; column-gap: 24px; padding: 22px 6px; }
.kompass-zeile .baustein-kopf { margin: 6px 0 0; font-size: 22px; }
.kompass-zeile b { font-size: 34px; font-weight: 700; display: block; }
.kompass-zeile span:last-child { grid-column: 2; font-size: 26px; color: var(--w-70); margin-top: 4px; }

/* Drei Antworten: Frage klein, Antwort groß, nichts sonst */
.antwort { padding: 40px 6px; }
.antwort .label { display: block; margin-bottom: 14px; }
.antwort p { font-size: 44px; font-weight: 600; line-height: 1.3; margin: 0; }
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
