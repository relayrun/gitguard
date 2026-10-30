# OneDev einrichten: KI-Rechte und menschliche Prüfung

[English](../en/onedev.md) · [简体中文](../zh-CN/onedev.md) · [日本語](../ja/onedev.md) · [Deutsch](onedev.md) · [Français](../fr/onedev.md) · [Español](../es/onedev.md) · [Português (Brasil)](../pt-BR/onedev.md) · [Русский](../ru/onedev.md)

[Git-Guard-Startseite](../../README.de.md) · [Schnellstart](README.md)

Dieser Leitfaden zu **RelayRun Git Guard** erklärt, wie Sie bei selbst betriebenem OneDev menschliche und KI-Rechte trennen, main schützen, Wege zur Umgehung der Prüfung begrenzen und unabhängige wiederherstellbare Kopien erhalten. Die KI committet und pusht Arbeitsbranches im autorisierten Rahmen; ein Mensch erstellt den Antrag, prüft ihn und führt den endgültigen Merge im Web aus.

**Git Guard richtet sich an Einzelpersonen und Teams mit Git-Repositorys, nicht nur an OneDev-Nutzer.** OneDev und GitHub sind Konfigurationsbeispiele. Andere Git-Verwaltungsplattformen können den [gemeinsamen Regeln für Zusammenarbeit und Schutz](workflow.md) folgen; Einstellungen und Ergebnisse sind anhand ihrer Fähigkeiten zu überprüfen. Dieses Kapitel zeigt OneDev; der [GitHub-Leitfaden](github.md) bietet ein weiteres Beispiel. OneDev ist eine Plattform eines Drittanbieters und kein RelayRun-Produkt.

Prüfentwurf 0.1. Referenz für Oberfläche und Fehlerbehebung: **OneDev 14.1.0**. Dies ist ein versionsgebundenes Beispiel, keine Empfehlung, eine alte Version ohne Prüfung des aktuellen Supports einzusetzen. [Arbeitsablauf](workflow.md) · [Sicherheitsabnahme](security-acceptance.md) · [GitHub-Alternative](github.md)

**Auf dieser Seite:** [KI-gestützte Einrichtung](#visible-ai-assisted-setup) · [Bereitstellung](#1-select-a-deployment-boundary) · [Identitäten](#2-establish-separate-identities) · [Branch-Schutz](#3-initialize-and-protect-the-target-branch) · [Menschlicher Merge](#4-set-pr-defaults-without-confusing-responsibilities) · [REST-Zugang](#5-optional-rest-ingress-restriction) · [Häufige Stolperfallen](#6-two-common-pitfalls) · [Abnahme und Wiederherstellung](#7-acceptance-and-recovery) · [Quellen](#sources-and-limits)

Folgen Sie vor einem autorisierten Commit oder Upload dem Inhaltsleitfaden: [Prüfung konfigurieren und ausführen](public-content-review.md#configure-the-public-content-check), danach [Ergebnisse verstehen und Funde behandeln](public-content-review.md#interpret-results-and-handle-findings).

<a id="visible-ai-assisted-setup"></a>

## Sichtbare KI-Unterstützung bei der Einrichtung

Sie können die Plattform manuell konfigurieren oder eine KI anweisen, diesem Leitfaden und dem Einrichtungsskill über eine sichtbare Computer-Use-Oberfläche zu folgen. Bestimmen Sie zuerst Projekt, handelnde Identität, zu ändernde Einstellungen und Rücknahmeverfahren. Ein Mensch genehmigt diesen Umfang und kann die Aktionen beobachten; daraus entsteht keine versteckte oder dauerhafte Administratorfreigabe.

Verwenden Sie für Verwaltungsfunktionen eine beaufsichtigte, temporäre Einrichtungssitzung, die für diese Änderungen bestimmt ist. Der Mensch gibt sensible Zugangsdaten ein, ohne sie in Chat, Screenshots oder Repository-Dateien abzulegen. Verwenden Sie keine Administratorsitzung, um eine verweigerte Alltagsaktion zu umgehen. Lesen Sie nach der Einrichtung die Einstellungen zurück, führen Sie die angemessen begrenzte Abnahme durch, beenden Sie die Sitzung mit erhöhten Rechten und kehren Sie zur eingeschränkten Alltagsidentität zurück. Kann die verfügbare Oberfläche einen erforderlichen Schritt nicht ausführen, melden Sie dies und überlassen Sie ihn dem Menschen; behaupten Sie keinen nicht erfolgten Klick.

Die sichtbare Bedienung macht die Konfiguration verständlich; erzwungene Rechte und ihre Tests liefern den Schutz.

<a id="1-select-a-deployment-boundary"></a>

## 1. Eine Grenze für die Bereitstellung wählen

Bevorzugen Sie einen unabhängigen Rechner, Server oder NAS, dessen Architektur und Containerunterstützung zur ausgewählten OneDev-Version passen. Halten Sie Server, Containerlaufzeit, Speicher, Backups und Administratorzugangsdaten außerhalb der Reichweite der KI-Entwicklungsidentität. Auf demselben Host sind ausdrückliche Betriebssystem- und Dateirechte nötig; Docker allein schafft diese Trennung nicht.

Nutzen Sie die offizielle Installationsanleitung und das [parametrisierte Beispiel](../../examples/onedev/README.md). Wählen Sie unterstützte Image-Versionen/Digests, einen unabhängigen Datenort, TLS-Zugang und Wiederherstellungsverfahren vor dem Start. Das Beispiel veröffentlicht nur ein Loopback-Gateway, verzichtet auf den Docker-Socket und deaktiviert direkte HTTP-/SSH-Hostzuordnungen. Es ist eine Ausgangskonfiguration, keine getestete Produktionsinstallation. Containerbasierte Builds können einen gesondert entworfenen Executor benötigen.

<a id="2-establish-separate-identities"></a>

## 2. Getrennte Identitäten einrichten

| Prüfbereich | Maßnahme | Überprüfung |
| --- | --- | --- |
| Administration → Users / Groups | Menschliche Prüfer/Administratoren, KI-Beitragende und schreibgeschützte Backup-Identität trennen | Tatsächliche Mitgliedschaften und Zugangsdaten einschließlich geerbter Zugriffe |
| Administration → Roles | Code-, Projektverwaltungs- und weitere Rechte der ausgewählten Rolle prüfen | Der Rollenname allein reicht nicht; die KI darf keine Projekte besitzen/verwalten oder Schutzregeln ändern |
| Project → Settings → Authorizations → Users / Groups | Nur notwendigen Projektumfang freigeben; Elternprojekte prüfen | Die Backup-Identität liest nur das vorgesehene Repository; KI-Rechte entsprechen dem erklärten Modell |
| Project → Settings → General | Elternprojekt und effektive Standardrolle prüfen | Keine unbeabsichtigten anonymen/Standardzugriffe oder geerbten Projekteigentümerrechte |

Der deaktivierte Schalter „Manage Pull Requests“ der Referenzrolle Code Writer betrifft Verwaltung/Sammelaktionen; er beweist nicht, dass ein Code Writer niemals den endgültigen Merge ausführen kann. Prüfen Sie die Merge-Berechtigung gesondert nach gültiger menschlicher Freigabe. Geben Sie der täglichen KI-Identität keine menschliche Browsersitzung oder Administratortokens. Die oben beschriebene beaufsichtigte Einrichtungssitzung ist vorübergehend und darf nicht für alltägliche Git-Arbeit bestehen bleiben.

<a id="3-initialize-and-protect-the-target-branch"></a>

## 3. Zielbranch initialisieren und schützen

Initialisieren Sie den vorgesehenen geschützten Branch im menschlich kontrollierten Einrichtungsablauf, bevor Sie eine Regel aktivieren, die seine Erstellung verhindert. Schalten Sie den Schutz nicht routinemäßig aus, damit die KI den Branch anlegen oder reparieren kann.

Öffnen Sie **Project → Settings → Code → Branch Protection**. Wählen Sie in der Referenzoberfläche den geschützten Branch, häufig `main`, und die betroffenen Identitäten; die Referenz verwendet `anyone`. Prüfen Sie die Regelreihenfolge: In dieser Version kommen lokale Regeln vor Elternregeln, und die erste passende Regel gilt. Eine untergeordnete Regel kann eine strengere übergeordnete verdecken; prüfen Sie das effektive Verhalten.

| Option | Erforderliche Überlegung |
| --- | --- |
| Prevent forced push | Für den geschützten Branch aktivieren; in einem Wegwerf-Testrepository prüfen, dass eine tatsächlich unzulässige Umschreibung abgelehnt wird |
| Prevent deletion | Branch schützen; das Löschen des Repositorys ist eine andere Berechtigung |
| Prevent creation | Nach der Initialisierung entscheiden; ersetzt keinen Schutz für Aktualisierungen/Prüfungen |
| Required reviewers | Unabhängigen menschlichen Prüfer über die Oberflächenauswahl bestimmen; resultierenden Ausdruck und Konto prüfen |
| Required builds / signatures | Nach Projektbedarf wählen, mit tatsächlich laufenden Prüfungen und vertrauenswürdigen Signaturschlüsseln |
| File/tag protection | Nur erforderlichen Umfang definieren; Branch-Regeln beweisen nicht automatisch Tag- oder Release-Schutz |

Die frühere Referenz hatte zunächst keinen vorgeschriebenen Prüfer; später wurden Prüfanforderungen ergänzt. Das Verhindern von Force-push blockiert **keinen** gewöhnlichen direkten Fast-forward-Push. Testen Sie direkte normale Pushes ausdrücklich. Ein benannter Prüfer, der zugleich den PR eingereicht hat, kann in der Referenz anders behandelt werden; getrennte menschliche und KI-Identitäten sind daher wesentlich. Behaupten Sie keinen ausschließlich menschlichen Merge, bevor diese Fähigkeit gesondert getestet wurde.

Speichern Sie gezielte Konfigurationsänderungen nur im autorisierten Rahmen. Lesen Sie Werte und zugeordnete Identitäten zurück; Screenshots zeigen Einstellungen, keine Durchsetzung.

<a id="4-set-pr-defaults-without-confusing-responsibilities"></a>

## 4. PR-Standardwerte ohne Verwechslung der Zuständigkeiten

Öffnen Sie **Project → Settings → Pull Requests**. Prüfen Sie für jedes Feld, ob es lokal oder geerbt ist.

- **Default merge strategy:** Die Referenz nutzt Squash. Ein Standardwert verbietet andere Strategien nicht.
- **Default assignee:** Zuständigkeit für die Arbeit, nicht der vorgeschriebene Prüfer.
- **Delete source branch after merge:** Optionale Bereinigung, die ebenfalls von der Berechtigung des Akteurs abhängt. Daraus folgt nie, dass alle alten Branches gelöscht werden sollen.
- Prüfen Sie vor der Übergabe immer Quelle, Ziel, Diff, Titel und Checks. Der Mensch prüft und führt den endgültigen Merge aus; die KI klickt weder Merge noch aktiviert sie Auto-merge.

Prüfen Sie nach einem Squash die integrierte Änderung relativ zur tatsächlichen Zielhistorie. Unterschiedliche Commit-IDs bedeuten allein keinen Inhaltsverlust. Folgen Sie dem gemeinsamen Ablauf für sichere Synchronisierung und begrenzte Bereinigung.

<a id="daily-human-request-creation"></a>

### Tägliche Antragserstellung durch den Menschen

Nachdem die KI den autorisierten Branch gepusht und Titel/Beschreibung vorgeschlagen hat, öffnet der Mensch die Pull-Request-Seite des Repositorys, erstellt einen neuen Antrag, prüft Quelle und Ziel, trägt den Text ein und sendet ihn ab. Lesen Sie Diff und tatsächliche Check-/Prüfergebnisse, bevor Sie persönlich den Merge bestätigen. Siehe [vollständige Übergabe](workflow.md). Ist der Ersteller zugleich vorgeschriebener Prüfer, prüfen Sie die Freigaberegeln Ihrer Version; ziehen Sie gegebenenfalls einen weiteren autorisierten Menschen hinzu, statt den Schutz zu schwächen.

<a id="5-optional-rest-ingress-restriction"></a>

## 5. Optionale Beschränkung des REST-Zugangs

Bei eigener Bereitstellung kann das Gateway den REST-Namensraum sperren und notwendige Web-/Git-Pfade zulassen. Das [Gateway-Beispiel](../../examples/onedev/README.md) beschreibt dieses Modell. Integrationen können dadurch ausfallen; wählen Sie es nur, wenn es zum Dienst passt.

Prüfen Sie alle Wege: direkten Backend-Port, SSH, alternative Hostnamen, IPv6, Tunnel, angemeldete Browsersitzungen, Serveraufgaben und Container-/Hostverwaltung. Ein gesperrter Proxy-Endpunkt beweist nicht, dass andere Wege gesperrt sind. Beziehen Sie normalisierte Pfade, Groß-/Kleinschreibung, Kodierungsvarianten, echte Git-Operationen und nötige WebSockets in die Abnahme ein. Netzwerkfehler belegen keine Berechtigungsverweigerung.

<a id="6-two-common-pitfalls"></a>

## 6. Zwei häufige Stolperfallen

<a id="pr-source-branch-is-not-suggested"></a>

### Der PR-Quellbranch wird nicht vorgeschlagen

In der Referenz 14.1.0 berücksichtigen Quellbranch-Vorschläge die E-Mail-Adresse des letzten Commit-Autors und die bestätigten E-Mail-Adressen des angemeldeten Nutzers. Prüfen Sie letzten Commit-Autor und vorgesehenen Nutzer. Fügen Sie über dessen Email Addresses nur eine von ihm kontrollierte Adresse hinzu und schließen Sie die normale Bestätigung ab. Administratorverhalten bedeutet nicht, dass gewöhnliche Nutzer diese Bestätigung überspringen können.

Öffnen Sie die PR-Erstellung erneut und prüfen Sie Quelle und Ziel. Manuelle Branchauswahl ist ebenfalls zulässig. Dies repariert einen Vorschlag, führt aber weder automatisch einen Merge aus noch erteilt es Freigabe. Ändern Sie nicht die globale Git-Identität und schreiben Sie keine Historie um, nur um den Vorschlag sichtbar zu machen. Eine ausdrücklich gewählte Quelle hat Vorrang.

<a id="a-ready-pr-remains-marked-work-in-progress"></a>

### Ein fertiger PR bleibt als laufende Arbeit markiert

Die Referenz behandelt Titel, die mit `wip` oder `[wip]` beginnen, unabhängig von Groß-/Kleinschreibung als laufende Arbeit und blockiert den Merge. Dies ist **kein** Verbot von Titeln, die mit irgendeinem englischen Buchstaben beginnen. Betroffen ist der PR-Titel, der aus Commit-Nachricht oder Branch abgeleitet sein kann.

Entfernen Sie die Markierung erst, wenn die Arbeit tatsächlich bereit ist. Vorgeschriebene Prüfungen, Checks und menschlicher endgültiger Merge gelten weiterhin; eine WIP-Sperre beweist keine Merge-Berechtigungsgrenze. Prüfen Sie die Regel in Ihrer eingesetzten Version.

<a id="7-acceptance-and-recovery"></a>

## 7. Abnahme und Wiederherstellung

Nutzen Sie die [gemeinsame Matrix](security-acceptance.md) und [Nachweisvorlage](../../templates/security-acceptance.csv). Beginnen Sie mit einer lesenden Bestandsaufnahme; holen Sie vor Verweigerungstests im Wegwerf-Repository die passende Autorisierung ein. Erfassen Sie Akteur, Version, Wege, Kontrolle, Vorher-/Nachher-Zustand und tatsächlichen Ablehnungsgrund. Ein unerklärter Fehler oder fehlender Test ist „nicht verifiziert“.

Erhalten Sie nach dem [Backup-Leitfaden](backup-and-recovery.md) unabhängige wiederherstellbare Versionen der Repositorys **und** der Dienstdaten/-konfiguration. Ein laufend aktualisierter Klon ist kein vollständiges OneDev-Backup. Kompilierung und Anwendungsstart sind optional und können nicht alle Serverdatenbanken oder Anlagen prüfen.

<a id="sources-and-limits"></a>

## Quellen und Grenzen

- [Offizielle Containerinstallation](https://docs.onedev.io/installation-guide/run-as-docker-container) und [Reverse-Proxy-Einrichtung](https://docs.onedev.io/administration-guide/reverse-proxy-setup).
- [Versionsgebundene Quellbranchauswahl](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/web/page/project/pullrequests/create/NewPullRequestPage.java).
- [Versionsgebundene WIP- und Merge-Bedingungen](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/model/PullRequest.java).
- [Versionsgebundener Branch-Schutz](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/model/support/code/BranchProtection.java) und [Push-Prüfungen](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/git/hook/GitPreReceiveCallback.java).

Die Anleitung verbindet versionsbezogene UI-Beobachtungen und Quellcodeprüfung. Ihre Erstellung installiert OneDev nicht und zertifiziert keinen anderen Server, keine Rolle, kein NAS-Modell, keinen Proxy und keine andere Version.

**Weiter:** Prüfen Sie konfigurierte Rechte mit der [Abnahmematrix](security-acceptance.md), folgen Sie dann dem [Vier-Schritte-Ablauf samt Bereinigung](workflow.md). Die [Git-Guard-Übersicht](../../README.de.md) erläutert das Produkt.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
