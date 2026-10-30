# Configurer OneDev : droits de l’IA et revue humaine

[English](../en/onedev.md) · [简体中文](../zh-CN/onedev.md) · [日本語](../ja/onedev.md) · [Deutsch](../de/onedev.md) · [Français](onedev.md) · [Español](../es/onedev.md) · [Português (Brasil)](../pt-BR/onedev.md) · [Русский](../ru/onedev.md)

[Accueil Git Guard](../../README.fr.md) · [Démarrage rapide](README.md)

Ce guide **RelayRun Git Guard** explique comment séparer droits humains et IA, protéger main, restreindre les voies contournant la revue et garder des copies indépendantes récupérables sur OneDev auto-hébergé. L’IA committe et pousse les branches de travail dans le périmètre autorisé ; une personne crée la demande, l’examine et effectue la fusion finale sur le Web.

**Git Guard s’adresse aux personnes et équipes utilisant des dépôts Git, pas seulement aux utilisateurs de OneDev.** OneDev et GitHub sont des exemples de configuration. Les autres plateformes de gestion Git peuvent suivre les [principes communs de collaboration et de protection](workflow.md), en vérifiant réglages et résultats selon leurs capacités. Ce chapitre illustre OneDev ; le [guide GitHub](github.md) donne un autre exemple. OneDev est une plateforme tierce, pas un produit RelayRun.

Projet de revue 0.1. Référence d’interface et de dépannage : **OneDev 14.1.0**. Cet exemple est lié à une version ; il ne recommande pas d’installer une ancienne version sans vérifier sa prise en charge actuelle. [Processus](workflow.md) · [Vérification de sécurité](security-acceptance.md) · [Alternative GitHub](github.md)

**Sur cette page :** [Configuration avec l’IA](#visible-ai-assisted-setup) · [Déploiement](#1-select-a-deployment-boundary) · [Identités](#2-establish-separate-identities) · [Protection des branches](#3-initialize-and-protect-the-target-branch) · [Fusion humaine](#4-set-pr-defaults-without-confusing-responsibilities) · [Accès REST](#5-optional-rest-ingress-restriction) · [Pièges fréquents](#6-two-common-pitfalls) · [Vérification et récupération](#7-acceptance-and-recovery) · [Sources](#sources-and-limits)

Avant un commit ou envoi autorisé, suivez le guide pour [configurer et lancer le contrôle](public-content-review.md#configure-the-public-content-check), puis [interpréter et traiter les signalements](public-content-review.md#interpret-results-and-handle-findings).

<a id="visible-ai-assisted-setup"></a>

## Configuration visible assistée par l’IA

Vous pouvez configurer la plateforme manuellement ou demander à l’IA de suivre ce guide et la compétence de configuration dans une interface Computer Use visible. Identifiez d’abord projet exact, acteur, réglages à modifier et retour arrière. La personne approuve ce périmètre et peut observer les actions ; aucun droit administrateur caché ou permanent n’en découle.

Pour les contrôles administratifs, utilisez une session temporaire supervisée, réservée aux modifications prévues. La personne saisit les identifiants sensibles sans les placer dans la conversation, les captures ou les fichiers du dépôt. Ne réutilisez pas une session administrateur pour contourner une action quotidienne refusée. À la fin, relisez les réglages, effectuez les vérifications au périmètre adapté, fermez la session privilégiée et revenez à l’identité quotidienne restreinte. Si l’interface disponible ne permet pas une étape, signalez-le et laissez-la à la personne ; ne prétendez pas avoir effectué un clic inexistant.

Observer l’écran aide à comprendre la configuration ; les permissions imposées et leurs tests apportent la protection.

<a id="1-select-a-deployment-boundary"></a>

## 1. Choisir une frontière de déploiement

Préférez un ordinateur, serveur ou NAS indépendant dont l’architecture et la prise en charge des conteneurs correspondent à la version OneDev choisie. Gardez serveur, moteur de conteneurs, stockage, sauvegardes et identifiants administrateur hors de portée de l’identité IA de développement. Sur un même hôte, des droits explicites de système et de fichiers sont nécessaires ; Docker seul n’assure pas cette séparation.

Utilisez le guide officiel et l’[exemple paramétrable](../../examples/onedev/README.md). Avant de démarrer, choisissez versions/digests d’images pris en charge, emplacement de données indépendant, accès TLS et méthode de récupération. L’exemple expose uniquement une passerelle sur l’interface de bouclage, omet le socket Docker et désactive les correspondances directes HTTP/SSH sur l’hôte. C’est une configuration de départ, pas une installation de production testée. Les compilations en conteneurs peuvent nécessiter un exécuteur conçu séparément.

<a id="2-establish-separate-identities"></a>

## 2. Établir des identités distinctes

| Emplacement à examiner | Action | Vérification |
| --- | --- | --- |
| Administration → Users / Groups | Séparer personne chargée de la revue/administration, contributeur IA et identité de sauvegarde en lecture seule | Appartenances et identifiants réels, y compris les accès hérités |
| Administration → Roles | Examiner les droits de code, gestion de projet et autres du rôle retenu | Le nom du rôle ne suffit pas ; l’IA ne doit ni posséder/administrer les projets ni modifier les protections |
| Project → Settings → Authorizations → Users / Groups | N’accorder que le périmètre nécessaire ; examiner les parents | L’identité de sauvegarde lit uniquement le dépôt prévu ; les droits IA correspondent au modèle déclaré |
| Project → Settings → General | Examiner le projet parent et le rôle effectif par défaut | Aucun accès anonyme/par défaut ni propriété héritée involontaire |

Dans le rôle Code Writer de référence, l’option « Manage Pull Requests » désactivée concerne les opérations de gestion/en masse ; elle ne prouve pas qu’un code writer ne peut jamais effectuer la fusion finale. Testez ce droit séparément après une approbation humaine valide. N’exposez pas une session Web humaine ni un jeton administrateur à l’identité IA quotidienne. La session supervisée et limitée décrite plus haut est temporaire et ne doit pas rester disponible pour le travail Git ordinaire.

<a id="3-initialize-and-protect-the-target-branch"></a>

## 3. Initialiser et protéger la branche cible

Initialisez la branche à protéger dans le processus de configuration contrôlé par la personne, avant d’activer une règle empêchant sa création. Ne désactivez pas régulièrement les protections pour laisser l’IA l’initialiser ou la réparer.

Ouvrez **Project → Settings → Code → Branch Protection**. Dans l’interface de référence, choisissez la branche protégée, souvent `main`, et les sujets concernés ; la référence utilise `anyone`. Lisez l’ordre des règles : dans cette version, les règles locales précèdent celles du parent et la première correspondance s’applique. Une règle enfant peut masquer une règle parent plus stricte ; examinez le comportement effectif.

| Option | Raisonnement nécessaire |
| --- | --- |
| Prevent forced push | Activer pour la branche protégée ; vérifier dans un dépôt jetable qu’une vraie réécriture non autorisée est refusée |
| Prevent deletion | Protéger la branche ; supprimer le dépôt relève d’une autre permission |
| Prevent creation | Décider après l’initialisation ; ne remplace pas la protection des mises à jour/revues |
| Required reviewers | Choisir un réviseur humain indépendant avec le sélecteur ; vérifier l’expression et le compte obtenus |
| Required builds / signatures | Choisir selon le projet, avec des contrôles réellement exécutés et des clés de signature fiables |
| File/tag protection | Définir uniquement le périmètre nécessaire ; les règles de branche ne prouvent pas la protection des tags ou versions |

La référence initiale n’exigeait aucun réviseur ; des obligations ont ensuite été ajoutées. Bloquer le push forcé **ne bloque pas** un push direct ordinaire en fast-forward. Testez-le explicitement. Un réviseur nommé qui soumet aussi la PR peut être traité différemment par l’implémentation de référence ; la séparation humain/IA est essentielle. Ne présentez pas cette configuration comme réservant la fusion aux humains avant d’avoir testé cette capacité séparément.

Enregistrez les changements de configuration délibérés uniquement dans leur autorisation. Relisez valeurs et identités correspondantes ; une capture montre la configuration, pas son application effective.

<a id="4-set-pr-defaults-without-confusing-responsibilities"></a>

## 4. Régler les valeurs par défaut des PR sans confondre les responsabilités

Ouvrez **Project → Settings → Pull Requests**. Vérifiez si chaque champ est local ou hérité.

- **Default merge strategy:** la référence utilise Squash. Une valeur par défaut n’interdit pas les autres stratégies.
- **Default assignee:** responsabilité du travail, pas réviseur obligatoire.
- **Delete source branch after merge:** nettoyage facultatif, également soumis aux droits de l’acteur. N’en déduisez jamais qu’il faut supprimer toutes les anciennes branches.
- Avant la transmission, examinez toujours source, cible, diff, titre et contrôles. Une personne examine et effectue la fusion finale ; l’IA ne clique pas sur la fusion et n’active pas l’automatisation.

Après un squash, vérifiez le changement intégré par rapport à l’historique réel de la cible. Des identifiants de commits différents ne signifient pas, à eux seuls, une perte de contenu. Suivez le processus commun de synchronisation sûre et de nettoyage limité.

<a id="daily-human-request-creation"></a>

### Création quotidienne des demandes par une personne

Après le push de la branche autorisée et la proposition du titre/de la description par l’IA, la personne ouvre la page des pull requests, crée une demande, vérifie source et cible, saisit le texte et soumet. Lisez le diff et les résultats réels des contrôles/revues avant de confirmer personnellement la fusion. Voir la [transmission complète](workflow.md). Si le créateur est également un réviseur obligatoire, vérifiez les règles d’approbation de votre version ; faites intervenir un autre humain autorisé si nécessaire au lieu d’affaiblir la protection.

<a id="5-optional-rest-ingress-restriction"></a>

## 5. Restriction facultative de l’accès REST

Un déploiement auto-hébergé peut bloquer l’espace REST à sa passerelle tout en permettant les voies Web/Git nécessaires. L’[exemple de passerelle](../../examples/onedev/README.md) décrit ce modèle. Des intégrations peuvent cesser de fonctionner ; retenez-le uniquement s’il convient au service.

Examinez chaque voie : port direct du backend, SSH, autre nom d’hôte, IPv6, tunnels, sessions Web authentifiées, tâches serveur et administration hôte/conteneur. Un point d’accès bloqué au proxy ne prouve pas le blocage des autres voies. Incluez chemins normalisés, variantes de casse/encodage, vraies opérations Git et WebSockets nécessaires dans la vérification. Une panne réseau ne prouve pas un refus de permission.

<a id="6-two-common-pitfalls"></a>

## 6. Deux pièges fréquents

<a id="pr-source-branch-is-not-suggested"></a>

### La branche source n’est pas proposée pour la PR

Dans la référence 14.1.0, les suggestions de branche source tiennent compte de l’adresse de l’auteur du dernier commit et des adresses vérifiées de l’utilisateur connecté. Examinez cet auteur et l’utilisateur prévu. Ajoutez uniquement une adresse contrôlée par cet utilisateur via ses réglages Email Addresses, puis suivez la vérification normale. Le comportement d’un administrateur n’implique pas qu’un utilisateur ordinaire puisse éviter cette vérification.

Rouvrez la création de PR et vérifiez source et cible. Choisir la branche manuellement est aussi valide. Cela corrige une suggestion, sans fusion automatique ni approbation. Ne changez pas l’identité Git globale et ne réécrivez pas l’historique simplement pour faire apparaître la suggestion. Une source explicitement choisie est prioritaire.

<a id="a-ready-pr-remains-marked-work-in-progress"></a>

### Une PR prête reste marquée comme travail en cours

L’implémentation de référence considère un titre commençant par `wip` ou `[wip]`, sans distinction de casse, comme en cours et bloque la fusion. Ce n’est **pas** une interdiction de tous les titres commençant par une lettre anglaise. La règle porte sur le titre de la PR, éventuellement dérivé d’un message de commit ou d’une branche.

Ne retirez le marqueur que lorsque le travail est réellement prêt. Revues obligatoires, contrôles et fusion finale humaine restent nécessaires ; le blocage WIP ne prouve pas une frontière de permission de fusion. Vérifiez la règle dans la version déployée.

<a id="7-acceptance-and-recovery"></a>

## 7. Vérification et récupération

Utilisez la [matrice commune](security-acceptance.md) et le [modèle de preuves](../../templates/security-acceptance.csv). Commencez par un inventaire en lecture seule ; obtenez l’autorisation appropriée avant les tests de refus dans un dépôt jetable. Consignez acteur, version, voies, contrôle, états avant/après et vraie raison du refus. Un échec inexpliqué ou un test manquant est « non vérifié ».

Conservez des versions indépendantes récupérables des dépôts **et** des données/configurations du service selon le [guide de sauvegarde](backup-and-recovery.md). Un clone mis à jour n’est pas une sauvegarde OneDev complète. Compilation et démarrage sont facultatifs et ne valident pas toutes les bases serveur ou pièces jointes.

<a id="sources-and-limits"></a>

## Sources et limites

- [Installation officielle en conteneur](https://docs.onedev.io/installation-guide/run-as-docker-container) et [configuration du proxy inverse](https://docs.onedev.io/administration-guide/reverse-proxy-setup).
- [Sélection de branche source dans la version de référence](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/web/page/project/pullrequests/create/NewPullRequestPage.java).
- [Conditions WIP et de fusion de la PR dans cette version](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/model/PullRequest.java).
- [Protection des branches dans cette version](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/model/support/code/BranchProtection.java) et [contrôles de push](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/git/hook/GitPreReceiveCallback.java).

Ce tutoriel combine observations d’interface et examen des sources liés à une version. Sa rédaction n’installe pas OneDev et ne certifie aucun autre serveur, rôle, modèle de NAS, proxy ou version.

**Suite :** vérifiez les permissions configurées avec la [matrice](security-acceptance.md), puis suivez le [processus en quatre étapes et le nettoyage](workflow.md). Revenez à la [présentation Git Guard](../../README.fr.md) pour découvrir le produit.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
