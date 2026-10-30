# Unabhängige Sicherung und Wiederherstellung

[English](../en/backup-and-recovery.md) · [简体中文](../zh-CN/backup-and-recovery.md) · [日本語](../ja/backup-and-recovery.md) · [Deutsch](backup-and-recovery.md) · [Français](../fr/backup-and-recovery.md) · [Español](../es/backup-and-recovery.md) · [Português (Brasil)](../pt-BR/backup-and-recovery.md) · [Русский](../ru/backup-and-recovery.md)

[Git-Guard-Startseite](../../README.de.md) · [Schnellstart](README.md)

Grundlagenentwurf 0.1 — 2026-10-28.

Rechtegrenzen und wiederherstellbare Kopien behandeln verschiedene Fehler. Grundlage sind automatische Synchronisierung auf ein unabhängiges Gerät, Integritätsprüfungen und geschützte historische Wiederherstellungspunkte. **Kompilierung und Anwendungsstart sind optional:** Wählen Sie je nach Projekt manuelle Prüfungen, einen separaten Auslöser oder zusätzliche Automatisierung.

<a id="personal-and-company-schedules"></a>

## Zeitplanung für Einzelpersonen und Unternehmen

Eine Person kann einen zweiten Laptop regelmäßig einschalten und die Daten über einen konfigurierten Auslöser synchronisieren. Unterscheiden Sie Systemstart von Benutzeranmeldung: Eine Anmeldeaufgabe kann nicht vor der Anmeldung dieses Benutzers laufen. Unternehmen können ein verfügbares unabhängiges Gerät täglich einsetzen, mit Behandlung verpasster Läufe, begrenzten Netzwerk-Wiederholungen, Parallelitätskontrolle und sichtbaren Fehlerergebnissen.

Das sind Implementierungsoptionen, keine durch diesen Leitfaden installierten Funktionen. Durch Lesen entsteht weder ein Backup-Skript noch eine geplante Aufgabe. Die KI-Entwicklungsidentität darf nicht alle Wiederherstellungsversionen löschen oder das Sicherungsgerät administrieren.

<a id="define-what-the-copy-covers"></a>

## Umfang der Kopie festlegen

Ein Checkout des Hauptbranchs ist keine vollständige Serversicherung. Definieren Sie den Umfang für Branches/Historie, nur lokale oder uncommittete Arbeit, Quellcode/Dokumente, erforderliche Abhängigkeiten, Laufzeitressourcen, externe Konfiguration und private Projekte. Geheimnisse gehören in einen angemessen geschützten Wiederherstellungsprozess, niemals in öffentliche Beispiele oder gewöhnliche Archive zum Teilen.

Repository-Daten unterscheiden sich von Metadaten des Git-Hostings. Vollständige selbst gehostete Wiederherstellung kann zusätzlich konsistente Datenbanken, Konten/Rechte, Issues/PRs, Anhänge, Konfiguration und Speicher erfordern. Prüfen Sie Dienstwiederherstellung getrennt vom Quellcode-Build.

Ein aktualisierter Spiegel kann Löschungen übernehmen. Bewahren Sie unabhängige Wiederherstellungspunkte und die letzte nachweislich gute Version. Wählen Sie die Aufbewahrung nach tatsächlichem Bedarf; löschen Sie ältere Kopien nicht automatisch, nur weil eine neue Übertragung Erfolg meldet.

<a id="baseline-checks"></a>

## Grundprüfungen

1. Quelle, beabsichtigte Revision/Umfang, Ziel, Identität und freien Speicher bestätigen. Fremde Daten erhalten.
2. Synchronisieren, ohne einen geänderten oder divergierenden Checkout zu überschreiben oder Änderungen zurückzuschieben. Exakte Gleichheit mit der vorgesehenen abgeholten Revision prüfen; ein lokal vorauseilender Branch kann sonst ebenfalls als aktuell erscheinen.
3. Den festgelegten Umfang konsistent erfassen und einen eindeutigen Wiederherstellungspunkt kennzeichnen. Ein-/Ausschlussregeln und Pflichtdateien festhalten.
4. Manifest und relevante Quell-/Datei-/Archiv-Hashes prüfen. ZIP öffnen, Dateien zählen oder nur die ZIP-Datei hashen beweist nicht, dass erforderliche Quellen enthalten sind. Fehler bei Pflichtprüfungen müssen den Gesamtstatus scheitern lassen.
5. Dauerhafte Ergebnisse speichern und regelmäßig in ein separates leeres Ziel wiederherstellen. Integritäts- und Wiederherstellungsprüfung getrennt ausweisen; bis zum tatsächlichen Restore bleibt dieser ungeprüft.

<a id="optional-compilation-and-startup"></a>

## Optionale Kompilierung und Startprüfung

Falls gewählt, kompilieren Sie die wiederhergestellte Kopie mit der tatsächlich unterstützten Toolchain und einem sauberen Build-Verfahren. Halten Sie Konfiguration, Umfang, nicht geladene/ausgeschlossene Projekte und Abhängigkeiten fest. Ein leeres Wiederherstellungsverzeichnis beweist keinen sauberen Build, wenn das Archiv bereits Cache-Ausgaben enthält. Nicht deklarierte Dateien des ursprünglichen Entwicklungsrechners dürfen Lücken nicht verdecken.

Eine wichtige Erfahrung: Backups können Projektdateien enthalten, aber erforderliche Herstellerquellen auslassen. Ein Build der wiederhergestellten Kopie kann diese Lücke finden. Kompilierung allein prüft jedoch nicht alle Dokumente, Laufzeitressourcen, Hosting-Datenbanken und Anwendungspfade.

Starten Sie bei Bedarf die wiederhergestellte Anwendung in einer geeigneten Testumgebung und prüfen Sie Grundfunktionen ohne Produktionsnebenwirkungen. Für Dokumentations- oder statische Projekte wählen Sie passende Inhalts-, Link- und Website-Prüfungen statt eines sachfremden Compilers.

Kennzeichnen Sie Build/Start als **nicht gewählt**, **nicht geprüft**, **bestanden** oder **fehlgeschlagen**. Nicht gewählte optionale Tests machen eine Basissicherung nicht fehlerhaft. Eine abgeschlossene Übertragung darf nicht als Build-geprüft bezeichnet werden.

<a id="if-validation-fails"></a>

## Bei fehlgeschlagener Prüfung

Unterscheiden Sie fehlende Backup-Inhalte, Umgebungsanforderungen und Anwendungsfehler. Korrigieren Sie Auswahlregeln oder deklarierte Umgebung, erstellen Sie einen neuen Wiederherstellungspunkt, stellen Sie ihn wieder her und wiederholen Sie betroffene Prüfungen. Bewahren Sie die frühere gute Version und den Fehlernachweis. Überschreiben Sie Fehlerbelege nicht stillschweigend und behaupten Sie keine Reparatur eines alten Backups ohne erneute Prüfung.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
