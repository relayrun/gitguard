# Täglicher Git-Ablauf

[English](../en/workflow.md) · [简体中文](../zh-CN/workflow.md) · [日本語](../ja/workflow.md) · [Deutsch](workflow.md) · [Français](../fr/workflow.md) · [Español](../es/workflow.md) · [Português (Brasil)](../pt-BR/workflow.md) · [Русский](../ru/workflow.md)

[Git-Guard-Startseite](../../README.de.md) · [Schnellstart](README.md)

Grundlagenentwurf 0.1 — 2026-10-28.

<a id="read-and-scope-the-work"></a>

## Arbeit lesen und abgrenzen

Bestimmen Sie Projekt, lokales Verzeichnis, Branch, Remote, Sichtbarkeit und aktuelle Freigabe genau. Lesen Sie den Agent-Einstieg, den aktuellen Plan und die einschlägigen Betriebsanweisungen. Lassen Sie fremde vorgemerkte und nicht vorgemerkte Änderungen unverändert. Bearbeiten, Committen, Pushen, PR-Erstellung, Release-Veröffentlichung und Website-Bereitstellung sind getrennte Aktionen. Bereits erteilte Freigaben gelten weiter; ein allgemeiner Plan erlaubt nicht automatisch alle diese Aktionen.

<a id="step-1--record-the-local-change"></a>

## Schritt 1 — lokale Änderung festhalten

Prüfen Sie Dateiliste und Diff und führen Sie passende Prüfungen aus. Bei öffentlichem Material erfolgt die [Veröffentlichungsprüfung](public-content-review.md) **vor dem Commit**, auch wenn dieser zunächst lokal bleibt. Merken Sie nur die beabsichtigten Dateien vor und erstellen Sie den autorisierten lokalen Commit. Prüfen Sie anschließend dessen Kennung, Inhalt und die verbleibenden Änderungen im Arbeitsbaum.

Ein lokaler Commit lädt nichts hoch. Initialisieren Sie bei einer gewöhnlichen Bearbeitung nicht nebenbei ein weiteres Repository, fügen Sie kein Remote hinzu und ändern Sie weder Schutzregeln noch Backup-Aufgaben. Verwerfen Sie keine fremden Änderungen, nur um einen sauberen Status zu erhalten.

<a id="step-2--share-the-branch-and-prepare-the-pr"></a>

## Schritt 2 — Branch teilen und PR vorbereiten

Prüfen Sie innerhalb der Freigabe das Remote-Ziel und den gesamten Branch-Diff zum tatsächlichen Zielbranch. Beziehen Sie frühere, noch nicht integrierte Branch-Commits ein, nicht nur den neuesten. Kontrollieren Sie vor jedem Upload erneut die Grenze der öffentlichen Inhalte.

Pushen Sie den freigegebenen Arbeitsbranch ohne Force. Im Standardbeispiel von Homepage und Video bereitet die KI Quelle/Ziel, Titel- und Beschreibungsvorschlag sowie tatsächliche Prüfergebnisse vor. Der Mensch erstellt die Anfrage in der Weboberfläche. Ein vorbereiteter Formulartext ist noch kein erstellter PR.

Ein Anwender kann die KI gesondert zum Erstellen oder Aktualisieren des zugehörigen PR autorisieren. Erst dann wird diese Aktion ausgeführt und ihre tatsächliche Existenz bzw. ihr Status geprüft. Die Variante verleiht kein Recht zum endgültigen Merge. Ein gepushter Branch oder Entwurfs-PR in einem öffentlichen Repository ist bereits öffentlich, nicht erst nach dem Merge.

Blockieren Regeln oder Rechte die Aktion, melden Sie die tatsächliche Ablehnung. Umgehen Sie sie nicht durch Administratorsitzungen, andere Tokens, direkte Serverports, Containerzugriff oder eine andere Oberfläche. Die Lösung eines Inhaltskonflikts darf die Freigabe nicht stillschweigend erweitern.

<a id="human-final-review-and-merge"></a>

## Abschließende menschliche Prüfung und Merge

Im Standardbeispiel öffnet der Mensch die Anfrageseite des Repositorys in OneDev/GitHub, wählt die Neuanlage, prüft vorgeschlagene Quell- und Zielbranches, trägt Titel/Beschreibung ein und sendet ab. Existiert nach einem separat autorisierten Ablauf bereits eine Anfrage, wird sie geprüft statt dupliziert. Branch-Vorschläge sind keine Zustimmung.

Der Mensch prüft den vollständigen Diff, Testnachweise, Ziel und gewünschtes Ergebnis und führt den Merge aus. Die KI klickt in diesem Ablauf nicht auf Merge, ruft keine Merge-API/CLI auf und aktiviert keinen automatischen Merge im Namen der Person.

Pflichtreviews und ausschließlich menschliche Merge-Rechte sind verschiedene Kontrollen. Auch nach bestandener Review-Prüfung kann eine KI-Identität weiterhin mergen dürfen. Prüfen Sie beides, bevor Sie technische Durchsetzung behaupten. Schützen Sie neben dem Bot-Konto auch Administratorzugänge und bestehende Browsersitzungen.

<a id="after-the-human-confirms-merge"></a>

## Nachdem der Mensch den Merge bestätigt

1. Prüfen Sie den tatsächlichen serverseitigen Merge und sein Ziel. Ein Auftrag zur PR-Vorbereitung bestätigt keinen Merge.
2. Holen Sie die Änderungen ab und vergleichen Sie die geprüfte Änderung mit dem integrierten Ergebnis. Squash/Rebase kann Commit-Kennungen ändern. Ist der Zielbranch weitergelaufen, vergleichen Sie die passende Basis und den resultierenden Diff statt vollständige identische Repository-Bäume zu verlangen. Bei einem Squash auf gleicher Basis sind gleiche Endbäume ein hilfreicher Nachweis.
3. Prüfen Sie vor dem Aufräumen uncommittete Arbeit, unveröffentlichte Commits, andere Worktrees und die geltende Wiederherstellungs-/Aufbewahrungsregelung. Erstellen Sie keine unbestellten Backups und überschreiben Sie keine nur lokal vorhandene Arbeit, um Gleichstand zu erzwingen.
4. Aktualisieren Sie den lokalen geschützten Branch per Fast-forward, soweit seine Beziehung zum Remote dies zulässt. Bei Divergenz stoppen und erklären, statt sie per Reset zu beseitigen.
5. Entfernen Sie im freigegebenen Umfang nur den nachweislich abgeschlossenen Arbeitsbranch. Hat der Server ihn bereits entfernt, bereinigen Sie die veraltete Tracking-Referenz, ohne den Branch neu anzulegen. Ein Squash besteht möglicherweise keinen einfachen Abstammungstest für Branch-Löschung. Prüfen Sie Inhalt und aufzubewahrende Arbeit vor jeder autorisierten Alternative.
6. Melden Sie den tatsächlichen Branch-/Worktree-Zustand sowie aufbewahrte Arbeit oder offene Probleme. Lokales Aufräumen ist weder Deployment noch Release-Veröffentlichung.

<a id="keep-the-rules-portable"></a>

## Regeln übertragbar halten

Benennungs- und Review-Konventionen legt der Repository-Eigentümer fest. OneDev und GitHub haben unterschiedliche Kontrollen und Kontenmodelle; die gemeinsame Reihenfolge bleibt gleich. Trennen Sie mit der [Sicherheitsabnahme](security-acceptance.md) beabsichtigte Regeln von nachgewiesenen Rechtegrenzen. Die [GitHub-Zuordnung](github.md) erklärt die dortigen Unterschiede.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->
