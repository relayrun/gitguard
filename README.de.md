# Git Guard: Git-Zusammenarbeit mit KI und menschlicher Prüfung

[Offizielle Website](https://www.relayrun.net/) · [Schnellstart](docs/de/README.md) · [KI-Skills](skills/README.md)

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Русский](README.ru.md)

## 1. Git Guard in 40 Sekunden

https://github.com/user-attachments/assets/ecab6d6e-2d90-43f7-880c-8a343a9ac9f1

[Deutsches Video herunterladen · MP4 · 40 s](https://raw.githubusercontent.com/relayrun/gitguard/main/assets/videos/RelayRun-GitGuard-Intro-de-v12.mp4)

## 2. Die KI bereitet vor. Menschen entscheiden.

**Effizient mit KI arbeiten und die Sicherheit des Repositorys in menschlicher Hand behalten.**

**Git Guard ist ein Open-Source-Projekt von [RelayRun](https://www.relayrun.net/) für die Zusammenarbeit mit Git.** Es bietet Einrichtungshandbücher für Menschen, Skills für KI, Vorlagen und Bereitstellungsbeispiele. Einzelpersonen und Teams können damit riskante KI-Aktionen begrenzen und die abschließende Prüfung und den Merge Menschen vorbehalten.

> [!NOTE]
> **Ein Mensch beauftragt → die KI arbeitet im erlaubten Umfang → ein Mensch prüft das Ergebnis.**

Die Zielgruppe sind Einzelpersonen und Teams, die Code oder Dokumentation in Git-Repositories mit KI bearbeiten. **OneDev und GitHub sind Konfigurationsbeispiele, keine Beschränkung auf diese Plattformen.** Andere Git-Verwaltungsplattformen können dieselben Prinzipien nutzen; Einstellungen und Wirkung sind anhand der jeweiligen Funktionen zu prüfen.

## 3. Warum Git Guard?

KI kann Code schnell ändern, aber auch schnell Schaden verursachen: Historie per Force-Push überschreiben, Branches löschen oder main ohne Prüfung ändern. Mit Administratorrechten könnte sie sogar die Schutzregeln selbst verändern.

Ein Prompt mit „Tu das nicht“ genügt nicht. Git Guard verankert die Kontrolle in **Serverrechten, Zugangswegen und unabhängigen Backups**. Die KI erledigt autorisierte Aufgaben; Menschen behalten wichtige Entscheidungen und Wiederherstellungszugänge.

## 4. Wie wird das Repository geschützt?

| Maßnahme | Angestrebte Wirkung |
| --- | --- |
| Hauptbranch schützen | Die KI darf autorisierte Arbeitsbranches pushen, aber nicht direkt nach main pushen, dessen Historie überschreiben oder geschützte Branches löschen. |
| Mensch erstellt, prüft und mergt im Web | Die KI bereitet Branch, Titel und Beschreibung vor. Ein Mensch erstellt den Antrag in OneDev/GitHub, prüft Änderungen und führt den Merge aus. |
| Umgehungswege begrenzen | Das selbst gehostete OneDev-Beispiel sperrt REST-API-Zugriffe am Reverse Proxy und schließt direkte Backend- sowie andere Umgehungszugänge. |
| Mitarbeit und Administration trennen | Die tägliche KI-Identität erhält keine Rechte zum finalen Merge, zur Änderung von Schutzregeln oder zur Backup-Verwaltung und nutzt keine menschliche Administratorsitzung. |
| Unabhängige Wiederherstellung | Backups auf einem separaten Gerät oder NAS, geschützte historische Wiederherstellungspunkte und Integritätsprüfungen. Builds und Starttests bleiben je nach Projekt optional. |

> [!WARNING]
> **Wichtige Berechtigungsgrenzen:** Direkte und erzwungene Pushes der KI nach main sowie eigenständige Merges beschränken; REST- und andere Wege zur Umgehung der Prüfung schließen. Abschließende Prüfung und Merge bleiben beim Menschen.

Dies sind Konfigurations- und Abnahmeziele, kein Nachweis bereits wirksamer Schutzmaßnahmen. Siehe [OneDev-Version und Grenzen](docs/de/onedev.md#sources-and-limits) und die plattformspezifischen Regeln im [GitHub-Leitfaden](docs/de/github.md).

## 5. KI kann bei der Einrichtung helfen

Sie können das Handbuch selbst umsetzen oder Handbuch und Skill an einen KI-Assistenten übergeben. **Sichtbare Computer-Use-Bedienung ist die bevorzugte Unterstützung:** Beobachten Sie die Aktionen, erteilen Sie gezielte Rechte und geben Sie vertrauliche Zugangsdaten selbst ein. Melden Sie die vorübergehende Administratorsitzung danach ab; die KI kehrt zu ihrer eingeschränkten Alltagsidentität zurück.

| Umgebung | Einstieg |
| --- | --- |
| Selbst gehostetes OneDev | [Handbuch](docs/de/onedev.md) · [Einrichtungs- und Abnahme-Skill (Englisch)](skills/gitguard-onedev-safety/SKILL.md) |
| GitHub | [GitHub-Leitfaden](docs/de/github.md) |
| Andere Git-Plattformen | [Gemeinsamen Ablauf](docs/de/workflow.md) und [Abnahmematrix](docs/de/security-acceptance.md) auf deren Funktionen übertragen. |

Die Ersteinrichtung umfasst vier Teile: Repository, Hauptbranch und getrennte Identitäten bestimmen; Schutz konfigurieren; erlaubte und verbotene Aktionen im autorisierten isolierten Testrepository überprüfen; [unabhängige Wiederherstellung einrichten](docs/de/backup-and-recovery.md). Nicht jede Änderung verlangt eine neue Einrichtung. Bei geänderten Rechten, Regeln oder Umgebungen prüfen Sie die betroffenen Teile erneut.

### Vertrauliche Inhalte vor dem Commit prüfen

Lassen Sie die KI dem [Leitfaden zur Inhaltsprüfung](docs/de/public-content-review.md) folgen: Veröffentlichungsumfang und Prüfmodus festlegen, dann Arbeitsdateien, vorgemerkte Bytes und ausgehende Historie getrennt prüfen. Der Helfer meldet mögliche Schlüssel, Rechnerpfade, private Netzwerkadressen und ähnliche Probleme. Bearbeiten und prüfen Sie Funde vor einem autorisierten Commit oder Push erneut. Er löscht oder ersetzt keine Inhalte und erkennt nicht alle privaten Informationen; Bilder und Videos benötigen menschliche Prüfung. Organisationsspezifische Geheimnis-/Kontovergleichslisten bleiben in privater Konfiguration außerhalb der Repositorys. Der [Workflow-Skill (Englisch)](skills/gitguard-workflow/SKILL.md) enthält die zugehörigen Arbeitsanforderungen.

## 6. Vier Schritte im Alltag

Verwenden Sie den [Workflow-Skill (Englisch)](skills/gitguard-workflow/SKILL.md) und den Git-Ablauf Ihres Projekts.

| Schritt | Was Sie sagen oder tun | Was die KI ausführt |
| --- | --- | --- |
| 1. Lokaler Commit | „Führe Schritt 1 nach Git.md aus.“ | Liest den Ablauf, prüft die Änderung und committet lokal. Noch kein Upload. |
| 2. Push und Vorbereitung | „Führe Schritt 2 nach Git.md aus.“ | Pusht den autorisierten Arbeitsbranch und bereitet Titel, Beschreibung und Prüfergebnisse vor. |
| 3. Menschliche Prüfung und Merge | Antrag im Web erstellen; Quell- und Zielbranch, Titel, Beschreibung, Änderungen und Prüfungen kontrollieren; danach mergen. | Erklärt und unterstützt. Den abschließenden Merge führt ein Mensch aus. |
| 4. Nachbereitung | „Ich habe gemergt. Prüfe das Ergebnis und räume danach auf.“ | Prüft den tatsächlich integrierten Inhalt, synchronisiert main sicher und entfernt nur bestätigt abgeschlossene Branches. |

`Git.md` steht für das tatsächliche Ablaufdokument Ihres Projekts. Sie entscheiden, wann committet, gepusht und gemergt wird. [Vollständiger Ablauf](docs/de/workflow.md)

## 7. Was Sie erhalten

- [Deutscher Schnellstart und alle sieben Handbuchkapitel](docs/de/README.md) · [Abdeckung der acht Sprachen](docs/README.md).
- [Zwei KI-Skills](skills/README.md): Alltag/Nachbereitung und OneDev-Einrichtung/Abnahme.
- [Vorlagen](templates/README.md) für Übergaben, Beschreibungen und Abnahmeprotokolle.
- [Bereitstellungsbeispiele](examples/onedev/README.md) sowie [Prüf- und Paketierungswerkzeuge](scripts/README.md).
- [Video- und Sprachintegration](docs/de/animation-and-language.md).

Skills, Vorlagen, Bereitstellungsbeispiele und Prüfwerkzeuge bleiben gemeinsame englische Ressourcen.

## 8. Häufige Fragen und Grenzen

### Muss die Einrichtung bei jeder Änderung wiederholt werden?

Nein. Nutzen Sie die vier Alltagsschritte und überprüfen Sie betroffene Einstellungen bei Änderungen an Identitäten, Rechten oder Umgebung.

### Kann ich Git Guard allein verwenden?

Ja, mit getrennter menschlicher und KI-Rolle sowie getrennten Einrichtungs- und Alltagssitzungen. Verlangt die Plattform eine weitere prüfende Person, bleibt diese Vorgabe bestehen.

### Schützt ein installierter Skill automatisch das Repository?

Nein. Skills beschreiben das Verhalten der KI. Wirksame Grenzen brauchen Serverkonfiguration und [Berechtigungsprüfungen](docs/de/security-acceptance.md).

### Welche Sprachen sind verfügbar?

Einführungen, Schnellstarts, alle sieben ausführlichen Handbuchkapitel und passende Videos gibt es in allen acht Sprachen. Siehe [Abdeckung](docs/README.md). Übersetzungen sind Prüfentwürfe; ein muttersprachliches Lektorat wird nicht behauptet.

Passen Sie Handbücher, Skills und Beispiele an Ihre Umgebung an. Erfolgreiche Dokumentprüfungen sind keine Live-Sicherheitsabnahme; ein lokaler Stand ist keine veröffentlichte Version. [Tonquellen](assets/videos/README.md) · [Prüfung öffentlicher Inhalte](docs/de/public-content-review.md) · [Repository](https://github.com/relayrun/gitguard)

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
