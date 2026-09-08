# Den Überblick behalten. KI-Impulse über den Dächern von Lübeck

Impuls von EDGE Digital bei **Lübeck.lokal** des Convention Bureau Lübeck,
**Atlantic Hotel, 9. September 2026, 9 bis 11 Uhr**. 30 Folien, 45 Minuten
plus 15 Minuten Fragen. Referenten: Emre Erdogan und Edgar Paul-Ghazaryan (Eddie).

## Live

**https://ueberblick.edge-digital.ai/**
GitHub Pages aus `main`, Repo `EdgarPaulEDGE/cbl-ueberblick`, öffentlich.
Jeder Push auf `main` geht automatisch live, das dauert etwa eine Minute.

Die Seite zum Mitnehmen liegt unter `/karte.html` und ist das, worauf der
QR-Code auf Folie 28 zeigt: die vier Türme, der Kompass, die vier Prompts
des Vormittags mit Kopieren-Knopf, die Montags-Aufgabe. Nichts wird gedruckt.

## Stamm

Das Deck ist ein Kind des K64-Decks (`cbl-aufgeweckt`): Kopf, Stylesheet und
Skript kommen unverändert von dort, nur die Folien und drei Bilder sind neu.
`bau.py` setzt `index.html` aus `../cbl-aufgeweckt/index.html` und `folien.html`
zusammen. **Folien werden in `folien.html` geändert, nie in `index.html`**,
danach `python3 bau.py`.

Was gegenüber K64 anders ist, und warum:

- **Wiederholer sitzen drin.** Einige waren am 26.08. in Travemünde. Deshalb
  kein Sandburg-Prinzip, kein Mensch-oder-Maschine, kein Pizza-Vergleich.
  RAKF bleibt als eine Folie (der Kompass), alles andere ist neu und live.
- **Beamer statt Strand.** Vier Live-Demos tragen den Vortrag, die Folien
  davor tragen nur das Versprechen (das Fragezeichen). Bestellung, Hotelsuche
  mit Quellen, Bild mit Referenz, vom Zettel zum Plan.
- **Der Titel gibt den Faden vor.** Vier Türme statt fünfzig Logos: Assistent,
  Rechercheur, Bildermacher, Gedächtnis. Das ist die eine Folie, die
  fotografiert wird.
- **Die Fragen vom Bogen.** Elf Rückmeldungen, null mal „Nein, noch nicht".
  Die Spiegel-Folie zeigt ihre Zitate, jede Demo beantwortet eine davon.

## Bedienung

| Taste | Wirkung |
|---|---|
| Pfeil rechts / links | Blättern |
| **S** | Redneransicht mit allen Regie-Notizen |
| **F** | Vollbild |
| **O** | Übersicht über alle Folien |
| **Esc** | Zurück aus der Übersicht |

`?nofrag` an die Adresse hängen zeigt alle Einblendungen sofort. Nur drei
Folien bauen sich klickweise auf: die Handzeichen (4) und die vier Türme (8).

Ohne Adressleiste: Taste `F`, oder Doppelklick auf `Vollbild starten.command`
(Chrome im Kiosk-Modus, Ende mit `cmd+Q`).

## Zeitplan

| Zeit | Folien | Block | Wer |
|---|---|---|---|
| 0:00 | 1 bis 2 | Titel über den Dächern, der Roboter stellt sich vor (Video, Klick) | Emre |
| 0:01 | 3 bis 4 | Team, dann die Agenda: die vier Farben des Vormittags | Emre |
| 0:04 | 5 bis 6 | Handzeichen, der Spiegel aus den Bögen | beide |
| 0:07 | 7 bis 9 | Weiß die KI alles, weniger ist mehr, die vier Arten von Werkzeug | beide |
| 0:13 | 10 bis 11 | Wo anfangen, vier Fragen vor dem Tippen (Kompass) | Emre |
| 0:15 | 12 bis 13 | Jetzt live, Demo 0: Reden statt tippen (Handy, Sprachmodus) | beide |
| 0:17 | 14 bis 15 | Demo 1: Die Absage, beide Prompts aus der Zwischenablage, dann der Merksatz | beide |
| 0:24 | 16 | Hotelsuche in drei Stufen (Stufe 1 live, 2 zeigen, 3 fertig vom Desktop) | beide |
| 0:27 | 17 bis 19 | Ein Foto, drei Schritte: Raum, Logo, Gäste (alle Bilder fertig, nichts live) | beide |
| 0:32 | 20 | Und jetzt bewegt es sich: die Kamerafahrt (Video, Klick) | beide |
| 0:33 | 21 bis 22 | Euer eigener Ordner: Gemini Notebook, eine Frage live, dann der Podcast (Folie 22) | beide |
| 0:37 | 23 bis 25 | Die Fragen, die immer kommen: kurze Antworten, dann Datenschutz im Detail | beide, Pingpong |
| 0:41 | 26 | Merksatz „Wer den Überblick behält" | |
| 0:42 | 27 bis 28 | Und am Montag (der Roboter verabschiedet sich), QR | Emre |
| 0:45 | 29 | Fragen, 15 Minuten | beide |
| 1:00 | 30 | Ende, Übergang in die Themenstränge | |

Streichliste, wenn es eng wird: erst die Hotelsuche ganz erzählen statt
zeigen (spart 3 Minuten), dann Demo 0 weglassen, dann die Bildreihe auf
Schritt 1 und 3 kürzen. In `reserve-folien.html` liegen die Zettel-Demo
und der Werkzeugkasten, falls eine Demo ausfällt und Zeit übrig ist.

## Demos vorbereiten (am Abend davor, jede einmal komplett)

| Demo | Braucht | Backup im Ordner `backup/` |
|---|---|---|
| Die Absage (Folie 13) | ChatGPT oder Claude eingeloggt, beide Prompts stehen auf der Karte mit Kopieren-Knopf, keine Mail nötig | Screenshots beider Ergebnisse vom Vorabend in `backup/` (noch anzulegen) |
| Hotelsuche (Folie 15) | Stufe 1 und 2 live im Chat, Stufe 3 liegt fertig: `Deep-Research-Tagungshotel-Luebeck.html` und `.pdf` auf dem Desktop, auch auf der Karte verlinkt | Screenshots von Stufe 1 und 2 vom Vorabend in `backup/` |
| Bild | nichts, alle drei Schritte liegen im Deck (`assets/images/demo/`) | die Folie selbst ist das Backup |
| Reden statt tippen | Handy per Kabel an der Saalanlage, ChatGPT-Sprachmodus, der Kompass-Satz (Folie 12) als Text auf dem Handy; keine Mail nötig, alles steckt im Satz | Bildschirmaufnahme vom Vorabend |
| Gemini Notebook | Notebook „Nordlicht 2027“ liegt im Google-Konto, Frage einmal testen (Desktop-Ordner `NotebookLM-Demo`, Ablauf.md) | Podcast läuft live im Deck (Folie 22) und auf der Karte: `assets/audio/podcast.mp3` plus `assets/podcast-wellen.js` (Three.js lokal unter `assets/vendor/three/`), das 3D-Wellenfeld wird aus dem Ton gerechnet, kein Video, darum auf jedem Bildschirm scharf. Braucht WebGL, läuft offline |
| Roboter-Clips | drei Clips liegen im Deck (`assets/video/robo-*.mp4`: Begrüßung, Jobs-Antwort, Montag), Ton im Saal um 8:30 testen | Folie ohne Ton erzählen |
| Gala-Kamerafahrt | liegt im Deck (`assets/video/gala.mp4`), nichts vorzubereiten | Das Standbild (Poster) ist Schritt 3 der Bildreihe |

Laptop per HDMI, eigener Hotspot als Netz-Fallback, Browser-Zoom 125 Prozent,
damit die letzte Reihe mitliest.

## Am Morgen um 8:30 im Saal

1. `Vollbild starten.command` oder https://ueberblick.edge-digital.ai im Chrome, einmal komplett durchblättern (30 Folien).
2. Ton: Folie 2 anklicken, Folie 22 anklicken. Beides muss aus der Saalanlage kommen.
3. Handy per Kabel an die Anlage, Sprachmodus mit dem Kompass-Satz einmal sprechen.
4. Zweiter Tab: ChatGPT oder Claude eingeloggt, Karte offen (Prompts zum Kopieren).
5. Dritter Tab: Gemini Notebook „Nordlicht 2027", einmal die Frage stellen.
6. Bericht `Deep-Research-Tagungshotel-Luebeck.html` vom Desktop öffnen, Tabelle sichtbar.

## Lokal starten und prüfen

```bash
npm run serve            # http://localhost:8080
python3 bau.py           # index.html aus Stamm und folien.html
node pruefe.mjs          # fehlende Dateien
npm run pruefe-alles     # Überlauf, Überlappung, Verzerrung, Ausrichtung
```

`node_modules` ist ein Symlink auf den K64-Ordner, dort liegt puppeteer.

## Bilder

Alle Bilder mit KI erzeugt und auf der Folie gekennzeichnet:

- `assets/images/robo/dach-petriturm.jpg`: der Begleiter auf der Dachterrasse,
  Petriturm dahinter. Titel und Schlussfrage. Text steht rechts, weil der
  Roboter links steht. Spiegeln ging nicht, die Kappe trägt Schrift.
- `assets/images/robo/tuerme.jpg`: der Begleiter mit Fernglas über den sieben
  Türmen. Trennfolie Landkarte und Merksatz.
- `assets/images/demo/`: die Bildreihe von Folie 16. `roof-vorher.jpg` ist das
  Foto der Roof Lounge von convention-luebeck.com (der Raum des 9. September),
  `schritt-1.jpg` bis `schritt-3.jpg` sind GPT Image 2 mit dem jeweils vorigen
  Bild als Referenz: Gala-Dinner, dann das CB-Logo als Datei angehängt, dann
  Gäste. `assets/video/gala.mp4` ist Grok Video 1.5 aus Schritt 3, acht Sekunden, die Kamera zieht zurück und öffnet den Blick auf die Skyline; fünf weitere Varianten (Seedance, Kling 4K, Kling Pro, Cinema Studio, MiniMax) liegen auf dem Desktop unter `Gala-Video-Varianten`.
- Alle übrigen Motive aus dem K64-Deck (Holstentor, Passat, Freisteller).

Beide neuen Bilder: GPT Image 2 mit dem Roboter-Freisteller und dem
Holstentor-Bild als Referenz, danach Bytedance-Upscale auf 3856 × 2160.
