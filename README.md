# datenmodell_assistent

Ein regelbasiertes Python-Tool zur Analyse von CSV-Geschäftsdaten und zur automatischen Erzeugung überprüfbarer Vorschläge für physische relationale Datenmodelle.

Die Anwendung analysiert CSV-Spalten und Werte, schlägt SQL-Datentypen vor, erkennt Datenqualitätsprobleme und ordnet bekannte Attribute über ein erweiterbares Regelwerk passenden Tabellen zu. Als Ergebnisse werden eine JSON-Datenmodellkonfiguration, ein physischer Datenmodellvorschlag und ein ausführlicher Analysebericht erzeugt.

> **Hinweis:** Alle Zuordnungen, Datentypen, Schlüssel und Beziehungen sind regelbasierte Vorschläge. Die Ergebnisse müssen vor einer praktischen Datenbankumsetzung fachlich und technisch geprüft werden.

## Status

- **Aktuelle Version:** v1.0-dev
- **Python-Version:** Python 3.13.15
- **SQL-Dialekt:** MySQL
- **Datenquelle:** CSV mit Semikolon als Trennzeichen
- **Externe Bibliotheken:** keine

Das Projekt verwendet ausschließlich Python und Module der Standardbibliothek.

## Funktionsübersicht

- CSV-Dateien über ein Konsolenmenü auswählen und einlesen
- Spaltennamen normalisieren und alternative Bezeichnungen erkennen
- typische Unternehmensattribute regelbasiert Tabellen zuordnen
- unbekannte Spalten unter `nicht_zugeordnet` sammeln
- SQL-Datentypen und Textlängen vorschlagen
- Primär-, Fremd- und mögliche Alternativschlüssel ergänzen
- bekannte 1:n-Beziehungen vorschlagen
- fehlende, unbekannte und möglicherweise nicht atomare Werte erkennen
- mögliche n:m-Beziehungen zur manuellen Prüfung dokumentieren
- dynamische Datenmodellkonfiguration als JSON speichern
- CSV-spezifische Modell- und Analyseberichte erzeugen

## Bekannte Einschränkungen

- Die Zuordnung basiert auf einem festen, erweiterbaren Regelwerk.
- Unbekannte oder mehrdeutige Begriffe können nicht sicher eingeordnet werden.
- Beziehungen werden anhand bekannter Tabellenkombinationen vorgeschlagen.
- Funktionale Abhängigkeiten und Kardinalitäten werden nicht vollständig analysiert.
- Mögliche n:m-Beziehungen werden erkannt, aber noch nicht automatisch modelliert.
- Verbindungstabellen und zusammengesetzte Primärschlüssel werden noch nicht erzeugt.
- `DECIMAL(10,2)` wird als allgemeiner Dezimaltyp verwendet.
- CSV-Dateien müssen aktuell UTF-8-codiert und mit Semikolon getrennt sein.
- Der Datenbankdialekt ist auf MySQL vorkonfiguriert.
- Große Dateien können umfangreiche Warnungslisten erzeugen.
- Die Ergebnisse ersetzen keine fachliche und technische Prüfung.

## Roadmap

- Excel-Dateien und mehrere Tabellenblätter unterstützen
- optionale Anbindung an Google Sheets
- ausführbare SQL-DDL-Dateien erzeugen
- Verbindungstabellen für bestätigte n:m-Beziehungen vorschlagen
- KI-gestützte Erkennung unbekannter oder mehrdeutiger Attribute erproben

## Changelog

### v1.0-dev

Aktueller regelbasierter Entwicklungsstand.

- **M8h:** Code-Review, Absicherungen und umfangreiche Funktionstests
- **M8g:** CSV-spezifische JSON-, Modell- und Analyseberichte
- **M8f:** Erkennung möglicher n:m-Beziehungen
- **M8e:** Dynamische Modellkonfiguration und bekannte 1:n-Beziehungen
- **M8d:** Dynamische Tabellenzuordnung und `nicht_zugeordnet`
- **M8c:** Regelwerk für typische Unternehmensattribute
- **M8b:** Normalisierung von Spaltennamen
- **M8a:** CSV-Auswahl und CSV-spezifische Ausgabedateien

### v0.1-prototype

Prototyp mit statischer JSON-Datenmodellkonfiguration.

- **M7:** Konsolenausgabe zusammenfassen und Textberichte speichern
- **M6:** Physischen Datenmodellvorschlag erzeugen
- **M5b:** Konfiguration und Analyseergebnisse zusammenführen
- **M5a:** Statische JSON-Konfiguration laden
- **M4:** Möglicherweise nicht atomare Werte erkennen
- **M3:** SQL-Datentypen und Textlängen vorschlagen
- **M2:** Spalten und Werte analysieren
- **M1:** CSV-Datei einlesen

## Lernziele des Projekts

- Python-Grundlagen praktisch vertiefen
- mit Listen, Dictionaries und verschachtelten Datenstrukturen arbeiten
- CSV- und JSON-Dateien verarbeiten
- modulare Programmstrukturen entwickeln
- Datenanalyse ohne externe Bibliotheken umsetzen
- regelbasierte Zuordnungslogik entwickeln
- Datenqualität systematisch prüfen
- physische relationale Datenmodelle besser verstehen
- Primär-, Fremd- und Alternativschlüssel unterscheiden
- 1:n- und mögliche n:m-Beziehungen erkennen

## Lizenz

Dieses Projekt ist als privates Lern-, Entwicklungs- und Referenzprojekt entstanden.

Die bereitgestellten CSV-Dateien enthalten ausschließlich synthetische Beispieldaten. Es werden keine realen Unternehmens-, Kunden- oder Personendaten verwendet.

Lizenzinformationen siehe Repository.
