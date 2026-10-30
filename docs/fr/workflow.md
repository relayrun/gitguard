# Processus Git quotidien

[English](../en/workflow.md) · [简体中文](../zh-CN/workflow.md) · [日本語](../ja/workflow.md) · [Deutsch](../de/workflow.md) · [Français](workflow.md) · [Español](../es/workflow.md) · [Português (Brasil)](../pt-BR/workflow.md) · [Русский](../ru/workflow.md)

[Accueil Git Guard](../../README.fr.md) · [Démarrage rapide](README.md)

Version de base 0.1 — 2026-10-28.

<a id="read-and-scope-the-work"></a>

## Lire les consignes et délimiter le travail

Identifiez précisément le projet, le dossier local, la branche, le dépôt distant, sa visibilité et l’autorisation actuelle. Lisez les consignes d’entrée de l’agent, le plan en cours et les instructions applicables. Préservez les modifications étrangères à la tâche, indexées ou non. Modifier, committer, pousser, créer une PR, publier une version et déployer un site sont des actions distinctes ; conservez les autorisations effectivement accordées sans prendre un plan général pour une permission de tout exécuter.

<a id="step-1--record-the-local-change"></a>

## Étape 1 — enregistrer la modification localement

Examinez la liste des fichiers modifiés et leurs différences. Effectuez les contrôles adaptés. Pour un contenu public, terminez la [revue avant publication](public-content-review.md) **avant le commit**, même si celui-ci doit d’abord rester local. Indexez uniquement les fichiers prévus et créez le commit local autorisé. Relisez son identifiant, son contenu et les modifications restant dans l’arbre de travail.

Un commit local ne téléverse rien. N’initialisez pas discrètement un autre dépôt, n’ajoutez pas de dépôt distant, ne modifiez pas les protections et ne créez pas de tâche de sauvegarde à l’occasion d’une simple modification. Ne supprimez pas des changements sans rapport pour obtenir un état propre.

<a id="step-2--share-the-branch-and-prepare-the-pr"></a>

## Étape 2 — partager la branche et préparer la PR

Dans le cadre autorisé, vérifiez la destination distante et l’ensemble des différences de la branche par rapport à la vraie cible. Incluez les anciens commits de la branche encore non fusionnés, et pas seulement le dernier. Revérifiez la séparation entre contenu public et privé avant tout envoi.

Poussez la branche de travail autorisée sans forcer. Dans l’exemple standard de la page d’accueil et de l’animation, préparez les bonnes branches source et cible, un titre et une description proposés ainsi que les résultats réels des contrôles ; la personne crée ensuite la demande dans l’interface Web. Un formulaire préparé n’est pas une PR créée.

Un utilisateur peut autoriser séparément l’IA à créer ou modifier la PR correspondante. Effectuez alors seulement cette action et vérifiez son existence et son état réels. Cette variante ne donne pas le droit de fusion finale. Une branche poussée ou une PR brouillon dans un dépôt public expose déjà son contenu ; celui-ci n’attend pas la fusion pour devenir public.

Si une règle ou une permission bloque l’action, signalez le refus réel. Ne le contournez pas par une session administrateur, un autre jeton, un port serveur direct, un accès au conteneur ou une autre interface. Résoudre un conflit de contenu n’étend pas implicitement l’autorisation.

<a id="human-final-review-and-merge"></a>

## Revue et fusion finales par une personne

Dans l’exemple standard, ouvrez la page des demandes du dépôt dans OneDev/GitHub, lancez une nouvelle demande, vérifiez les branches proposées, saisissez titre et description, puis soumettez-la. Si une demande existe déjà selon une procédure autorisée séparément, examinez-la au lieu d’en créer un doublon. Une branche proposée par défaut n’est pas une approbation.

La personne examine l’ensemble des différences, les preuves de test, la cible et le résultat attendu, puis effectue la fusion finale. Dans ce processus, l’IA ne clique pas sur la fusion, n’appelle pas d’API ou de commande de fusion et n’active pas la fusion automatique à sa place.

L’obligation de revue et le droit exclusif de fusion humaine sont deux contrôles distincts. Une revue réussie peut encore laisser à l’IA la capacité de fusionner. Vérifiez les deux avant d’affirmer que le processus est imposé techniquement. Protégez aussi les identifiants administrateur et les sessions Web existantes, au-delà du compte du robot.

<a id="after-the-human-confirms-merge"></a>

## Après confirmation de la fusion par la personne

1. Vérifiez la fusion réelle côté serveur et sa cible. Une instruction de préparer une PR n’annonce pas sa fusion.
2. Récupérez les références et comparez le changement examiné avec le résultat intégré. Squash/rebase peuvent modifier les identifiants de commits ; si la cible a avancé, comparez la bonne base et le diff obtenu plutôt que d’exiger des arbres complets identiques. Pour un squash sur la même base, l’équivalence des arbres finaux constitue une preuve utile.
3. Avant le nettoyage, vérifiez les changements non committés, les commits non publiés, les autres arbres de travail et les dispositions de récupération/conservation applicables. Ne créez pas de sauvegarde non demandée et n’écrasez pas un travail uniquement local pour forcer l’alignement.
4. Avancez la branche protégée locale par fast-forward si sa relation avec le dépôt distant le permet. Arrêtez-vous et expliquez une divergence au lieu de l’effacer par réinitialisation.
5. Supprimez uniquement la branche de travail confirmée terminée, dans le périmètre de nettoyage autorisé. Si le serveur l’a déjà supprimée, élaguez sa référence de suivi obsolète sans la recréer. Un squash peut ne pas satisfaire un test de suppression fondé uniquement sur l’ascendance ; vérifiez contenu et travail conservé avant toute autre méthode autorisée.
6. Indiquez l’état réel des branches et arbres de travail, les travaux conservés et les problèmes non résolus. Le nettoyage local n’équivaut ni au déploiement ni à la publication d’une version.

<a id="keep-the-rules-portable"></a>

## Garder des règles transposables

Le propriétaire définit les conventions de nommage et de revue. OneDev et GitHub ont des contrôles et modèles de comptes différents ; l’ordre général reste le même. La [vérification de sécurité](security-acceptance.md) distingue la règle souhaitée de la frontière de permissions effectivement testée ; le [guide GitHub](github.md) précise les différences de cette plateforme.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
