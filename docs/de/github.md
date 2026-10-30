# GitHub: kurze Zuordnung der Plattformfunktionen

[English](../en/github.md) · [简体中文](../zh-CN/github.md) · [日本語](../ja/github.md) · [Deutsch](github.md) · [Français](../fr/github.md) · [Español](../es/github.md) · [Português (Brasil)](../pt-BR/github.md) · [Русский](../ru/github.md)

[Git-Guard-Startseite](../../README.de.md) · [Schnellstart](README.md)

Grundlagenentwurf 0.1 — Abgleich mit den verlinkten GitHub-Dokumenten am 2026-10-28.

OneDev bleibt das ausführliche Konfigurationsbeispiel von Git Guard. GitHub ist das zweite Beispiel und nutzt denselben [Arbeitsablauf](workflow.md), dieselbe [Sicherheitsabnahme](security-acceptance.md) und [Backup-Anleitung](backup-and-recovery.md). Dieses Kapitel ordnet Fähigkeiten zu und beschreibt nicht die aktuelle Konfiguration eines konkreten Repositorys.

| Gemeinsame Anforderung | Umsetzung auf GitHub |
| --- | --- |
| Lokal vorbereiten und committen | Gewöhnliche lokale Git-Arbeit; noch kein Upload |
| Autorisierte Zusammenarbeit am Remote | Arbeitsbranch pushen und Anfragetext vorbereiten; im Standardbeispiel erstellt der Mensch den PR im Web |
| Pflichtreview und geschütztes main | Passenden Branchschutz/Rulesets und Reviewer-Anforderungen konfigurieren |
| Force-push und Löschen geschützter Referenzen begrenzen | Entsprechende Erlaubnisse deaktiviert lassen und Ausnahmen prüfen |
| Menschlicher endgültiger Merge | KI-Identität/Zugangsdaten von menschlichen Rechten trennen; Pflichtreview allein schafft kein exklusives Merge-Recht |
| Nach menschlichem Merge | Ergebnis prüfen, lokales main sicher synchronisieren und nur bestätigte abgeschlossene Branches entfernen |

GitHub dokumentiert geschützte Branches und Branch-/Tag-Rulesets für öffentliche Repositorys in Free-Tarifen; bei privaten Repositorys hängt die Verfügbarkeit vom Tarif ab. Daraus folgt nicht die Verfügbarkeit aller erweiterten Funktionen oder Push-Rulesets. [Geschützte Branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) · [Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).

Erforderliche zustimmende Reviews bestimmen nicht allein, wer anschließend mergen darf. Administratorausnahmen beim klassischen Branchschutz, erlaubte Akteure, Ruleset-Ausnahmen, Anwendungsrechte und zugängliche menschliche Anmeldedaten sind ebenfalls relevant. Dokumentierte Push-Beschränkungen geeigneter Organisationsrepositorys sind zusammen mit vorgeschriebenen PRs zu bewerten. Prüfen Sie die tatsächliche Identität, bevor Sie ausschließlich menschlichen Merge behaupten. Verwaltung, Löschen und Regeländerungen müssen getrennt beim Eigentümer bleiben.

Im Standardbeispiel prüft der Mensch im PR-Dialog base (Ziel) und compare (Quelle), trägt Titel/Beschreibung ein, sendet ab, prüft Diff und Checks und führt den Merge selbst aus. Erforderliche unabhängige Zustimmungen gelten weiter; Erstellen eines PR ist keine Zustimmung. Die separat freigegebene KI-PR-Erstellung erklärt der [gemeinsame Ablauf](workflow.md).

GitHub unterstützt automatischen Merge, dieser Ablauf belässt die Ausführung jedoch beim Menschen. Aktivieren Sie Auto-Merge nicht beiläufig. Ein als eingeschränkt bezeichnetes Token garantiert nicht, dass Arbeitsbranch-Schreibrechte erlaubt und sämtliche Merge-Aktionen verboten sind.

Der selbst gehostete OneDev-Reverse-Proxy wird nicht zu einem Proxy vor GitHub. Übertragen Sie das Schutzziel auf GitHubs Identitäten, Regeln, Anwendungsrechte und überprüfte Zugriffspfade.

Prüfen Sie vor der Übernahme Tarif, Sichtbarkeit, aktive Regeln und Ausnahmen und wenden Sie die gemeinsame Abnahmematrix in einer autorisierten Testumgebung an. Durch das Schreiben dieses Kapitels wurden weder Repository-Einstellungen verändert noch negative Sicherheitstests durchgeführt.


<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
