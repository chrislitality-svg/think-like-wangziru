<div align="center">

<img src="assets/banner.svg" width="860" alt="wangziru-analysis"/>

# Déconstruction de l'expression de Wang Ziru (2ᵉ édition) · wangziru-analysis · V2

**Apprendre la structure, pas l'accent — étudier comment fonctionne sa pensée, pas imiter ses tics de langage.**

[![Version](https://img.shields.io/badge/version-v1.7-blue)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/chrislitality-svg/wangziru-analysis-skill-v2/ci.yml?branch=main&label=CI)](.github/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](tools/)
[![Corpus](https://img.shields.io/badge/corpus-103%20videos%20%C2%B71.04M%20chars-8b5cf6)](corpus/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

[![Stars](https://img.shields.io/github/stars/chrislitality-svg/wangziru-analysis-skill-v2?style=social)](https://github.com/chrislitality-svg/wangziru-analysis-skill-v2/stargazers)
[![Forks](https://img.shields.io/github/forks/chrislitality-svg/wangziru-analysis-skill-v2?style=social)](https://github.com/chrislitality-svg/wangziru-analysis-skill-v2/network/members)

[简体中文](README.md) · [English](README.en.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · **Français** · [Deutsch](README.de.md)

</div>

> **2ᵉ édition (V2) — édition renforcée par les données** : itérée sur la 1ʳᵉ édition (recette originale) avec davantage de données vidéo — plus proche de l'homme lui-même, mais potentiellement surajustée à l'échantillon d'origine. Pour la recette originale plus générique (workflow « plan d'abord » : déconstruire → 13 portes qualité → rédiger), utilisez [wangziru-analysis-skill-v1](https://github.com/chrislitality-svg/wangziru-analysis-skill-v1). Essayez les deux.

---

## Qu'est-ce que ce dépôt ?

**Ce dépôt est d'abord un projet de recherche : comment la pensée de Wang Ziru fonctionne réellement, et quelles sont ses vraies habitudes d'expression.** L'Agent Skill pour assistants de codage IA (`SKILL.md` — rédiger / réécrire / coacher) est le résumé exécutable de cette recherche — la couche produit. L'entrée recherche est [`references/thinking-思维运转.md`](references/thinking-思维运转.md) (chaque conclusion citée avec fichier du corpus + horodatage), l'entrée produit est `SKILL.md` ; quelles conclusions sont des faits mesurés et lesquelles sont des règles de rédaction traduites est gradé dans [`METHODOLOGY.md`](METHODOLOGY.md) §9.

### Découvertes clés : comment tourne son esprit

1. **Le jugement précède le langage.** Interrogé en improvisation, le verdict tombe au premier temps sans délai (« Y a-t-il encore un avenir dans l'industrie du smartphone ? — Non. »), et ce que le langage ajoute ensuite est toujours un mécanisme, jamais des adjectifs. Dans les vidéos scénarisées, l'ordre s'inverse (preuves d'abord, jugement ensuite). Un seul esprit, deux modes de sortie — les jugements sont **préfabriqués**, pas raisonnés sur le vif.
2. **Les règles de mesure sont un stock.** Les jugements puisent dans une bibliothèque de standards de long terme appelée d'une vidéo à l'autre (la vidéo Huawei réutilise directement la grille à trois cases de la vidéo iPhone18) ; un standard apparaît souvent sous forme de question rhétorique.
3. **Les concessions sont explicites.** Les branches de l'hésitation sont dites à voix haute, une est choisie, et l'appartenance est marquée (« 我觉得 » 6,5 pour 10 000 caractères ; les mots de prudence dépassent les mots de certitude ~2,7:1 — l'assurance vient des définitions et de la numérotation).
4. **La chute est le format de stockage.** Chaque chaîne de raisonnement se termine par le jugement coulé en une phrase citable (« Aucune entreprise ne s'est noyée dans la salive »).
5. **Les tics verbaux s'estompent.** « 对吧 » est passé de 20,8 pour 10 000 caractères (base 71 vidéos) à 3,7 dans le corpus 2026 — imiter ses tics, c'est imiter ce qu'il est en train d'abandonner. Sa continuité est dans l'ordre de fonctionnement, pas dans un mot.

<div align="center">
<img src="assets/mindflow.svg" width="820" alt="Un esprit, deux ordres — vidéos scénarisées : preuves→jugement ; improvisation : jugement→mécanisme"/>
</div>

### Modèles recommandés

| Priorité | Modèle | Remarques |
|---|---|---|
| 🥇 **Premier choix** | **Gemini 3.8 Flash** | Contexte long capable de contenir tous les fichiers de référence, chaînes logiques stables, fidélité à votre personne et à vos faits lors des réécritures, meilleur rapport qualité-prix |
| 🥈 **Second choix** | **DeepSeek V4 Flash** | Alternative : chinois au naturel proche de la référence orale, stable sur les formats courts de 2–3 min, solide avec les vérificateurs `tools/` |

## Démarrage en 30 secondes

Zéro dépendance — sentez d'abord le détecteur de « saveur IA » sur sa vraie parole :

```bash
git clone https://github.com/chrislitality-svg/wangziru-analysis-skill-v2.git
cd wangziru-analysis-skill-v2

# Sa vraie parole (clip de live sept. 2026) : saveur IA attendue ≈ 11 (niveau humain)
python tools/ai_flavor_check.py "corpus/clips-jachzhu/2026-09-22-聊西贝事件的根源-1m11s.txt"

# Un brouillon généré par IA fera bondir le score à 70+ — cet écart est ce que la recherche explique
python tools/ai_flavor_check.py brouillon.txt --json
```

Installation du skill pour assistants de codage IA (Claude Code / Codex / Cursor, etc.) : `git clone https://github.com/chrislitality-svg/wangziru-analysis-skill-v2.git ~/.claude/skills/wangziru-analysis`

> **Non officiel** · Il s'agit d'une étude de méthode d'expression, sans lien avec Wang Ziru ni son équipe ; elle n'utilise ni sa voix ni son image, et les textes produits ne doivent pas être signés de son nom ni se faire passer pour lui.

## Corpus et méthodologie

- **Corpus** : chaîne Bilibili « Wang Ziru AI », **71 vidéos** (~50 h, 864 937 caractères) + **32 transcriptions complètes publiées** (`corpus/`, horodatées) — 7 vidéos longues officielles (avr.–oct. 2026) et 25 capsules improvisées sans script. N'importe qui peut reproduire les chiffres de ce dépôt.
- **Méthodologie** : codage qualitatif (chaînes question-réponse) au centre, la lexicométrie ne sert qu'à vérifier. Échantillonnage, commandes de collecte/transcription et guide de reproduction dans [`METHODOLOGY.md`](METHODOLOGY.md) ; notes brutes du processus de recherche ouvertes dans `research/`.

## Communauté

- **Contribuer** : reproduire/contester les conclusions, annoter de nouveaux corpus, vérifier le biais d'échantillonnage de la couche improvisée (problème ouvert prioritaire), traduire — [guide de contribution](CONTRIBUTING.md) / [code de conduite](CODE_OF_CONDUCT.md)
- **Dépôt sœur** : [wangziru-analysis-skill-v1](https://github.com/chrislitality-svg/wangziru-analysis-skill-v1) (1ʳᵉ édition · recette originale · workflow plan d'abord)

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos/chrislitality-svg/wangziru-analysis-skill-v2&type=Date)](https://star-history.com/#chrislitality-svg/wangziru-analysis-skill-v2&Date)

Si cette recherche vous sert, une étoile est appréciée ⭐

</div>

## Licence

[CC BY-NC 4.0](LICENSE) : utilisation, modification et redistribution libres avec attribution ; usage commercial interdit. Les citations d'origine sortent du champ de cette licence. Documentation de recherche complète (chinois/anglais) : [README.md](README.md) / [README.en.md](README.en.md).
