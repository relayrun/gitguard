# Revue du contenu public

[English](../en/public-content-review.md) · [简体中文](../zh-CN/public-content-review.md) · [日本語](../ja/public-content-review.md) · [Deutsch](../de/public-content-review.md) · [Français](public-content-review.md) · [Español](../es/public-content-review.md) · [Português (Brasil)](../pt-BR/public-content-review.md) · [Русский](../ru/public-content-review.md)

[Accueil Git Guard](../../README.fr.md) · [Démarrage rapide](README.md)

Projet de revue 0.1. Procédure réutilisable pour les projets publiant du contenu. [Processus](workflow.md)

<a id="configure-the-public-content-check"></a>

## Configurer le contrôle du contenu public

1. Identifiez précisément le projet et les fichiers destinés au public. Gardez hors de cet arbre les relevés internes, identifiants, configurations privées de scanner et diagnostics. Si le dossier de développement contient des données privées, examinez une copie de publication séparée ; ne supprimez pas les originaux privés simplement pour faire réussir le scan.
2. Repérez le vérificateur dans les sources Git Guard ou dans l’instantané de référence fourni avec la compétence installée. Il exige Python 3.9 ou ultérieur et la bibliothèque standard. Il ne s’installe pas, ne lance pas de service et n’impose aucune permission serveur. Fixez explicitement la cible avec `--root` ; le dossier de la compétence installée n’est pas le projet cible.
3. Pour un projet adoptant la méthode, utilisez `--profile generic`. Réservez `--profile gitguard` aux exclusions supplémentaires propres à la structure publique/privée de ce paquet. Le vérificateur intégré n’a ni liste personnalisée de termes sensibles ni remplacement automatique. Pour les secrets ou identifiants propres à l’organisation, utilisez un scanner distinct adapté, dont la configuration reste privée hors de l’arbre publié ; voir les [listes privées](#sensitive-matching-lists-stay-private).
4. Examinez séparément fichiers de travail, octets indexés et historique sortant. Les chemins ci-dessous sont fictifs. Remplacez la plage d’historique par les commits réellement sortants ; le vérificateur ne fait ni fetch ni push. Sans dépôt Git, commencez par les fichiers de travail, puis examinez index et historique lorsqu’ils existent. Un contrôle des seuls fichiers de travail ne certifie pas les commits ultérieurs.

```sh
python3 -B /path/to/gitguard/scripts/check_public_content.py --root /path/to/public-project --profile generic
python3 -B /path/to/gitguard/scripts/check_public_content.py --root /path/to/public-project --profile generic --staged
python3 -B /path/to/gitguard/scripts/check_public_content.py --root /path/to/public-project --profile generic --history origin/main..HEAD
```

<a id="interpret-results-and-handle-findings"></a>

## Interpréter les résultats et traiter les signalements

Le code de sortie **0** signifie aucun signalement dans les règles implémentées ; **1**, des signalements à examiner ; **2**, un contrôle inachevé. Les rapports indiquent chemins, catégories et numéros de ligne, pas les valeurs secrètes détectées. Le scan des fichiers de travail inclut les fichiers ignorés, sauf les métadonnées Git : ignorer un fichier n’empêche pas sa copie accidentelle dans une publication.

Les règles signalent les signatures de clés privées, certains formats de jetons GitHub, les identifiants dans les URL, les chemins de machines, les adresses réseau privées, certains noms de fichiers privés/d’exécution et les liens Markdown relatifs cassés ou sortant du périmètre. Elles ne détectent pas tous les mots de passe ou identifiants de comptes. Les binaires exigent une revue manuelle ; les fichiers de plus de 2 000 000 octets ne sont pas inspectés ; la limite est de 3 000 fichiers et de 200 commits par plage d’historique. Découpez les périmètres déclarés plus grands pour les examiner ; ne les omettez pas discrètement.

Pour chaque signalement, relevez catégorie, emplacement, décision et résultat du nouveau contrôle sans reproduire les valeurs sensibles. Corrigez la copie publique ou les règles d’inclusion, ou justifiez un résultat bénin/vérifié manuellement ; recontrôlez ensuite les vues de travail, d’index et d’historique concernées. Ne supprimez pas globalement les alertes de binaires ou de taille. Une exposition réelle d’identifiants nécessite leur remplacement et une correction de l’historique autorisée séparément ; cet outil ne répare pas l’historique et ne supprime ni ne remplace le contenu. Un délai dépassé ou un scan incomplet n’est pas une réussite.

Pour ce paquet Git Guard, utilisez d’abord `scripts/prepare_release.py` pour créer une copie publique au périmètre explicite. Les caches de développement restent à leur emplacement initial ; les exclusions sont consignées séparément. L’option `--media-review` lit un relevé privé des PNG/MP4 examinés individuellement avec leurs SHA-256 exacts. Seuls les signalements binaires correspondants sont déclarés examinés et listés à part ; fichiers modifiés, secrets, fichiers illisibles et dépassements de taille restent à traiter. Le code 0 peut inclure ces examens documentés, sans constituer une certification automatique de confidentialité. Voir les [instructions de contrôle et de création de paquets](../../scripts/README.md).

<a id="before-a-local-commit"></a>

## Avant un commit local

Examinez les vrais fichiers modifiés, y compris ceux non suivis. Confirmez propriété et droits de publication. Retirez du contenu public plans privés, chemins d’hôtes/utilisateurs, adresses internes, jetons, clés privées, identifiants, données clients, captures/logs bruts et sources de produits sans rapport. Les exemples emploient noms et valeurs génériques.

Vérifiez liens, texte UTF-8, couverture linguistique réelle, mentions de tiers et exactitude des déclarations d’achèvement. Un site ou déploiement prévu ne doit pas être annoncé comme disponible. Les preuves privées restent hors de l’arbre de publication.

Inspectez séparément les octets indexés, qui peuvent différer des fichiers de travail. Examinez renommages/suppressions, binaires, sous-modules et liens symboliques ; un document apparemment sain ne prouve pas qu’une pièce jointe intégrée l’est. Un commit local n’autorise pas la publication.

<a id="before-a-push"></a>

## Avant un push

Énumérez les commits exacts à envoyer à la destination prévue et examinez chaque instantané pertinent, y compris les fichiers supprimés. Les anciens secrets restent dans l’historique après leur suppression ultérieure. Examinez tags et autres références seulement s’ils font partie du push proposé ; un nouveau dépôt ne doit pas hériter accidentellement d’un historique privé.

Si du contenu sensible a été committé, arrêtez la publication, organisez le remplacement approprié des identifiants et une correction approuvée séparément. Ne forcez pas un push et ne supprimez pas un dépôt en silence pour dissimuler l’historique. Les scanners automatiques apportent des indices, pas la preuve que tout contenu privé a disparu.

<a id="reviewable-release"></a>

## Une publication pouvant être examinée

Consignez destination, visibilité, fichiers modifiés, historique sortant, décision sur droits/licence, validations et limites restantes. Confirmez l’autorisation existante pour cette action précise. Préservez la fusion finale humaine.

Si le dépôt renvoie à un site officiel, vérifiez nom d’hôte, certificat HTTPS, identité visuelle et page réelle. Traduisez uniformément le libellé visible dans tous les README pris en charge, avec la même destination canonique. Vérifiez le champ Website du dépôt lors de la publication autorisée. Le manuel doit rester utile indépendamment du site.

<a id="evidence-levels"></a>

## Niveaux de preuve

Distinguez : inspecté, vérifié statiquement, testé en comportement, déployé, confirmé par l’utilisateur. Une capture de configuration, un code de sortie du scanner ou un transfert réussi n’est pas un certificat de sécurité réelle ou de restauration. Pour les permissions, utilisez la [spécification de vérification](security-acceptance.md).

<a id="sensitive-matching-lists-stay-private"></a>

## Les listes de correspondance sensibles restent privées

Ne publiez que la logique réutilisable et des données de test inventées. Valeurs secrètes réelles, identifiants de comptes et listes de correspondance/remplacement propres au projet restent hors des sources, paquets de compétences, téléchargements, captures et historique Git sortant. Une règle contenant une valeur privée exacte est elle-même sensible ; sa présence dans une configuration de scanner ne la rend pas publiable. Les règles d’ignorance ne remplacent pas l’examen de l’index et de l’historique.

Si vous utilisez un scanner distinct comme Gitleaks avec une configuration privée, fournissez ce fichier depuis un emplacement privé à l’exécution. Ne le copiez pas dans un paquet public, n’affichez pas les valeurs détectées et n’utilisez pas de valeurs réelles dans les arguments de commande ou les données de test. Gardez les diagnostics privés et masquez leur contenu avant partage.

Le vérificateur fourni est un nouvel outil écrit pour Git Guard. Il ne charge pas une liste privée existante et ne reconnaît pas spécifiquement comptes de trading/clients, mots de passe arbitraires ou tous les types de jetons. Ses heuristiques génériques complètent un scanner adapté au projet et la revue humaine ; un résultat propre ne garantit pas l’absence de tous les secrets. Il ne nettoie pas l’historique.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
