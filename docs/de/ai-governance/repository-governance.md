# Repository-Governance

## Zweck

Dieses Dokument definiert die Governance-Regeln für das Repository. Governance stellt sicher, dass alle Änderungen am Repository kontrolliert, nachvollziehbar und auditierbar sind. Ohne definierten Freigabeprozess werden weder Code noch Dokumentation in geschützte Branches gemergt.

---

## CODEOWNERS

Die Datei `.github/CODEOWNERS` definiert, welche Personen oder Teams für bestimmte Pfade im Repository verantwortlich sind. Wenn Änderungen an diesen Pfaden erfolgen, werden Review-Anfragen automatisch den jeweiligen CODEOWNERS zugewiesen.

Beispielkonfiguration:

```text
* @KonstantinData
docs/de/privacy/ @KonstantinData
docs/en/security/ @KonstantinData
.github/workflows/ @KonstantinData
```

Regeln:

* Änderungen an allen Pfaden erfordern eine Freigabe durch die zuständigen CODEOWNERS.
* Dies gilt sowohl für `docs/de` als auch für `docs/en`.
* Ein Merge ohne CODEOWNERS-Freigabe ist nicht möglich, sofern die entsprechenden Branch-Protection-Regeln aktiviert sind.

---

## Branch-Schutz

Die folgenden Branches sind durch Branch-Protection-Regeln geschützt:

* `main` (verpflichtend)
* `develop` (optional, empfohlen)

Erforderliche Einstellungen:

* Pull Request vor Merge erforderlich
* Review durch CODEOWNERS erforderlich
* Status-Checks müssen erfolgreich sein
* Administratoren sind in den Schutzregeln eingeschlossen (muss aktiviert sein)

---

## Merge-Prozess

1. Erstelle einen neuen Branch auf Basis des aktuellen Stands von `main`.
2. Nimm Änderungen vor und eröffne einen Pull Request.
3. CODEOWNERS werden automatisch zur Prüfung angefordert und müssen den PR freigeben.
4. Alle konfigurierten CI-Checks müssen erfolgreich durchlaufen.
5. Ein Merge ist nur nach vollständiger Freigabe und erfolgreichen Checks erlaubt.

---

## Geltungsbereich der Governance

Die folgenden Repository-Bereiche unterliegen der Governance:

* `docs/de/**`
* `docs/en/**`
* `policies/**`
* `bom/**`
* `.github/workflows/**`
* `scripts/**`

---

## Nichteinhaltung

Ein Merge wird blockiert, wenn eine der folgenden Bedingungen zutrifft:

* Keine Freigabe durch CODEOWNERS
* Erforderliche Status-Checks sind fehlgeschlagen
* Erforderliche Dokumentation fehlt
* Strukturelle Verstöße gegen Repository-Konventionen liegen vor
