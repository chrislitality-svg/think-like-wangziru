<div align="center">

<img src="assets/banner.svg" width="860" alt="wangziru-analysis"/>

# Analyse des Ausdrucks von Wang Ziru (2. Ausgabe) · wangziru-analysis · V2

**Die Struktur lernen, nicht den Slang — erforschen, wie sein Denken abläuft, statt seine Sprachfloskeln nachzuahmen.**

[![Version](https://img.shields.io/badge/version-v1.7-blue)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/chrislitality-svg/wangziru-analysis-skill-v2/ci.yml?branch=main&label=CI)](.github/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](tools/)
[![Corpus](https://img.shields.io/badge/corpus-103%20videos%20%C2%B71.04M%20chars-8b5cf6)](corpus/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

[![Stars](https://img.shields.io/github/stars/chrislitality-svg/wangziru-analysis-skill-v2?style=social)](https://github.com/chrislitality-svg/wangziru-analysis-skill-v2/stargazers)
[![Forks](https://img.shields.io/github/forks/chrislitality-svg/wangziru-analysis-skill-v2?style=social)](https://github.com/chrislitality-svg/wangziru-analysis-skill-v2/network/members)

[简体中文](README.md) · [English](README.en.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [Français](README.fr.md) · **Deutsch**

</div>

> **2. Ausgabe (V2) — datenverstärkte Edition**: auf der 1. Ausgabe (Originalrezept) mit mehr Videodaten weiterentwickelt — näher am Menschen selbst, aber womöglich auf die Originalstichprobe überangepasst. Für das allgemeinere Originalrezept (Blueprint-Workflow: dekonstruieren → 13 Qualitäts Gates → schreiben) nutze [wangziru-analysis-skill-v1](https://github.com/chrislitality-svg/wangziru-analysis-skill-v1). Probiere beide aus.

---

## Was ist dieses Repository?

**Dieses Repository ist zuerst ein Forschungsprojekt: Wie Wang Zirus Denken tatsächlich funktioniert und was seine echten Ausdrucksgewohnheiten sind.** Der Agent Skill für KI-Coding-Assistenten (`SKILL.md` — schreiben / umschreiben / coachen) ist die ausführbare Zusammenfassung dieser Forschung — die Produktebene. Der Forschungseinstieg ist [`references/thinking-思维运转.md`](references/thinking-思维运转.md) (jede Aussage mit Korpusquelle + Zeitstempel), der Produkteinstieg ist `SKILL.md`; welche Aussagen gemessene Fakten sind und welche abgeleitete Schreibregeln, ist in [`METHODOLOGY.md`](METHODOLOGY.md) §9 abgestuft.

### Kernbefunde: wie sein Kopf arbeitet

1. **Das Urteil geht der Sprache voraus.** Improvisiert gefragt, fällt das Urteil im ersten Schlag ohne Verzögerung („Hat die Smartphone-Branche noch Zukunft? — Nein.“), und was die Sprache danach nachliefert, ist immer ein Mechanismus, nie Adjektive. In Videos mit Skript kehrt sich die Reihenfolge um (erst Belege, dann Urteil). Ein Kopf, zwei Ausgabemodi — die Urteile sind vorgefertigt, nicht spontan erschlossen.
2. **Maßstäbe sind Inventar.** Urteile schöpfen aus einer langfristigen Bibliothek von Standards, videoübergreifend aufgerufen (das Huawei-Video recycelt direkt den Drei-Kaster-Maßstab des iPhone18-Videos); ein Standard erscheint oft als rhetorische Frage.
3. **Zugeständnisse sind explizit.** Die Zweige des Zögerns werden laut ausgesprochen, einer gewählt und als eigenes Urteil markiert („我觉得“ 6,5 pro 10.000 Zeichen; Absicherungs-Wörter übertreffen Gewissheits-Wörter ~2,7:1 — Sicherheit kommt aus Definitionen und Nummerierung).
4. **Der Schlusssatz ist das Speicherformat.** Jede Denkkette endet mit dem in ein einzeln zitierbares Urteil gegossenen Satz („Kein Unternehmen ist jemals im Spucke ertrunken“).
5. **Sprachtics verblassen.** „对吧“ fiel von 20,8 pro 10.000 Zeichen (71-Video-Basis) auf 3,7 im Korpus 2026 — wer seine Tics nachahmt, ahmt nach, was er gerade ablegt. Seine Kontinuität liegt in der Ablaufsordnung, nicht in einem einzelnen Wort.

<div align="center">
<img src="assets/mindflow.svg" width="820" alt="Ein Kopf, zwei Reihenfolgen — Skript-Videos: Belege→Urteil; Improvisation: Urteil→Mechanismus"/>
</div>

### Empfohlene Modelle

| Priorität | Modell | Anmerkung |
|---|---|---|
| 🥇 **Erste Wahl** | **Gemini 3.8 Flash** | Langer Kontext, der alle Referenzdateien auf einmal fasst, stabile Logikketten, bewahrt deine Personen und Fakten beim Umschreiben, bestes Preis-Leistungs-Verhältnis |
| 🥈 **Zweite Wahl** | **DeepSeek V4 Flash** | Alternative: muttersprachlich anmutendes Chinesisch nahe der mündlichen Referenz, stabil bei 2–3-Min-Kurzbeiträgen, solide mit den `tools/`-Prüfern |

## In 30 Sekunden starten

Keine Abhängigkeiten — spüre zuerst den „KI-Geschmack“-Detektor auf seiner echten Rede:

```bash
git clone https://github.com/chrislitality-svg/wangziru-analysis-skill-v2.git
cd wangziru-analysis-skill-v2

# Seine echte Rede (Live-Clip Sept. 2026): KI-Geschmack erwartet ≈ 11 (menschliches Niveau)
python tools/ai_flavor_check.py "corpus/clips-jachzhu/2026-09-22-聊西贝事件的根源-1m11s.txt"

# Ein KI-generierter Entwurf springt auf 70+ — diese Lücke erklärt die Forschung
python tools/ai_flavor_check.py entwurf.txt --json
```

Installation des Skills für KI-Coding-Assistenten (Claude Code / Codex / Cursor usw.): `git clone https://github.com/chrislitality-svg/wangziru-analysis-skill-v2.git ~/.claude/skills/wangziru-analysis`

> **Inoffiziell** · Dies ist eine Untersuchung der Ausdrucksmethode, ohne Bezug zu Wang Ziru oder seinem Team; sie nutzt weder seine Stimme noch sein Abbild, und erzeugte Texte dürfen weder seinen Namen tragen noch als er ausgegeben werden.

## Korpus und Methodik

- **Korpus**: Bilibili-Kanal „Wang Ziru AI“, **71 Videos** (~50 Std., 864.937 Zeichen) + **32 vollständige Transkripte offen veröffentlicht** (`corpus/`, mit Zeitstempeln) — 7 offizielle Langvideos (Apr.–Okt. 2026) und 25 unskriptete Improvisations-Clips. Jede Zahl dieses Repositories ist reproduzierbar.
- **Methodik**: Qualitative Kodierung (Frage-Antwort-Ketten) im Zentrum, Wortfrequenzen nur zur Verifikation. Stichprobe, Sammel- und Transkriptionsbefehle sowie Reproduktionsleitfaden in [`METHODOLOGY.md`](METHODOLOGY.md); rohe Forschungsnotizen offen in `research/`.

## Community

- **Mitwirken**: Ergebnisse reproduzieren/anfechten, neue Korpusvideos kodieren, den Stichproben-Bias der Improvisationsebene prüfen (höchste offene Priorität), Übersetzungen — [Beitragsleitfaden](CONTRIBUTING.md) / [Verhaltenskodex](CODE_OF_CONDUCT.md)
- **Schwester-Repository**: [wangziru-analysis-skill-v1](https://github.com/chrislitality-svg/wangziru-analysis-skill-v1) (1. Ausgabe · Originalrezept · Blueprint-Workflow)

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=chrislitality-svg/wangziru-analysis-skill-v2&type=Date)](https://star-history.com/#chrislitality-svg/wangziru-analysis-skill-v2&Date)

Wenn dir diese Forschung hilft, freue ich mich über einen Stern ⭐

</div>

## Lizenz

[CC BY-NC 4.0](LICENSE): freie Nutzung, Änderung und Weitergabe mit Namensnennung; kommerzielle Nutzung verboten. Originalzitate fallen nicht unter diese Lizenz. Vollständige Forschungsdokumentation (Chinesisch/Englisch): [README.md](README.md) / [README.en.md](README.en.md).
