# Git Guard — Schnellstart

[English](../en/README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [Deutsch](README.md) · [Français](../fr/README.md) · [Español](../es/README.md) · [Português (Brasil)](../pt-BR/README.md) · [Русский](../ru/README.md)

[Git-Guard-Startseite](../../README.de.md)

Einführung, Schnellstart, alle sieben ausführlichen Handbuchkapitel und Video sind auf Deutsch verfügbar. OneDev und GitHub sind Beispiele; die Prinzipien lassen sich auf andere Git-Plattformen übertragen. Dies ist ein Übersetzungsentwurf, keine Live-Sicherheitsabnahme.

Folgen Sie vor einem autorisierten Commit oder Upload dem Inhaltsleitfaden: [Prüfung konfigurieren und ausführen](public-content-review.md#configure-the-public-content-check), danach [Ergebnisse verstehen und Funde behandeln](public-content-review.md#interpret-results-and-handle-findings).

## KI kann bei der Einrichtung helfen

Sie können das Handbuch selbst umsetzen oder Handbuch und Skill an einen KI-Assistenten übergeben. **Sichtbare Computer-Use-Bedienung ist die bevorzugte Unterstützung:** Beobachten Sie die Aktionen, erteilen Sie gezielte Rechte und geben Sie vertrauliche Zugangsdaten selbst ein. Melden Sie die vorübergehende Administratorsitzung danach ab; die KI kehrt zu ihrer eingeschränkten Alltagsidentität zurück.

| Umgebung | Einstieg |
| --- | --- |
| Selbst gehostetes OneDev | [Handbuch](onedev.md) · [Einrichtungs- und Abnahme-Skill (Englisch)](../../skills/gitguard-onedev-safety/SKILL.md) |
| GitHub | [GitHub-Leitfaden](github.md) |
| Andere Git-Plattformen | [Gemeinsamen Ablauf](workflow.md) und [Abnahmematrix](security-acceptance.md) auf deren Funktionen übertragen. |

Die Ersteinrichtung umfasst vier Teile: Repository, Hauptbranch und getrennte Identitäten bestimmen; Schutz konfigurieren; erlaubte und verbotene Aktionen im autorisierten isolierten Testrepository überprüfen; [unabhängige Wiederherstellung einrichten](backup-and-recovery.md). Nicht jede Änderung verlangt eine neue Einrichtung. Bei geänderten Rechten, Regeln oder Umgebungen prüfen Sie die betroffenen Teile erneut.

## Vier Schritte im Alltag

Verwenden Sie den [Workflow-Skill (Englisch)](../../skills/gitguard-workflow/SKILL.md) und den Git-Ablauf Ihres Projekts.

| Schritt | Was Sie sagen oder tun | Was die KI ausführt |
| --- | --- | --- |
| 1. Lokaler Commit | „Führe Schritt 1 nach Git.md aus.“ | Liest den Ablauf, prüft die Änderung und committet lokal. Noch kein Upload. |
| 2. Push und Vorbereitung | „Führe Schritt 2 nach Git.md aus.“ | Pusht den autorisierten Arbeitsbranch und bereitet Titel, Beschreibung und Prüfergebnisse vor. |
| 3. Menschliche Prüfung und Merge | Antrag im Web erstellen; Quell- und Zielbranch, Titel, Beschreibung, Änderungen und Prüfungen kontrollieren; danach mergen. | Erklärt und unterstützt. Den abschließenden Merge führt ein Mensch aus. |
| 4. Nachbereitung | „Ich habe gemergt. Prüfe das Ergebnis und räume danach auf.“ | Prüft den tatsächlich integrierten Inhalt, synchronisiert main sicher und entfernt nur bestätigt abgeschlossene Branches. |

`Git.md` steht für das tatsächliche Ablaufdokument Ihres Projekts. Sie entscheiden, wann committet, gepusht und gemergt wird. [Vollständiger Ablauf](workflow.md)

## Schutz und Wiederherstellung

Vorhandene Einstellungen beweisen keine wirksame Sperre. Ablehnungstests benötigen eine eigene Freigabe und ein entbehrliches Testrepository; ungeprüfte Zugangswege bleiben als ungeprüft markiert. Verwenden Sie unabhängige Synchronisierung und geschützte historische Wiederherstellungspunkte. Ein sauberer Build und Programmstart sind je nach Projekt optionale Prüfungen.

Im OneDev-Beispiel kann eine bestätigte Autorenadresse den vorgeschlagenen Quellbranch beeinflussen; sie löst keinen Merge aus. WIP-Präfixe im Titel können den Merge in der Referenzversion blockieren. Das ist kein allgemeines Verbot von Titeln mit Buchstaben am Anfang.

## Ausführliche Anleitungen

- [Täglicher Arbeitsablauf](workflow.md)
- [OneDev einrichten](onedev.md)
- [GitHub-Zuordnung](github.md)
- [Sicherheitsabnahme](security-acceptance.md)
- [Backup und Wiederherstellung](backup-and-recovery.md)
- [Öffentliche Inhalte prüfen](public-content-review.md)
- [Animation und Sprachen](animation-and-language.md)
- [Skills](../../skills/README.md) · [Templates](../../templates/README.md)

Skills, Vorlagen, Bereitstellungsbeispiele und Prüfwerkzeuge bleiben gemeinsame englische Ressourcen.

Die KI bereitet Änderungen vor. Ein Mensch prüft sie und führt den endgültigen Merge aus.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
