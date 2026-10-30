# Sauvegarde indépendante et restauration

[English](../en/backup-and-recovery.md) · [简体中文](../zh-CN/backup-and-recovery.md) · [日本語](../ja/backup-and-recovery.md) · [Deutsch](../de/backup-and-recovery.md) · [Français](backup-and-recovery.md) · [Español](../es/backup-and-recovery.md) · [Português (Brasil)](../pt-BR/backup-and-recovery.md) · [Русский](../ru/backup-and-recovery.md)

[Accueil Git Guard](../../README.fr.md) · [Démarrage rapide](README.md)

Version de base 0.1 — 2026-10-28.

Les permissions et les copies récupérables répondent à des défaillances différentes. La base est une synchronisation automatique vers un appareil indépendant, des contrôles d’intégrité et des points de récupération historiques protégés. **Compilation et lancement de l’application sont facultatifs** : choisissez des contrôles manuels, un déclenchement séparé ou une automatisation supplémentaire selon le projet.

<a id="personal-and-company-schedules"></a>

## Planification individuelle et en entreprise

Une personne peut allumer périodiquement un second ordinateur portable et laisser le déclencheur configuré synchroniser les données. Indiquez s’il s’agit du démarrage système ou de l’ouverture de session ; une tâche déclenchée à la connexion ne s’exécute pas avant celle de cet utilisateur. Une entreprise peut utiliser un appareil indépendant disponible, avec planification quotidienne, rattrapage des exécutions manquées, tentatives réseau limitées, contrôle des exécutions simultanées et échecs visibles.

Ce sont des choix d’implémentation, pas des fonctions livrées par ce guide. Sa lecture n’installe aucun script ni aucune tâche planifiée. Ne donnez pas à l’identité IA de développement le pouvoir de supprimer toutes les versions de récupération ou d’administrer l’appareil de sauvegarde.

<a id="define-what-the-copy-covers"></a>

## Définir ce que couvre la copie

Une extraction de main n’est pas une sauvegarde serveur complète. Précisez la couverture des branches et de l’historique, des travaux locaux/non committés, du code et des documents, des dépendances requises, des ressources d’exécution, de la configuration externe et des projets privés. Conservez les secrets dans un processus de restauration correctement protégé, jamais dans des exemples publics ni dans une archive ordinaire destinée au partage.

Les données Git et les métadonnées de l’hébergement sont distinctes. Une restauration auto-hébergée complète peut aussi nécessiter une base cohérente, comptes et permissions, tickets/PR, pièces jointes, configuration et stockage. Testez la restauration du service séparément de la compilation du code.

Un miroir mis à jour peut répliquer les suppressions. Gardez des points indépendants et protégez la dernière version connue comme bonne. Adaptez la conservation au besoin réel ; n’effacez pas automatiquement les anciennes copies au seul motif qu’un nouveau transfert annonce un succès.

<a id="baseline-checks"></a>

## Contrôles de base

1. Confirmez source, révision/périmètre prévu, destination, identité et espace disponible. Préservez les données sans rapport.
2. Synchronisez sans écraser une copie modifiée ou divergente et sans repousser les changements vers la source. Vérifiez l’égalité exacte avec la révision récupérée prévue ; une branche locale en avance peut autrement sembler déjà à jour.
3. Capturez le périmètre déclaré de façon cohérente, avec un identifiant de point de récupération unique. Enregistrez règles d’inclusion/exclusion et fichiers nécessaires.
4. Vérifiez manifeste et empreintes pertinentes du code, des fichiers et archives. Ouvrir un ZIP, compter ses fichiers ou calculer sa seule empreinte ne prouve pas que les sources nécessaires sont incluses. Tout échec obligatoire doit faire échouer le résultat.
5. Gardez des résultats durables et restaurez périodiquement dans une destination distincte et vide. Distinguez intégrité et restauration ; tant qu’aucune restauration n’a été effectuée, celle-ci est non vérifiée.

<a id="optional-compilation-and-startup"></a>

## Compilation et démarrage facultatifs

Si vous les choisissez, compilez la copie restaurée avec l’outillage réellement pris en charge et une procédure de compilation propre. Consignez configuration, couverture, projets non chargés/exclus et dépendances. Un dossier de restauration vide ne prouve pas une compilation propre si l’archive contient déjà des sorties en cache. Ne laissez pas des fichiers non déclarés du poste de développement initial masquer des omissions.

Une leçon historique utile : une sauvegarde peut contenir les fichiers de projet tout en omettant des sources fournisseur indispensables ; compiler la copie restaurée peut révéler ce manque. La compilation seule ne valide toutefois pas chaque document, ressource d’exécution, base d’hébergement ou parcours applicatif.

Vous pouvez ensuite démarrer l’application restaurée et vérifier ses fonctions de base dans un environnement de test adapté. Évitez les effets sur la production. Pour la documentation ou le contenu statique, choisissez des contrôles pertinents de liens/contenu/site plutôt qu’un compilateur sans rapport.

Marquez compilation/démarrage comme **non sélectionné**, **non vérifié**, **réussi** ou **échoué**, selon le cas. Un contrôle facultatif non sélectionné ne fait pas échouer la sauvegarde de base, et un transfert terminé ne doit pas être déclaré validé par compilation.

<a id="if-validation-fails"></a>

## En cas d’échec de validation

Déterminez s’il s’agit d’une omission dans la sauvegarde, d’un prérequis d’environnement ou d’un défaut applicatif. Corrigez les règles d’inclusion ou l’environnement déclaré, créez un nouveau point, restaurez et répétez les contrôles concernés. Préservez la version bonne précédente et le relevé d’échec. N’écrasez pas silencieusement les preuves d’échec et ne déclarez pas une ancienne sauvegarde réparée sans nouvelle validation.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
