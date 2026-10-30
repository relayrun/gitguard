# GitHub : correspondance des fonctions essentielles

[English](../en/github.md) · [简体中文](../zh-CN/github.md) · [日本語](../ja/github.md) · [Deutsch](../de/github.md) · [Français](github.md) · [Español](../es/github.md) · [Português (Brasil)](../pt-BR/github.md) · [Русский](../ru/github.md)

[Accueil Git Guard](../../README.fr.md) · [Démarrage rapide](README.md)

Version de base 0.1 — vérifiée par rapport à la documentation GitHub liée le 2026-10-28.

OneDev reste l’exemple principal détaillé de Git Guard. GitHub est le second exemple : appliquez le même [processus quotidien](workflow.md), la même [vérification de sécurité](security-acceptance.md) et les mêmes [conseils de sauvegarde](backup-and-recovery.md). Ce chapitre décrit les fonctions correspondantes, pas les réglages actuels d’un dépôt particulier.

| Exigence commune | Équivalent GitHub |
| --- | --- |
| Préparation et commit locaux | Travail Git local ordinaire ; aucun envoi distant à cette étape |
| Collaboration distante autorisée | Pousser une branche de travail et préparer le texte ; dans l’exemple standard, une personne crée la PR sur le Web |
| Revue obligatoire et main protégée | Configurer les protections/rulesets de branche et les exigences de revue adaptées |
| Restreindre les push forcés et la suppression de références protégées | Laisser les autorisations correspondantes désactivées et examiner les exceptions |
| Fusion finale humaine | Séparer identité et identifiants de l’IA de l’autorité humaine ; une revue obligatoire ne réserve pas à elle seule la fusion |
| Après fusion humaine | Vérifier le résultat, synchroniser main localement avec précaution et ne nettoyer que la branche confirmée terminée |

La documentation GitHub prévoit les branches protégées et les rulesets de branches/tags pour les dépôts publics des offres Free ; leur disponibilité en dépôt privé dépend de l’offre. N’en déduisez pas la disponibilité de toutes les fonctions avancées ou des push rulesets. [Branches protégées](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) · [Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).

Les revues approuvantes obligatoires ne déterminent pas, à elles seules, qui peut fusionner après approbation. Exceptions administrateur des protections classiques, acteurs autorisés, listes de contournement des rulesets, permissions des applications et accès aux identifiants humains comptent également. Les restrictions de push documentées pour les dépôts d’organisation éligibles sont un contrôle à évaluer avec l’obligation de PR ; testez l’identité réelle avant d’affirmer que seule une personne peut fusionner. Le propriétaire doit garder séparément le contrôle de l’administration, de la suppression du dépôt et des modifications de règles.

Dans l’exemple standard, la personne suit le parcours de création d’une pull request : vérifier base (cible) et compare (source), saisir titre et description, soumettre, examiner les différences et contrôles, puis fusionner elle-même. Les approbations indépendantes requises restent applicables ; créer une PR ne l’approuve pas. Le [processus commun](workflow.md) décrit la variante où la création par l’IA est autorisée séparément.

GitHub propose aussi la fusion automatique ; ce processus réserve l’exécution finale à la personne. Ne l’activez pas comme simple commodité annexe. Ne supposez pas qu’un jeton autorise l’écriture sur les branches de travail tout en interdisant toutes les fusions parce que son libellé le dit restreint.

L’exemple de proxy inverse OneDev auto-hébergé ne devient pas un proxy devant le service GitHub. Traduisez l’objectif de protection en identités, règles, permissions d’applications et voies d’accès vérifiées propres à GitHub.

Avant l’adoption, inspectez l’offre réelle du compte, la visibilité du dépôt, les règles actives et exceptions, puis appliquez la matrice commune dans un environnement jetable autorisé. La rédaction de ce chapitre n’a modifié aucun dépôt ni effectué de tests de refus de sécurité.


<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
