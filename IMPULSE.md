# Impulse für den 09.09.: sprechender Roboter, NotebookLM, Werkzeugkasten

Stand 05.09.2026. Ausgangslage: 45 Minuten sind mit vier Demos voll. Jeder
neue Baustein muss entweder unter einer Minute liegen oder etwas ersetzen.
Regel für alles hier: **pro Block höchstens ein Live-Risiko, alles andere ist
vorproduziert und liegt offline im Deck.**

## 1. Der sprechende Roboter

Drei Stufen, das Risiko steigt von oben nach unten. Empfehlung: Stufe 1 fest,
Stufe 2 fest, Stufe 3 nur bei grünem Technikcheck um 8:30.

**Stufe 1, sicher: Der Roboter begrüßt die Runde (30 Sekunden).**
Der Fischbrötchen-Roboter spricht auf der Titelfolie, lippensynchron, mit
einer deutschen ElevenLabs-Stimme („Albert", Charakterstimme, verstanden
Wort für Wort). Der Clip liegt als Video im Deck, läuft offline auf Klick.
Text: „Moin! Ich bin der Kollege mit der Fischbrötchen-Mütze. Ich kann Mails
schreiben, Hotels vergleichen und Bilder bauen. Aber ich kann nicht wissen,
was ihr mir nicht sagt." Der letzte Satz ist die These des ganzen Vormittags,
aus dem Mund des Roboters. Zweiter Clip am Ende („Und am Montag?"):
„Sucht euch die Aufgabe, die jede Woche kommt. Den Rest mache ich."
Stimmprobe liegt vor, Videotest läuft (Higgsfield, Bild plus Audio).

**Stufe 2, mittleres Risiko: Mit der KI reden statt tippen (2 Minuten).**
Für Anfänger der leichteste Einstieg überhaupt: Eddie hält das Handy hoch,
ChatGPT im Sprachmodus, und sagt: „Ich habe eine Anfrage aus Dänemark
bekommen, übersetz mir das und antworte auf Dänisch." Die KI antwortet
laut, in Sekunden. Trifft die Bogen-Antwort „überwiegend für Übersetzungen"
und die Leute, die nie tippen wollen. Absicherung: Handy per Kabel an die
Saalanlage, vorher um 8:30 getestet; Backup ist eine Bildschirmaufnahme
vom Vorabend. Ohne Ton im Saal wird der Punkt gestrichen, nicht improvisiert.

**Stufe 3, riskant: Ein echter Roboter-Agent, der Fragen beantwortet.**
ElevenLabs Agents könnte den Roboter als Gesprächspartner bauen: Mikro an,
jemand stellt eine Frage, der Roboter antwortet mit seiner Stimme. Das ist
der größte Wow, aber auch der größte Ausfall: Netz, Latenz, Saalhall,
Missverständnisse. Nicht im 45-Minuten-Slot. Wenn überhaupt, dann in den
15 Minuten Fragen als Bonus, und nur wenn der Test am Morgen sauber war.

## 2. NotebookLM, in ihrer Sprache

Erklärung für den Raum: „Ein KI-Ordner, der nur eure eigenen Unterlagen
kennt. Was nicht im Ordner liegt, weiß er nicht, und das ist der Sinn."

Warum das genau diese Gruppe trifft:
- Bogen-Sorge „Man muss die Quellen immer prüfen": NotebookLM zeigt zu jeder
  Antwort die Fundstelle im eigenen Dokument, ein Klick und man steht drin.
- Bogen-Sorge „Bleibt meine Kommunikation im Haus?": Mit dem Firmenkonto
  (Google Workspace) werden die Unterlagen nicht zum Training genutzt. Mit
  einem privaten Gratis-Konto gilt das nicht, das sagen wir dazu.
- Bogen-Frage „Welche Prompts für Eventplanung inkl. Locationsuche?": Drei
  Hotelangebote als PDF rein, Frage: „Welches Hotel hat Tageslicht im
  Tagungsraum und was kostet die Pauschale?" Antwort mit Fundstelle.

**Demo (4 Minuten, ein Live-Risiko):** Das Notebook ist vorbereitet: die
Ausschreibung, drei Hotelangebote, die Hausordnung des Atlantic. Live wird
nur die eine Frage getippt, Antwort in fünf Sekunden, Fundstelle anklicken.
Dann der Wow, vorproduziert: die „Audio-Übersicht", zwei Stimmen reden
über die eigenen Unterlagen wie ein Podcast. 45 Sekunden abspielen, nicht
live erzeugen (das dauert Minuten). Für Anfänger ist das der Moment, an dem
sie verstehen, was „Gedächtnis" auf der Türme-Folie bedeutet.

Einbau: NotebookLM ist Turm 4. Die Demo ersetzt nichts, sie füllt den
Turm, der bisher nur ein Wort auf der Folie war.

## 3. Der Werkzeugkasten, in ihrer Sprache (eine Folie, 2 Minuten, nichts live)

Sechs Werkzeuge, je ein Satz, was es für Planerinnen tut. Keine Fachwörter.

| Werkzeug | Was es für euch tut | Trifft welche Sorge vom Bogen |
|---|---|---|
| Copilot in Outlook und Teams | Fasst das Meeting zusammen, während ihr noch drin sitzt | „Workflows in Teams" |
| ChatGPT zum Sprechen | Übersetzt und antwortet laut, ohne Tippen | „überwiegend Übersetzungen" |
| NotebookLM | Beantwortet Fragen nur aus euren eigenen Unterlagen | „Quellen prüfen", „bleibt es im Haus" |
| Canva mit KI | Macht aus drei Zeilen die Einladung mit eurem Logo | „Flyer, Einladungen, Plakate" |
| Perplexity | Sucht wie Google, antwortet wie ein Kollege, mit Links | „Locationsuche" |
| Transkription (Scribe, Whisper) | Macht aus der Aufnahme das Protokoll | „Protokolle" (Travemünde) |

Fünf von elf haben Copilot in der Firma. Die Folie sagt nicht „nehmt X",
sie sagt „das, was ihr schon habt, kann mehr, als ihr benutzt".

## 4. Was das mit der Zeit macht

Roboter-Begrüßung kostet 30 Sekunden, Werkzeugkasten 2 Minuten,
NotebookLM 4 Minuten, Sprachmodus 2 Minuten. Das sind 8,5 Minuten, die
nicht da sind. Vorschlag:
- Hotelsuche in drei Stufen von 5 auf 3 Minuten (Stufe 2 nur zeigen, nicht tippen)
- „Vom Zettel zum Plan" auf die Streichliste: gut, aber die vierte Demo
  mit demselben Muster wie die erste
- Bild von 8 auf 6 Minuten (Logo-Schritt nur erzählen, Ergebnis zeigen)
Damit passt es in 45, und jeder Block hat einen Plan B.

## 5. Technikcheck 8:30, Reihenfolge

1. Laptop an den Beamer, Deck laden, Roboter-Clip abspielen (Ton im Saal?)
2. Handy an die Anlage, Sprachmodus einmal fragen, hört man die Antwort hinten?
3. NotebookLM öffnen, Frage stellen, Fundstelle klicken
4. Hotspot als Netz-Reserve, Backup-Ordner mit allen Screenshots offen
Fällt Punkt 2 aus, fällt der Sprachmodus, nicht der Vortrag.
