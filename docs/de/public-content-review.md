# Prüfung öffentlicher Inhalte

[English](../en/public-content-review.md) · [简体中文](../zh-CN/public-content-review.md) · [日本語](../ja/public-content-review.md) · [Deutsch](public-content-review.md) · [Français](../fr/public-content-review.md) · [Español](../es/public-content-review.md) · [Português (Brasil)](../pt-BR/public-content-review.md) · [Русский](../ru/public-content-review.md)

[Git-Guard-Startseite](../../README.de.md) · [Schnellstart](README.md)

Prüfentwurf 0.1. Wiederverwendbarer Ablauf für öffentlich veröffentlichte Projekte. [Arbeitsablauf](workflow.md)

<a id="configure-the-public-content-check"></a>

## Inhaltsprüfung konfigurieren

1. Bestimmen Sie das Projekt und die vorgesehenen öffentlichen Dateien genau. Interne Aufzeichnungen, Zugangsdaten, private Scannerkonfiguration und Diagnoseausgaben bleiben außerhalb dieses Baums. Enthält das Entwicklungsverzeichnis private Daten, prüfen Sie eine separate Veröffentlichungskopie. Löschen Sie private Originale nicht bloß für ein sauberes Scan-Ergebnis.
2. Suchen Sie den Checker im Git-Guard-Quellbaum oder im Referenzpaket des installierten Skills. Er benötigt Python ab 3.9 und die Standardbibliothek. Er installiert sich nicht, startet keinen Dienst und erzwingt keine Serverrechte. Geben Sie das Ziel mit `--root` an; das Skill-Verzeichnis ist nicht das Zielprojekt.
3. Andere Projekte verwenden `--profile generic`; `--profile gitguard` prüft zusätzlich die besonderen öffentlichen/privaten Verzeichnisgrenzen dieses Pakets. Der Checker hat weder eine benutzerdefinierte Geheimwortliste noch automatische Ersetzung. Für organisationsspezifische Geheimnisse oder Kontokennungen verwenden Sie einen geeigneten separaten Scanner mit privater Konfiguration außerhalb des Veröffentlichungssatzes; siehe [private Vergleichslisten](#sensitive-matching-lists-stay-private).
4. Prüfen Sie Arbeitsdateien, vorgemerkte Inhalte und ausgehende Historie getrennt. Die folgenden Pfade sind Platzhalter. Ersetzen Sie den Bereich durch die tatsächlich zu übertragenden Commits; der Checker führt weder Fetch noch Push aus. Ohne Git-Repository beginnen Sie mit Arbeitsdateien und prüfen Index/Historie später, wenn vorhanden. Die Arbeitsdateiprüfung zertifiziert keine späteren Commits.

```sh
python3 -B /path/to/gitguard/scripts/check_public_content.py --root /path/to/public-project --profile generic
python3 -B /path/to/gitguard/scripts/check_public_content.py --root /path/to/public-project --profile generic --staged
python3 -B /path/to/gitguard/scripts/check_public_content.py --root /path/to/public-project --profile generic --history origin/main..HEAD
```

<a id="interpret-results-and-handle-findings"></a>

## Ergebnisse verstehen und behandeln

Exit **0** bedeutet keine Funde innerhalb der implementierten Regeln, **1** bedeutet zu prüfende Funde, **2** eine unvollständige Prüfung. Berichte nennen Pfade, Kategorien und Zeilen, keine gefundenen Geheimwerte. Die Arbeitsdateiprüfung umfasst außer Git-Metadaten auch ignorierte Dateien: Ignorieren verhindert keine versehentliche Übernahme ins Paket.

Erkannt werden private Schlüsselmerkmale, ausgewählte GitHub-Tokenformate, Zugangsdaten in URLs, Rechnerpfade, interne IP-Adressen, bestimmte private/Laufzeitdateinamen und defekte oder aus dem Paket führende relative Markdown-Links. Nicht jedes Passwort oder Konto wird erkannt. Binärdateien erfordern manuelle Prüfung; Dateien über 2.000.000 Byte werden nicht inhaltlich untersucht. Die Grenze beträgt 3.000 Dateien bzw. 200 Commits pro Historienbereich. Größere vereinbarte Umfänge in Teilen prüfen, nicht stillschweigend auslassen.

Dokumentieren Sie Kategorie, Ort, Entscheidung und Nachprüfung ohne Geheimwerte. Korrigieren Sie die öffentliche Kopie oder Aufnahmeregeln bzw. begründen Sie harmlose/manuell geprüfte Funde und prüfen Sie betroffene Arbeits-, Index- und Historiensichten erneut. Unterdrücken Sie Binär-/Größenmeldungen nicht pauschal. Echte offengelegte Zugangsdaten brauchen Ersatz und gesondert autorisierte Historienbereinigung. Der Helfer repariert keine Historie und löscht/ersetzt keine Inhalte. Timeout oder unvollständige Prüfung gilt nicht als bestanden.

Für dieses Git-Guard-Paket erstellt `scripts/prepare_release.py` zuerst eine öffentliche Kopie mit festgelegtem Umfang. Entwicklungscaches bleiben am ursprünglichen Ort; Ausschlüsse werden separat protokolliert. Die optionale Angabe `--media-review` liest einen privaten Prüfbeleg für einzeln geprüfte PNG/MP4-Dateien mit ihren exakten SHA-256-Werten. Nur passende Binärprüfhinweise werden separat als geprüft ausgewiesen; geänderte Dateien, Geheimnisse, unlesbare Dateien und Größenüberschreitungen bleiben offen. Exitcode 0 kann solche dokumentierten Medienprüfungen enthalten, ist aber keine automatische Datenschutzbescheinigung. Siehe die [Prüf- und Paketanleitung](../../scripts/README.md).

<a id="before-a-local-commit"></a>

## Vor einem lokalen Commit

Prüfen Sie tatsächliche Änderungen einschließlich unversionierter Dateien sowie Eigentum und Veröffentlichungsrechte. Entfernen Sie interne Projektpläne, Host-/Benutzerpfade, interne Adressen, Tokens, private Schlüssel, Zugangsdaten, Kundendaten, rohe Screenshots/Logs und fremden Produktquellcode aus dem öffentlichen Umfang. Beispiele verwenden allgemeine Namen und Werte.

Prüfen Sie Links, UTF-8, sinnvolle Sprachabdeckung, Drittanbieterhinweise und zutreffende Fertigstellungsangaben. Geplante Websites/Deployments dürfen nicht als verfügbar gelten. Private Nachweise bleiben außerhalb des Release-Baums.

Untersuchen Sie vorgemerkte Bytes getrennt von Arbeitsdateien, da sie abweichen können. Prüfen Sie Umbenennungen/Löschungen, Binärdateien, Submodule und symbolische Links. Ein unauffälliges Dokument beweist keine sichere eingebettete Anlage. Lokales Committen erlaubt keine Veröffentlichung.

<a id="before-a-push"></a>

## Vor einem Push

Ermitteln Sie die exakt ausgehenden Commits zum vorgesehenen Ziel und prüfen Sie relevante Snapshots einschließlich später gelöschter Dateien. Entfernte Geheimnisse bleiben in älterer Historie erhalten. Prüfen Sie Tags/andere Referenzen nur soweit sie zum vorgesehenen Push gehören; ein neues Repository darf keine private Historie erben.

Wurde Vertrauliches committet, stoppen Sie die Veröffentlichung, veranlassen geeigneten Zugangsdatenersatz und gesondert genehmigte Abhilfe. Kein stilles Force-push oder Repository-Löschen, um Historie zu verbergen. Scanner unterstützen die Prüfung, beweisen aber keine vollständige Entfernung privater Daten.

<a id="reviewable-release"></a>

## Prüfbare Veröffentlichung

Dokumentieren Sie Ziel, Sichtbarkeit, Dateimenge, ausgehende Historie, Rechte/Lizenzentscheidung, Prüfungen und Grenzen. Bestätigen Sie die bestehende Freigabe genau dieser Aktion und erhalten Sie den menschlichen endgültigen Merge.

Bei einer verlinkten offiziellen Website prüfen Sie Hostname, HTTPS-Zertifikat, Marke und tatsächliche Seite. Übersetzen Sie sichtbare Linkbeschriftungen konsistent für alle READMEs bei gleichem kanonischen Ziel. Prüfen Sie bei autorisierter Veröffentlichung das Website-Feld des Repositorys. Das Handbuch muss auch unabhängig von der Website nutzbar bleiben.

<a id="evidence-levels"></a>

## Nachweisstufen

Unterscheiden Sie untersucht, statisch geprüft, im Verhalten getestet, bereitgestellt und vom Nutzer bestätigt. Ein Konfigurationsbild, Scannerstatus oder erfolgreicher Transfer ist kein Nachweis vollständiger Live-Sicherheit/Wiederherstellbarkeit. Nutzen Sie für Rechte die [Abnahmespezifikation](security-acceptance.md).

<a id="sensitive-matching-lists-stay-private"></a>

## Sensible Vergleichslisten bleiben privat

Veröffentlichen Sie nur wiederverwendbare Prüflogik und erfundene Testdaten. Reale Geheimnisse, Kontokennungen und projektspezifische Vergleichs-/Ersetzungslisten bleiben außerhalb von Quellbaum, Skill-Paketen, Downloads, Screenshots und ausgehender Git-Historie. Eine Regel mit einem realen Geheimwert ist selbst vertraulich, auch als Scannerkonfiguration. Ignore-Regeln ersetzen weder Index- noch Historienprüfung.

Nutzen Sie bei einem separaten Scanner wie Gitleaks eine private Konfiguration, geben Sie sie zur Laufzeit aus einem privaten Ort dazu. Nicht ins Release kopieren, keine Trefferwerte ausgeben und keine echten Werte als Kommandoargumente oder Testdaten verwenden. Diagnoseausgaben bleiben privat und werden vor Weitergabe bereinigt.

Der mitgelieferte Checker wurde für Git Guard neu geschrieben. Er lädt keine vorhandene private Vergleichsliste und erkennt nicht gezielt Handels-/Kundenkonten, beliebige Passwörter oder alle Tokentypen. Seine Heuristiken ergänzen geeignete Scanner und menschliche Prüfung. Ein sauberer Bericht ist keine vollständige Geheimnisfreigabe; Historie wird nicht bereinigt.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
