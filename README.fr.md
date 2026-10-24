<div align="center">

<img src="assets/banner.svg" width="860" alt="wangziru-analysis"/>

# La pensée à la Wang Ziru, 2ᵉ édition · wangziru-analysis

**La réponse d'abord, la raison clairement, et ça tient face aux objections. Une phrase à votre IA suffit pour qu'elle analyse une question, écrive un script, corrige votre texte ou discute un sujet à fond avec vous.**

[![Version](https://img.shields.io/badge/version-v1.12-blue)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/chrislitality-svg/wangziru-analysis-skill-v2/ci.yml?branch=main&label=CI)](.github/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](tools/)
[![Corpus](https://img.shields.io/badge/corpus-103%20videos%20%C2%B70.96M%20chars-8b5cf6)](corpus/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

[![Last Commit](https://img.shields.io/github/last-commit/chrislitality-svg/wangziru-analysis-skill-v2)](https://github.com/chrislitality-svg/wangziru-analysis-skill-v2/commits/main)

[简体中文](README.md) · [English](README.en.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · **Français** · [Deutsch](README.de.md)

</div>

> **Voici la 2ᵉ édition.** Elle a été affinée avec davantage de vidéos ; elle suit donc de plus près sa façon d'expliquer, mais elle colle peut-être aussi davantage aux échantillons d'origine. Pour une version générale qui rédige d'abord un plan avant d'écrire, utilisez la 1ʳᵉ édition, [wangziru-analysis-skill-v1](https://github.com/chrislitality-svg/wangziru-analysis-skill-v1). Les deux valent la peine d'être essayées.

---

## Qu'est-ce que ce dépôt ?

Un skill à installer dans des outils d'IA comme Claude Code, Codex ou Cursor. Une fois installé, aucune commande à apprendre : il suffit de dire une phrase à l'IA.

Il apprend à l'IA à produire du contenu comme Wang Ziru rend une idée claire : donner la réponse d'abord, puis la raison, expliquer comment la chose fonctionne vraiment, et annoncer d'emblée les exceptions et les coûts. Le lecteur n'a pas besoin de savoir qui est Wang Ziru pour comprendre, retenir et transmettre.

La méthode ne repose pas sur des impressions. Nous avons transcrit mot à mot 32 de ses vidéos et les avons lues paragraphe par paragraphe. Chaque procédé du skill cite ses propres mots avec un horodatage que vous pouvez vérifier.

## Mode d'emploi : dites une seule phrase

Les instructions du skill sont en chinois ; il fonctionne donc au mieux si vous demandez en chinois. Vous pouvez aussi indiquer à l'IA la langue de sortie souhaitée.

| Dites ceci | Vous obtenez | Exemple |
|---|---|---|
| 用王自如 skill 分析一下：现在给孩子报编程班还值不值？ (Analyse : un cours de programmation pour mon enfant vaut-il encore le coup ?) | Un court texte prêt à partager : la réponse dès le premier paragraphe, puis le critère, les raisons, les exceptions et des conseils | [Exemple 05](examples/05-分析-孩子要不要学编程.md) |
| 用王自如的方式写一篇 2 分钟口播：为什么收藏了那么多干货还是没进步 (Un script de 2 minutes : pourquoi tant d'astuces sauvegardées ne vous ont pas fait progresser) | Un script à lire tel quel, plus trois lignes (question, réponse, fondement) pour vérifier la logique | [Exemple 06](examples/06-写稿-收藏了那么多干货为什么没进步.md) |
| 我想和王自如聊聊要不要辞职创业，你来当王自如 (Discutons de quitter mon emploi pour créer une entreprise ; joue Wang Ziru) | Un échange où chaque réponse contient un jugement et une raison. L'IA précise qu'elle raisonne à sa manière, ne se fait pas passer pour lui et n'invente pas son passé | [Exemple 07](examples/07-对谈-30岁要不要辞职创业.md) |
| 这是我的逐字稿，王自如帮我改一下：（贴上稿子） (Voici ma transcription, corrige-la) | Les un ou deux problèmes principaux, le texte entier corrigé et l'explication des changements. Votre ton et vos faits sont conservés | [Exemple 08](examples/08-改稿-年轻人要不要考公.md) |

L'installation tient en une ligne : `git clone https://github.com/chrislitality-svg/wangziru-analysis-skill-v2.git ~/.claude/skills/wangziru-analysis`

## D'où vient la méthode : comment tourne son esprit

Les cinq points ci-dessous sont un résumé. Les sources, les contre-exemples et les questions encore ouvertes se trouvent dans [thinking-思维运转.md](references/thinking-思维运转.md).

1. **La réponse d'abord, les raisons ensuite.** Interrogé en direct, il donne le plus souvent la réponse dès la première phrase : « Y a-t-il encore un avenir dans l'industrie du smartphone ? Non. » Puis il explique pourquoi. C'est le plus net avec les questions fermées, mais la plupart des questions ouvertes suivent le même ordre.
2. **Il donne presque toujours la raison.** Il lâche rarement un verdict nu. La raison est d'ordinaire un calcul, une contradiction dans ce que veut l'utilisateur, une limite physique ou une fenêtre déjà refermée, rarement un adjectif.
3. **Il utilise ses propres critères, et les réutilise.** Dans sa vidéo sur Huawei, il a repris les trois critères posés deux semaines plus tôt pour l'iPhone : est-ce perceptible, est-ce utilisé souvent, est-ce que ça vaut l'argent. Nous n'avons vu ce réemploi que deux fois ; on ne peut pas encore parler d'habitude.
4. **Il dit son hésitation à voix haute, puis il choisit.** Sur la polémique Xibei : « Ses problèmes seraient enterrés, retardés, ou n'arriveraient jamais ? Seulement retardés. » Il expose les possibilités et indique laquelle est son avis. Dans les vidéos scénarisées il dit rarement « forcément » ou « absolument » ; en direct, plus souvent.
5. **Les tics verbaux ne sont pas sa signature.** La même année, « 对吧 » (hein ?) apparaît 2 fois pour 10 000 caractères dans une vidéo et 20 fois dans une autre. Imiter ses tics ne vous fera pas parler comme lui.

Nous avons cru que ses jugements étaient tous préparés à l'avance et simplement ressortis sur le moment. Les preuves ne suffisent pas ; nous le traitons comme une hypothèse à tester.

<div align="center">
<img src="assets/mindflow.svg" width="820" alt="Son ordre habituel quand on l'interroge en direct : la réponse d'abord, la raison, une concession seulement s'il y a une vraie exception, une phrase de conclusion quand il en a une"/>
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

# Sa vraie parole, un clip de live de septembre 2026. Score attendu : 0, niveau humain
python tools/ai_flavor_check.py "corpus/clips-jachzhu/2026-09-22-聊西贝事件的根源-1m11s.txt"

# Un brouillon généré par IA fait bondir le score au-delà de 70. Cet écart est ce que la recherche explique
python tools/ai_flavor_check.py brouillon.txt --json
```

Installez le skill sur Claude Code, Codex, Cursor ou un autre assistant de codage IA pour analyser, rédiger, discuter ou corriger un texte directement. L'installation tient en une ligne : `git clone https://github.com/chrislitality-svg/wangziru-analysis-skill-v2.git ~/.claude/skills/wangziru-analysis`

> **Non officiel** · Ce dépôt est une étude de méthode d'expression, sans lien avec Wang Ziru ni son équipe. Elle n'utilise ni sa voix ni son image, et les textes produits ne doivent être signés de son nom ni passer pour lui.

## Corpus et méthodologie

La base lexicale est constituée des 71 vidéos de la chaîne Bilibili « Wang Ziru AI », environ 50 heures et 864 937 caractères. S'y ajoute la publication intégrale de 32 transcriptions horodatées dans `corpus/`, dont 7 vidéos longues officielles d'avril à octobre 2026 et 25 capsules improvisées sans script, si bien que chacun peut reproduire les chiffres du dépôt. La méthode place le codage qualitatif au centre et réserve la lexicométrie à la vérification. L'échantillonnage, les commandes de collecte et de transcription et le guide de reproduction sont dans [`METHODOLOGY.md`](METHODOLOGY.md), les notes brutes du processus de recherche sont ouvertes dans `research/`.

## Communauté

- **Contribuer** : reproduire ou contester les conclusions, annoter de nouveaux corpus, et vérifier le biais d'échantillonnage de la couche improvisée, c'est le problème ouvert le plus important en ce moment. Les traductions sont bienvenues aussi. Voir le [guide de contribution](CONTRIBUTING.md) et le [code de conduite](CODE_OF_CONDUCT.md)
- **Dépôt sœur** : [wangziru-analysis-skill-v1](https://github.com/chrislitality-svg/wangziru-analysis-skill-v1), 1ʳᵉ édition, recette originale, workflow plan d'abord

## Licence

[CC BY-NC 4.0](LICENSE). Utilisation, modification et redistribution libres avec attribution, usage commercial interdit. Les citations d'origine sortent du champ de cette licence. La documentation complète est dans [README.md](README.md) et [README.en.md](README.en.md).
