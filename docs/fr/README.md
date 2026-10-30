# Git Guard — Démarrage rapide

[English](../en/README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [Deutsch](../de/README.md) · [Français](README.md) · [Español](../es/README.md) · [Português (Brasil)](../pt-BR/README.md) · [Русский](../ru/README.md)

[Accueil Git Guard](../../README.fr.md)

Présentation, démarrage rapide, les sept guides détaillés et vidéo sont disponibles en français. OneDev et GitHub sont des exemples ; les principes peuvent être adaptés à d’autres plateformes Git. Cette traduction est à relire et ne remplace pas une vérification des droits réels.

Avant un commit ou envoi autorisé, suivez le guide pour [configurer et lancer le contrôle](public-content-review.md#configure-the-public-content-check), puis [interpréter et traiter les signalements](public-content-review.md#interpret-results-and-handle-findings).

## Se faire aider par l’IA pour la configuration

Suivez le manuel vous-même, ou confiez le manuel et la compétence adaptée à un assistant. **Privilégiez une utilisation visible de l’interface, par Computer Use :** observez les actions, accordez les droits nécessaires au périmètre prévu et saisissez vous-même les informations sensibles. Ensuite, fermez la session administrative temporaire et rendez à l’IA son identité quotidienne limitée.

| Environnement | Point de départ |
| --- | --- |
| OneDev auto-hébergé | [Manuel](onedev.md) · [Compétence de configuration et de vérification (anglais)](../../skills/gitguard-onedev-safety/SKILL.md) |
| GitHub | [Guide GitHub](github.md) |
| Autres plateformes Git | Adapter le [processus commun](workflow.md) et la [matrice de vérification](security-acceptance.md) à leurs permissions et interfaces. |

La configuration initiale comprend quatre points : définir dépôt, branche principale et identités distinctes ; configurer les protections ; vérifier opérations permises et refusées dans un dépôt de test isolé et autorisé ; organiser les [sauvegardes et la restauration](backup-and-recovery.md). Inutile de tout recommencer à chaque modification : revérifiez les parties concernées lorsque les droits, règles ou environnements changent.

## Quatre étapes au quotidien

Utilisez la [compétence de collaboration (anglais)](../../skills/gitguard-workflow/SKILL.md) et le processus Git de votre projet.

| Étape | Ce que vous dites ou faites | Ce que fait l’IA |
| --- | --- | --- |
| 1. Commit local | « Exécute l’étape 1 selon Git.md. » | Lit le processus, vérifie les modifications et crée un commit local. Rien n’est encore envoyé. |
| 2. Push et préparation | « Exécute l’étape 2 selon Git.md. » | Pousse la branche autorisée et prépare titre, description et résultats des contrôles. |
| 3. Revue et fusion humaines | Créez la demande sur le Web ; vérifiez branches source et cible, titre, description, différences et contrôles ; puis fusionnez. | Fournit des explications et de l’aide. Une personne effectue la fusion finale. |
| 4. Clôture après fusion | « J’ai fusionné. Vérifie le résultat et effectue le nettoyage. » | Vérifie le contenu réellement intégré, synchronise main sans risque pour les travaux locaux et ne supprime que les branches confirmées terminées. |

`Git.md` désigne le document de votre projet ; son nom peut différer. Vous décidez quand créer un commit, pousser et fusionner. [Processus complet](workflow.md)

## Protection et récupération

Une configuration présente ne prouve pas que les protections fonctionnent. Les tests de refus exigent une autorisation précise et un dépôt de test jetable ; indiquez les voies non vérifiées. Prévoyez une synchronisation indépendante et des points de récupération historiques protégés. Une compilation propre et le lancement du programme restent des contrôles facultatifs selon le projet.

Dans l’exemple OneDev, l’adresse vérifiée de l’auteur peut influencer la branche source suggérée, sans effectuer de fusion. Les préfixes WIP du titre peuvent bloquer la fusion dans la version de référence ; tous les titres commençant par une lettre ne sont pas interdits.

## Guides détaillés

- [Processus quotidien](workflow.md)
- [Configuration OneDev](onedev.md)
- [Correspondance GitHub](github.md)
- [Vérification de sécurité](security-acceptance.md)
- [Sauvegarde et restauration](backup-and-recovery.md)
- [Revue du contenu public](public-content-review.md)
- [Animation et langues](animation-and-language.md)
- [Skills](../../skills/README.md) · [Templates](../../templates/README.md)

Compétences, modèles, exemples de déploiement et outils de contrôle restent des ressources communes en anglais.

L’IA prépare les modifications ; une personne les examine et effectue la fusion finale.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
