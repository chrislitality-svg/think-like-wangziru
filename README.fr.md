<div align="center">

<img src="assets/banner.svg" width="860" alt="wangziru-analysis"/>

# Déconstruction de l'expression de Wang Ziru, 2ᵉ édition · wangziru-analysis · V2

**Apprendre la structure, pas l'accent. Étudier comment fonctionne sa pensée, pas imiter ses tics de langage.**

[![Version](https://img.shields.io/badge/version-v1.7-blue)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/chrislitality-svg/wangziru-analysis-skill-v2/ci.yml?branch=main&label=CI)](.github/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](tools/)
[![Corpus](https://img.shields.io/badge/corpus-103%20videos%20%C2%B71.04M%20chars-8b5cf6)](corpus/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

[![Last Commit](https://img.shields.io/github/last-commit/chrislitality-svg/wangziru-analysis-skill-v2)](https://github.com/chrislitality-svg/wangziru-analysis-skill-v2/commits/main)

[简体中文](README.md) · [English](README.en.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · **Français** · [Deutsch](README.de.md)

</div>

> **Voici la 2ᵉ édition, l'édition renforcée par les données.** Elle a été développée sur la 1ʳᵉ édition avec davantage de données vidéo. Elle est plus proche de l'homme lui-même, au risque d'être surajustée à l'échantillon d'origine. Si vous préférez la recette originale plus générique, le workflow qui déconstruit d'abord le sujet et le fait passer par des portes qualité avant d'écrire, utilisez [wangziru-analysis-skill-v1](https://github.com/chrislitality-svg/wangziru-analysis-skill-v1). Essayez les deux.

---

## Qu'est-ce que ce dépôt ?

**Ce dépôt est d'abord un projet de recherche. Il étudie comment la pensée de Wang Ziru fonctionne réellement et quelles sont ses vraies habitudes d'expression.** L'Agent Skill pour assistants de codage IA est le résumé exécutable de cette recherche, il appartient à la couche produit. Lisez les deux couches séparément. L'entrée recherche est [`references/thinking-思维运转.md`](references/thinking-思维运转.md), où chaque conclusion remonte à un fichier du corpus avec son horodatage. L'entrée produit est `SKILL.md`. Les conclusions qui sont des faits mesurés et celles qui sont des règles de rédaction traduites sont distinguées dans le tableau des niveaux de preuve de [`METHODOLOGY.md`](METHODOLOGY.md) §9.

### Découvertes clés : comment tourne son esprit

Le document complet est dans [thinking-思维运转.md](references/thinking-思维运转.md). L'essentiel tient en cinq points.

1. **Le jugement précède le langage.** Interrogé en improvisation, le verdict tombe au premier temps sans délai. « Y a-t-il encore un avenir dans l'industrie du smartphone ? Non. » Ce que le langage ajoute ensuite est toujours un mécanisme, jamais des adjectifs. Dans les vidéos scénarisées, l'ordre s'inverse et les preuves viennent d'abord. Un seul esprit, deux modes de sortie : les jugements sont préfabriqués.
2. **Les règles de mesure sont un stock.** Les jugements puisent dans une bibliothèque de standards de long terme, appelée d'une vidéo à l'autre. La vidéo Huawei réutilise directement la grille à trois cases de la vidéo iPhone18. Un standard apparaît souvent sous forme de question rhétorique.
3. **Les concessions sont explicites.** Les branches de l'hésitation sont dites à voix haute, une est choisie, et l'appartenance est marquée. « 我觉得 » apparaît 6,5 fois par 10 000 caractères, et les mots de prudence dépassent les mots de certitude dans un rapport d'environ 2,7 pour 1. Son assurance vient des définitions et de la numérotation, jamais de « absolument ».
4. **La chute est le format de stockage.** Chaque chaîne de raisonnement se termine par le jugement coulé en une phrase citable, comme « Aucune entreprise ne s'est noyée dans la salive ».
5. **Les tics verbaux s'estompent.** « 对吧 » est passé de 20,8 pour 10 000 caractères dans la base de 71 vidéos à 3,7 dans le corpus 2026. Imiter ses tics revient à imiter ce qu'il est en train d'abandonner. Sa continuité est dans l'ordre de fonctionnement.

<div align="center">
<img src="assets/mindflow.svg" width="820" alt="Un esprit, deux ordres. Les vidéos scénarisées vont des preuves au jugement, les réponses improvisées vont du jugement au mécanisme."/>
</div>

### Modèles recommandés

| Priorité | Modèle | Remarques |
|---|---|---|
| 🥇 **Premier choix** | **Gemini 3.8 Flash** | Il contient tous les fichiers de référence dans un seul contexte, tient des chaînes logiques stables, respecte votre personne et vos faits lors des réécritures, et offre le meilleur rapport qualité-prix |
| 🥈 **Second choix** | **DeepSeek V4 Flash** | C'est l'alternative. Son chinois sonne proche de la référence orale, il est stable sur les formats courts de 2 à 3 minutes et solide avec les vérificateurs de `tools/` |

## Démarrage en 30 secondes

Aucune dépendance. Commencez par goûter le détecteur de saveur IA sur sa vraie parole. C'est la seule entrée exécutable du dépôt, tout le reste est du Markdown.

```bash
git clone https://github.com/chrislitality-svg/wangziru-analysis-skill-v2.git
cd wangziru-analysis-skill-v2

# Sa vraie parole, un clip de live de septembre 2026. Score attendu : 11, niveau humain
python tools/ai_flavor_check.py "corpus/clips-jachzhu/2026-09-22-聊西贝事件的根源-1m11s.txt"

# Un brouillon généré par IA fait bondir le score au-delà de 70. Cet écart est ce que la recherche explique
python tools/ai_flavor_check.py brouillon.txt --json
```

Installez le skill sur Claude Code, Codex, Cursor ou un autre assistant de codage IA pour rédiger, réécrire ou vous coacher directement. L'installation tient en une ligne : `git clone https://github.com/chrislitality-svg/wangziru-analysis-skill-v2.git ~/.claude/skills/wangziru-analysis`

> **Non officiel** · Ce dépôt est une étude de méthode d'expression, sans lien avec Wang Ziru ni son équipe. Elle n'utilise ni sa voix ni son image, et les textes produits ne doivent être signés de son nom ni passer pour lui.

## Corpus et méthodologie

La base lexicale est constituée des 71 vidéos de la chaîne Bilibili « Wang Ziru AI », environ 50 heures et 864 937 caractères. S'y ajoute la publication intégrale de 32 transcriptions horodatées dans `corpus/`, dont 7 vidéos longues officielles d'avril à octobre 2026 et 25 capsules improvisées sans script, si bien que chacun peut reproduire les chiffres du dépôt. La méthode place le codage qualitatif au centre et réserve la lexicométrie à la vérification. L'échantillonnage, les commandes de collecte et de transcription et le guide de reproduction sont dans [`METHODOLOGY.md`](METHODOLOGY.md), les notes brutes du processus de recherche sont ouvertes dans `research/`.

## Communauté

- **Contribuer** : reproduire ou contester les conclusions, annoter de nouveaux corpus, et vérifier le biais d'échantillonnage de la couche improvisée, c'est le problème ouvert le plus important en ce moment. Les traductions sont bienvenues aussi. Voir le [guide de contribution](CONTRIBUTING.md) et le [code de conduite](CODE_OF_CONDUCT.md)
- **Dépôt sœur** : [wangziru-analysis-skill-v1](https://github.com/chrislitality-svg/wangziru-analysis-skill-v1), 1ʳᵉ édition, recette originale, workflow plan d'abord

## Licence

[CC BY-NC 4.0](LICENSE). Utilisation, modification et redistribution libres avec attribution, usage commercial interdit. Les citations d'origine sortent du champ de cette licence. La documentation complète est dans [README.md](README.md) et [README.en.md](README.en.md).
