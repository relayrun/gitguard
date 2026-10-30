# Spécification de vérification de sécurité

[English](../en/security-acceptance.md) · [简体中文](../zh-CN/security-acceptance.md) · [日本語](../ja/security-acceptance.md) · [Deutsch](../de/security-acceptance.md) · [Français](security-acceptance.md) · [Español](../es/security-acceptance.md) · [Português (Brasil)](../pt-BR/security-acceptance.md) · [Русский](../ru/security-acceptance.md)

[Accueil Git Guard](../../README.fr.md) · [Démarrage rapide](README.md)

Version de base 0.1 — 2026-10-28.

Cette spécification est commune au manuel humain et aux futures compétences. C’est un plan de test, pas le compte rendu d’une installation validée. Le guide OneDev détaillé et le guide GitHub abrégé doivent s’y référer sans définir de critères contradictoires.

<a id="inspect-first"></a>

## Inspecter d’abord

Relevez plateforme/version, visibilité du dépôt, branches protégées, identités, rôles, droits des jetons/applications, règles héritées, ordre et application des règles, et exceptions de contournement. Examinez les voies pertinentes Git/SSH/HTTPS, Web, API, CI/intégration, proxy et hôte/stockage. Vérifiez si l’IA peut également utiliser une session Web ou des identifiants humains existants.

En auto-hébergement, examinez l’accès à l’hôte, aux conteneurs, aux dossiers de données et aux ports alternatifs. Un serveur/NAS indépendant n’offre une frontière utile que si l’IA ne peut pas l’administrer. Un proxy inverse contrôle les requêtes qui le traversent ; il ne protège ni une autre voie exposée ni le stockage sous-jacent. Les plateformes hébergées exigent leurs propres contrôles de comptes/applications ; on ne peut pas y transposer implicitement un proxy auto-hébergé.

<a id="test-only-in-the-authorized-environment"></a>

## Tester uniquement dans l’environnement autorisé

Utilisez un dépôt ou une instance jetable, autorisé séparément, avec des règles représentatives et des identités distinctes. Confirmez la récupération possible des données de test et les opérations censées être permises. Réalisez les tests négatifs uniquement sur ces objets jetables, avec du contenu inoffensif, et conservez les preuves. Ce document n’autorise ni suppression de dépôts de production, ni réécriture d’historique réel, ni changement des rôles en service.

<a id="acceptance-matrix"></a>

## Matrice de vérification

| Capacité ou voie | Résultat attendu pour l’identité IA restreinte | Preuve requise |
| --- | --- | --- |
| Lire et préparer une branche de travail autorisée | Permis dans le périmètre | Un contrôle positif atteint le service prévu avec l’identité prévue |
| Pousser directement des commits ordinaires sur main protégée | Refus selon la politique choisie | Refus réel et référence protégée inchangée |
| Réécrire l’historique protégé par push forcé | Refus | Refus de permission et historique inchangé |
| Supprimer une branche/référence protégée | Refus | Refus réel et référence toujours présente |
| Supprimer le dépôt/projet | Refus | Projet jetable toujours présent ; absence de capacité effective de suppression |
| Approuver au nom de la personne requise | Refus | Identités de revue et relevé d’autorisation |
| Effectuer la fusion finale, y compris après approbation | Refus selon la politique de fusion exclusivement humaine | Résultat réel de permission ; une PR non approuvée ne suffit pas comme test |
| Activer/utiliser la fusion automatique ou une intégration équivalente | Refus pour l’IA dans ce processus | Voie API/Web/application et acteur réel enregistrés |
| Modifier rôles, protections, exceptions ou contrôles de sécurité | Refus | Configuration avant/après et refus |
| Utiliser d’autres identifiants, sessions, points d’accès ou voies CI | Aucune autorité involontaire | Inventaire et test limité de chaque voie pertinente ; voies inconnues non vérifiées |
| Modifier hôte, conteneur ou stockage du dépôt | Aucun accès administratif ou destructeur | Preuves des limites du système/stockage, pas seulement une case de l’application |
| Supprimer/écraser tous les points de récupération | Refus pour l’identité de développement | Conservation indépendante et séparation de l’administration des sauvegardes |
| La personne examine et effectue la fusion prévue | Permis selon la politique de revue | Contrôle positif avec l’identité réelle de la personne |

Examinez création de branches/tags, suppression de tags et exceptions propres aux branches lorsqu’elles affectent la politique. Ne bloquez pas par erreur toute préparation en prétendant avoir réussi la séparation des responsabilités.

<a id="record-each-result"></a>

## Consigner chaque résultat

Pour chaque ligne, conservez : identité de test ; version logicielle et configuration ; source/cible ; opération et voie ; résultat attendu ; résultat réel et motif ; état des objets avant/après ; heure ; emplacement des preuves. Masquez identifiants et données privées étrangères au test avant tout partage.

Utilisez **réussi**, **échoué** ou **non vérifié**, avec une explication. Délai dépassé, échec de connexion, conflit, requête invalide, marqueur WIP, serveur indisponible, capture d’écran ou option activée ne prouvent pas que la permission prévue a refusé l’action. Un contrôle positif aide à distinguer l’application d’une restriction d’un test mal configuré.

Si une frontière requise échoue ou reste non vérifiée, signalez explicitement cette lacune. Précisez les opérations réellement bloquées sans prétendre éliminer toutes les erreurs possibles de l’IA. Retestez les voies affectées après un changement de rôle, proxy, règle, version ou intégration ; conservez les preuves antérieures avec leur périmètre initial.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
