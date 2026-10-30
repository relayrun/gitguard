# Spezifikation der Sicherheitsabnahme

[English](../en/security-acceptance.md) · [简体中文](../zh-CN/security-acceptance.md) · [日本語](../ja/security-acceptance.md) · [Deutsch](security-acceptance.md) · [Français](../fr/security-acceptance.md) · [Español](../es/security-acceptance.md) · [Português (Brasil)](../pt-BR/security-acceptance.md) · [Русский](../ru/security-acceptance.md)

[Git-Guard-Startseite](../../README.de.md) · [Schnellstart](README.md)

Grundlagenentwurf 0.1 — 2026-10-28.

Diese Spezifikation gilt gemeinsam für das menschliche Handbuch und künftige Skills. Sie ist ein Testplan, kein bestandener Abnahmebericht einer Installation. Der ausführliche OneDev-Leitfaden und die kürzere GitHub-Zuordnung verweisen hierher, statt widersprüchliche Kriterien festzulegen.

<a id="inspect-first"></a>

## Zuerst untersuchen

Erfassen Sie Plattform/Version, Sichtbarkeit, geschützte Branches, Identitäten, Rollen, Token-/Anwendungsrechte, vererbte Regeln, Reihenfolge/Durchsetzung und Ausnahmen. Prüfen Sie relevante Git-/SSH-/HTTPS-, Web-, API-, CI-/Integrations-, Proxy- sowie Host-/Speicherpfade. Kontrollieren Sie, ob die KI eine bestehende menschliche Browsersitzung oder Zugangsdaten mitbenutzen kann.

Beim Selbsthosting gehören Host-/Container-/Datenverzeichniszugriffe und alternative Ports dazu. Ein separater Server oder NAS bildet nur dann eine wirksame Grenze, wenn die KI ihn nicht administrieren kann. Ein Reverse Proxy kontrolliert nur durchgeleitete Anfragen, nicht offene Alternativwege oder den darunterliegenden Speicher. Gehostete Plattformen brauchen eigene Konto-/Anwendungskontrollen; das selbst gehostete Proxy-Muster lässt sich nicht einfach übernehmen.

<a id="test-only-in-the-authorized-environment"></a>

## Nur in der autorisierten Umgebung testen

Verwenden Sie ein gesondert autorisiertes, entbehrliches Testrepository oder eine Testinstanz mit repräsentativen Regeln und getrennten Identitäten. Bestätigen Sie wiederherstellbare Testdaten und erwartete erlaubte Vorgänge. Negative Tests richten sich ausschließlich gegen diese Testobjekte, nutzen harmlose Inhalte und hinterlassen Nachweise. Dieses Dokument erlaubt weder Produktionslöschungen noch das Umschreiben realer Historie oder Änderungen produktiver Rollen.

<a id="acceptance-matrix"></a>

## Abnahmematrix

| Fähigkeit/Pfad | Erwartung für die eingeschränkte KI-Identität | Erforderlicher Nachweis |
| --- | --- | --- |
| Erlaubten Arbeitsbranch lesen und vorbereiten | Im Umfang erlaubt | Positivkontrolle erreicht den vorgesehenen Dienst mit der vorgesehenen Identität |
| Neue Commits normal direkt auf geschütztes main pushen | Nach Richtlinie abgelehnt | Tatsächliche Ablehnung und unveränderte geschützte Referenz |
| Geschützte Historie per Force-push ändern | Abgelehnt | Rechteverweigerung und unveränderte Historie |
| Geschützten Branch/Ref löschen | Abgelehnt | Tatsächliche Ablehnung und weiter bestehende Referenz |
| Repository/Projekt löschen | Abgelehnt | Testprojekt bleibt erhalten; Konto besitzt keine effektive Löschberechtigung |
| Für den erforderlichen menschlichen Reviewer genehmigen | Abgelehnt | Review-Identitäten und Freigabenachweis |
| Endgültiger Merge, auch nach erfolgreichen Reviews | Bei ausschließlich menschlichem Merge abgelehnt | Tatsächliches Rechteergebnis; ein ungeprüfter PR allein reicht nicht |
| Auto-Merge oder gleichwertige Integration aktivieren/nutzen | Für KI in diesem Ablauf abgelehnt | API-/Web-/Anwendungspfad und tatsächlicher Akteur dokumentiert |
| Rollen, Schutz, Ausnahmen oder Sicherheitsprüfungen ändern | Abgelehnt | Konfiguration vorher/nachher und Ablehnung |
| Andere Zugangsdaten, Sitzung, Endpunkt oder CI-Pfad nutzen | Keine unbeabsichtigte Befugnis | Inventar und begrenzter Test aller relevanten Pfade; unbekannte Pfade bleiben ungeprüft |
| Host/Container/Repository-Speicher ändern | Kein administrativer oder destruktiver Zugriff | OS-/Speichergrenze nachgewiesen, nicht nur ein Anwendungsschalter |
| Alle Wiederherstellungspunkte löschen/überschreiben | Für Entwicklungsidentität abgelehnt | Unabhängige Aufbewahrung und getrennte Backup-Administration |
| Mensch prüft und führt vorgesehenen Merge aus | Unter Review-Regeln erlaubt | Positivkontrolle mit der tatsächlichen menschlichen Identität |

Prüfen Sie Branch-/Tag-Erstellung, Tag-Löschung und branchbezogene Ausnahmen, soweit sie die Richtlinie beeinflussen. Blockieren Sie nicht versehentlich sämtliche Vorbereitungen und bezeichnen das als gelungene Aufgabentrennung.

<a id="record-each-result"></a>

## Jedes Ergebnis erfassen

Bewahren Sie je Zeile auf: Testidentität, Software-/Konfigurationsstand, Quelle/Ziel, Vorgang und Pfad, erwartetes und tatsächliches Ergebnis samt Grund, Zustand vorher/nachher, Zeitpunkt und Nachweisort. Entfernen Sie Zugangsdaten und sachfremde private Daten vor dem Teilen.

Verwenden Sie **bestanden**, **fehlgeschlagen** oder **nicht geprüft** mit Erklärung. Timeout, Anmeldefehler, Konflikt, ungültige Anfrage, WIP-Markierung, unerreichbarer Server, Screenshot oder aktivierter Schalter beweisen keine gezielte Rechteverweigerung. Eine Positivkontrolle trennt Durchsetzung von einem defekten Testaufbau.

Ist eine erforderliche Grenze ungeprüft oder fehlerhaft, benennen Sie die Lücke. Geben Sie an, welche Vorgänge tatsächlich blockiert sind; behaupten Sie nicht, sämtliche KI-Fehler seien ausgeschlossen. Wiederholen Sie betroffene Tests nach Änderungen an Rollen, Proxy, Regeln, Version oder Integrationen. Frühere Nachweise bleiben mit ihrem damaligen Umfang erhalten.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
