# Den Überblick behalten. KI-Impulse über den Dächern von Lübeck

Impuls von EDGE Digital bei **Lübeck.lokal** des Convention Bureau Lübeck,
**Atlantic Hotel, 9. September 2026, 9 bis 11 Uhr**. 23 Folien, 45 Minuten
plus 15 Minuten Fragen. Referenten: Emre Erdogan und Edgar Paul-Ghazaryan (Eddie).

## Live

**https://ueberblick.edge-digital.ai/**
GitHub Pages aus `main`, Repo `EdgarPaulEDGE/cbl-ueberblick`, öffentlich.
Jeder Push auf `main` geht automatisch live, das dauert etwa eine Minute.

Die Seite zum Mitnehmen liegt unter `/karte.html` und ist das, worauf der
QR-Code auf Folie 21 zeigt: die vier Türme, der Kompass, die vier Prompts
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
Folien bauen sich klickweise auf: die Handzeichen (3) und die vier Türme (7).

Ohne Adressleiste: Taste `F`, oder Doppelklick auf `Vollbild starten.command`
(Chrome im Kiosk-Modus, Ende mit `cmd+Q`).

## Zeitplan

| Zeit | Folien | Block | Wer |
|---|---|---|---|
| 0:00 | 1 bis 3 | Titel, Team, Handzeichen | Emre |
| 0:05 | 4 bis 5 | Der Spiegel, „Weiß die KI alles?" | Eddie |
| 0:07 | 6 bis 8 | Vier Türme, wo anfangen | Eddie |
| 0:14 | 9 | Der Kompass, eine Folie | Emre |
| 0:16 | 10 bis 11 | Demo 1: Die Absage, vorbereiteter Fall, zwei Prompts aus der Zwischenablage | Eddie tippt, Emre erzählt |
| 0:23 | 12 bis 13 | Merksatz, dann die Hotelsuche in drei Stufen (Stufe 1 und 2 live, Deep Research fertig von heute früh) | Eddie |
| 0:29 | 14 | Demo 3: Raum, Logo, Gesicht | Eddie |
| 0:37 | 15 | Demo 4: Emres Zettel wird Aufgabenliste und Teams-Ordner | Emre |
| 0:41 | 16 bis 19 | Daten, Strom, Jobs | beide, Pingpong |
| 0:44 | 20 bis 21 | Montags-Aufgabe, QR | Emre |
| 0:45 | 22 | Fragen, 15 Minuten | beide |
| 1:00 | 23 | Ende, Übergang in die Themenstränge | |

Streichliste, wenn es eng wird: erst Demo 4 nur erzählen (spart 4 Minuten),
dann Folie 18 überspringen und die drei Antworten mündlich geben.

## Demos vorbereiten (am Abend davor, jede einmal komplett)

| Demo | Braucht | Backup im Ordner `backup/` |
|---|---|---|
| Bestellung | ChatGPT oder Claude eingeloggt, eine eigene alte Mail als Tonvorlage | Screenshots beider Ergebnisse |
| Hotelsuche | Deep Research vorab einmal gelaufen, Dauer gemessen | Ergebnis als PDF |
| Bild | Raumfoto um 8:30, CLB-Logo als PNG, Eddies Porträt | alle drei Bilder vorab erzeugt |
| Zettel | von Hand geschriebene Seite, AirDrop vom Handy | Ergebnistabelle als Screenshot |

Laptop per HDMI, eigener Hotspot als Netz-Fallback, Browser-Zoom 125 Prozent,
damit die letzte Reihe mitliest.

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
- Alle übrigen Motive aus dem K64-Deck (Holstentor, Passat, Freisteller).

Beide neuen Bilder: GPT Image 2 mit dem Roboter-Freisteller und dem
Holstentor-Bild als Referenz, danach Bytedance-Upscale auf 3856 × 2160.
