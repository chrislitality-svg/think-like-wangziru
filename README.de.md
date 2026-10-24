<div align="center">

<img src="assets/banner.svg" width="860" alt="wangziru-analysis"/>

# Analyse des Ausdrucks von Wang Ziru, 2. Ausgabe · wangziru-analysis · V2

**Die Struktur lernen, nicht den Slang. Erforschen, wie sein Denken abläuft, statt seine Sprachfloskeln nachzuahmen.**

[![Version](https://img.shields.io/badge/version-v1.10-blue)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/chrislitality-svg/wangziru-analysis-skill-v2/ci.yml?branch=main&label=CI)](.github/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](tools/)
[![Corpus](https://img.shields.io/badge/corpus-103%20videos%20%C2%B70.96M%20chars-8b5cf6)](corpus/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

[![Last Commit](https://img.shields.io/github/last-commit/chrislitality-svg/wangziru-analysis-skill-v2)](https://github.com/chrislitality-svg/wangziru-analysis-skill-v2/commits/main)

[简体中文](README.md) · [English](README.en.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [Français](README.fr.md) · **Deutsch**

</div>

> **Dies ist die 2. Ausgabe, die datenverstärkte Edition.** Sie wurde auf der 1. Ausgabe mit mehr Videodaten weiterentwickelt. Sie kommt dem Menschen selbst näher, läuft dafür aber Gefahr, auf die Originalstichprobe überangepasst zu sein. Wer das allgemeinere Originalrezept möchte, also den Workflow, der ein Thema erst zerlegt und durch Qualitäts Gates schickt, bevor geschrieben wird, nutzt [wangziru-analysis-skill-v1](https://github.com/chrislitality-svg/wangziru-analysis-skill-v1). Probiere beide aus.

---

## Was ist dieses Repository?

**Dieses Repository ist zuerst ein Forschungsprojekt. Es untersucht, wie Wang Zirus Denken tatsächlich funktioniert und was seine echten Ausdrucksgewohnheiten sind.** Der Agent Skill für KI-Coding-Assistenten ist die ausführbare Zusammenfassung dieser Forschung und gehört zur Produktebene. Lies die beiden Ebenen getrennt. Der Forschungseinstieg ist [`references/thinking-思维运转.md`](references/thinking-思维运转.md), dort lässt sich jede Aussage auf Korpusdatei und Zeitstempel zurückverfolgen. Der Produkteinstieg ist `SKILL.md`. Welche Aussagen gemessene Fakten sind und welche abgeleitete Schreibregeln, steht in der Nachweistabelle in [`METHODOLOGY.md`](METHODOLOGY.md) §9.

### Kernbefunde: wie sein Kopf arbeitet

Das vollständige Dokument steht in [thinking-思维运转.md](references/thinking-思维运转.md). Das Wichtigste in fünf Punkten.

1. **Beim Improvisieren kommt das Urteil oft vor den Gründen.** Von 72 Antwort-Einheiten aus 25 Clips beginnen 72 % mit einem Urteil (90 % bei Ja/Nein-Fragen, 65 % bei offenen Fragen), und 89 % liefern danach einen Mechanismus. „Hat die Smartphone-Branche noch Zukunft? Nein." Danach folgt meist ein Mechanismus, keine Adjektive. Früher schlossen wir daraus: „Skript-Videos gehen von den Belegen zum Urteil, Improvisation kehrt das um, also sind seine Urteile vorgefertigt." v1.9 zieht das zurück: Auch Skript-Videos nennen das Urteil oft zuerst (iPhone 18 [00:58]), der Clip-Ersteller bestimmt den Einstiegspunkt, und die meisten Fragen sind Ja/Nein-Fragen. „Vorgefertigt" ist nur noch eine zu prüfende Hypothese.
2. **Maßstäbe sind Inventar.** Urteile schöpfen aus einer langfristigen Bibliothek von Standards, die videoübergreifend aufgerufen wird. Das Huawei-Video recycelt direkt den Drei-Kaster-Maßstab des iPhone18-Videos. Ein Standard erscheint oft als rhetorische Frage.
3. **Zugeständnisse sind explizit.** Die Zweige des Zögerns werden laut ausgesprochen, einer wird gewählt und als eigenes Urteil markiert. „我觉得" kommt 6,5-mal pro 10.000 Zeichen vor, und Absicherungs-Wörter übertreffen Gewissheits-Wörter etwa 2,7 zu 1. Seine Sicherheit kommt aus Definitionen und Nummerierung, nie aus „absolut".
4. **Der Schlusssatz ist das Speicherformat.** Jede Denkkette endet damit, dass das Urteil in ein einzeln zitierbares Urteil gegossen wird, etwa „Kein Unternehmen ist jemals im Spucke ertrunken".
5. **Sprachtics schwanken stark von Video zu Video.** In sechs Solo-Langvideos von 2026 liegt „对吧" zwischen 2,4 und 20,0 pro 10.000 Zeichen, und die beiden September-Videos liegen über dem Langvideo-Durchschnitt der 71-Video-Basis (etwa 15). Die frühere Aussage „Tics verblassen, 20,8 → 3,7" beruhte an beiden Enden auf falschen Nennern und überlappenden Stichproben und ist in v1.9 zurückgezogen. Sicher ist: Über seine Tics erfasst man ihn nicht, dieselbe Person schwankt im selben Jahr um den Faktor acht.

<div align="center">
<img src="assets/mindflow.svg" width="820" alt="Zu prüfende Hypothese: Skript-Videos Belege→Urteil, Improvisation Urteil→Mechanismus. Die erste Hälfte hat Gegenbeispiele, die zweite kann von Schnitt, Frageform und Thema herrühren."/>
</div>

### Empfohlene Modelle

| Priorität | Modell | Anmerkung |
|---|---|---|
| 🥇 **Erste Wahl** | **Gemini 3.8 Flash** | Er fasst alle Referenzdateien in einen Kontext, hält stabile Logikketten, bewahrt beim Umschreiben deine Personen und Fakten und bietet das beste Preis-Leistungs-Verhältnis |
| 🥈 **Zweite Wahl** | **DeepSeek V4 Flash** | Das ist die Alternative. Sein Chinesisch klingt nah an der mündlichen Referenz, es bleibt stabil bei 2 bis 3 Minuten kurzen Beiträgen und läuft solide mit den Prüfern in `tools/` |

## In 30 Sekunden starten

Keine Abhängigkeiten. Probiere zuerst den KI-Geschmack-Detektor auf seiner echten Rede. Das ist der einzige ausführbare Einstieg im Repository, alles andere ist Markdown.

```bash
git clone https://github.com/chrislitality-svg/wangziru-analysis-skill-v2.git
cd wangziru-analysis-skill-v2

# Seine echte Rede, ein Live-Clip von September 2026. Erwartet: KI-Geschmack 0, menschliches Niveau
python tools/ai_flavor_check.py "corpus/clips-jachzhu/2026-09-22-聊西贝事件的根源-1m11s.txt"

# Ein KI-generierter Entwurf springt über 70. Diese Lücke ist es, die die Forschung erklärt
python tools/ai_flavor_check.py entwurf.txt --json
```

Installiere den Skill auf Claude Code, Codex, Cursor oder einem anderen KI-Coding-Assistenten und schreibe, schreibe um oder lass dich coachen. Die Installation ist eine Zeile: `git clone https://github.com/chrislitality-svg/wangziru-analysis-skill-v2.git ~/.claude/skills/wangziru-analysis`

> **Inoffiziell** · Dies ist eine Untersuchung der Ausdrucksmethode und hat nichts mit Wang Ziru oder seinem Team zu tun. Sie nutzt weder seine Stimme noch sein Abbild, und erzeugte Texte dürfen weder seinen Namen tragen noch als er ausgegeben werden.

## Korpus und Methodik

Die Wortfrequenz-Basis bilden 71 Videos des Bilibili-Kanals „Wang Ziru AI", rund 50 Stunden mit 864.937 Zeichen. Dazu kommen 32 vollständige Transkripte mit Zeitstempeln, offen in `corpus/`, darunter 7 offizielle Langvideos von April bis Oktober 2026 und 25 unskriptete Improvisations-Clips. Damit kann jede Zahl dieses Repositories nachgerechnet werden. Die Methode setzt auf qualitative Kodierung, Wortfrequenzen dienen nur der Verifikation. Stichprobe, Sammel- und Transkriptionsbefehle sowie der Reproduktionsleitfaden stehen in [`METHODOLOGY.md`](METHODOLOGY.md), die rohen Forschungsnotizen sind in `research/` offen.

## Community

- **Mitwirken**: Ergebnisse reproduzieren oder anfechten, neue Korpusvideos kodieren und den Stichproben-Bias der Improvisationsebene prüfen, das ist gerade das wichtigste offene Problem. Übersetzungen sind ebenfalls willkommen. Siehe [Beitragsleitfaden](CONTRIBUTING.md) und [Verhaltenskodex](CODE_OF_CONDUCT.md)
- **Schwester-Repository**: [wangziru-analysis-skill-v1](https://github.com/chrislitality-svg/wangziru-analysis-skill-v1), 1. Ausgabe, Originalrezept, Blueprint-Workflow

## Lizenz

[CC BY-NC 4.0](LICENSE). Freie Nutzung, Änderung und Weitergabe mit Namensnennung, kommerzielle Nutzung verboten. Originalzitate fallen nicht unter diese Lizenz. Die vollständige Dokumentation steht in [README.md](README.md) und [README.en.md](README.en.md).
