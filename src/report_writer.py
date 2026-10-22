from pathlib import Path

def write_text_file(output_file_path, text_content):
    """
    Text in Datei schreiben
    Bereits vorhandene Datei überschreiben
    """

    output_path = Path(output_file_path)

    # Erstelle bei Bedarf übergeordnetes Verzeichnis automatisch mit
    # (allen nötigen Überverzeichnisse, und ohne Fehler bei bereits bestehendem Verzeichnis)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, mode='w', encoding='utf-8') as output_file:
        output_file.write(text_content)

        # Zeilenumbruch am Dateiende für eine saubere Git-Darstellung ergänzen
        output_file.write('\n')

def create_physical_model_text(physical_model):
    """
    Textdarstellung des vorgeschlagenen physischen Datenmodells erzeugen
    """

    output_lines = []

    output_lines.append('=' * 80)
    output_lines.append('VORSCHLAG FÜR EIN PHYSISCHES DATENMODELL')
    output_lines.append('=' * 80)
    output_lines.append('')
    output_lines.append('Der Datenmodellvorschlag wurde automatisch aus der Datenanalyse')
    output_lines.append('und der regelbasiert erzeugten Datenmodellkonfiguration erstellt.')
    output_lines.append('')
    output_lines.append('Tabellen, Attribute, Schlüssel, Beziehungen und Datentypen')
    output_lines.append('müssen vor einer praktischen Umsetzung geprüft werden.')
    output_lines.append('')
    output_lines.append(f"SQL-Dialekt: {physical_model['database_dialect']}")

    output_lines.append('')
    output_lines.append('TABELLENÜBERSICHT')
    output_lines.append('=' * 80)

    for physical_table in physical_model['tables']:
        output_lines.append('')
        output_lines.append(f"TABELLE: {physical_table['name']}")
        output_lines.append('-' * 80)
        output_lines.append(f"{'Attribut':<21} {'Schlüssel':<11} {'Datentyp':<17} Eigenschaft / Beziehung")
        output_lines.append('-' * 80)

        for physical_attribute in physical_table['attributes']:
            attribute_details = '-'

            if len(physical_attribute['properties']) > 0:
                attribute_details = ', '.join(physical_attribute['properties'])

            if physical_attribute['references'] is not None:
                attribute_details = f"-> {physical_attribute['references']}"

            output_lines.append(f"{physical_attribute['name']:<21} {physical_attribute['key_type']:<11} {physical_attribute['sql_data_type']:<17} {attribute_details}")

    output_lines.append('')
    output_lines.append('BEZIEHUNGEN')
    output_lines.append('=' * 80)

    relationships = physical_model['relationships']

    if len(relationships) == 0:
        output_lines.append('Keine bekannten Beziehungen vorgeschlagen.')

    for relationship in relationships:
        output_lines.append(f"{relationship['parent_table']}.id 1 <---- n {relationship['child_table']}.{relationship['foreign_key']}")

    output_lines.append('')
    output_lines.append('LEGENDE')
    output_lines.append('=' * 80)
    output_lines.append('PK  = Primärschlüssel')
    output_lines.append('FK  = Fremdschlüssel')
    output_lines.append('AK? = möglicher Alternativschlüssel, manuell prüfen')

    # Jede Zeile in der Liste mit Zeilenumbruch verbinden und zurückgeben
    return '\n'.join(output_lines)

def create_analysis_report_text(
        csv_file_path,
        data_records,
        column_analyses,
        quality_warnings,
        missing_information_warnings,
        unrecognized_columns,
        many_to_many_warnings,
        model_warnings):
    """
    Textdarstellung der Datenanalyse mit allen gefundenen Warnungen erzeugen
    """

    output_lines = []

    output_lines.append('=' * 80)
    output_lines.append('DATENANALYSEBERICHT')
    output_lines.append('=' * 80)
    output_lines.append('')
    output_lines.append(f"Quelldatei: {csv_file_path}")
    output_lines.append(f"Anzahl Datensätze: {len(data_records)}")
    output_lines.append(f"Anzahl Spalten: {len(column_analyses)}")
    output_lines.append('')

    output_lines.append('ZUSAMMENFASSUNG')
    output_lines.append('=' * 80)
    output_lines.append(f"Möglicherweise nicht atomare Werte: {len(quality_warnings)}")
    output_lines.append(f"Fehlende oder unbekannte Angaben: {len(missing_information_warnings)}")
    output_lines.append(f"Nicht zugeordnete Spalten: {len(unrecognized_columns)}")
    output_lines.append(f"Mögliche n:m-Beziehungen: {len(many_to_many_warnings)}")
    output_lines.append(f"Datenmodellwarnungen: {len(model_warnings)}")
    output_lines.append('')

    output_lines.append('DETAILANALYSE DER SPALTEN')
    output_lines.append('=' * 80)

    for column_analysis in column_analyses:
        output_lines.append('')
        output_lines.append(f"Attribut: {column_analysis['column_name']}")
        output_lines.append('-' * 80)
        output_lines.append(f"Datensätze: {column_analysis['record_count']}")
        output_lines.append(f"Gefüllte Werte: {column_analysis['filled_value_count']}")
        output_lines.append(f"Leere Werte: {column_analysis['empty_value_count']}")
        output_lines.append(f"Eindeutige Werte: {column_analysis['unique_value_count']}")
        output_lines.append(f"Wiederholte Einträge: {column_analysis['duplicate_value_count']}")
        output_lines.append(f"Maximale Zeichenlänge: {column_analysis['maximum_length']}")
        output_lines.append(f"Vorgeschlagener SQL-Datentyp: {column_analysis['suggested_sql_data_type']}")

    append_quality_warnings(output_lines, quality_warnings)

    append_missing_information_warnings(output_lines, missing_information_warnings)

    append_unrecognized_columns(output_lines, unrecognized_columns)

    append_many_to_many_warnings(output_lines, many_to_many_warnings)

    append_model_warnings(output_lines, model_warnings)

    output_lines.append('')
    output_lines.append('ABSCHLIESSENDER HINWEIS')
    output_lines.append('=' * 80)
    output_lines.append('Alle automatisch erzeugten Zuordnungen, Beziehungen, Datentypen')
    output_lines.append('und Warnungen müssen vor einer Datenbankübernahme geprüft werden.')

    return '\n'.join(output_lines)

def append_quality_warnings(output_lines, quality_warnings):
    """
    Warnungen zu möglicherweise nicht atomaren Werten ergänzen
    """

    output_lines.append('')
    output_lines.append('MÖGLICHERWEISE NICHT ATOMARE WERTE')
    output_lines.append('=' * 80)

    if len(quality_warnings) == 0:
        output_lines.append('Keine Auffälligkeiten gefunden.')
        return

    for quality_warning in quality_warnings:
        output_lines.append('')
        output_lines.append(f"WARNUNG: {quality_warning['title']}")
        output_lines.append('-' * 80)
        output_lines.append(f"Spalte: {quality_warning['column_name']}")
        output_lines.append(f"CSV-Zeile: {quality_warning['row_number']}")
        output_lines.append(f"Wert: {quality_warning['column_value']}")
        output_lines.append(f"Erkanntes Trennzeichen: {quality_warning['separator_name']}")
        output_lines.append(f"Empfehlung: {quality_warning['recommendation']}")

def append_missing_information_warnings(output_lines, missing_information_warnings):
    """
    Warnungen zu fehlenden oder unbekannten Angaben ergänzen
    """

    output_lines.append('')
    output_lines.append('FEHLENDE ODER UNBEKANNTE INFORMATIONEN')
    output_lines.append('=' * 80)

    if len(missing_information_warnings) == 0:
        output_lines.append('Keine Auffälligkeiten gefunden.')
        return

    for missing_warning in missing_information_warnings:
        output_lines.append('')
        output_lines.append(f"WARNUNG: {missing_warning['title']}")
        output_lines.append('-' * 80)
        output_lines.append(f"Spalte: {missing_warning['column_name']}")
        output_lines.append(f"CSV-Zeile: {missing_warning['row_number']}")
        output_lines.append(f"Wert: {missing_warning['column_value']}")
        output_lines.append(f"Empfehlung: {missing_warning['recommendation']}")

def append_model_warnings(output_lines, model_warnings):
    """
    Warnungen zur Datenmodellkonfiguration ergänzen
    """

    output_lines.append('')
    output_lines.append('WARNUNGEN ZUM DATENMODELL')
    output_lines.append('=' * 80)

    if len(model_warnings) == 0:
        output_lines.append('Keine Unstimmigkeiten zwischen Quelldaten und Datenmodellkonfiguration gefunden.')
        return

    for model_warning in model_warnings:
        output_lines.append('')
        output_lines.append(f"WARNUNG: {model_warning['title']}")
        output_lines.append('-' * 80)
        output_lines.append(f"Tabelle: {model_warning['table_name']}")
        output_lines.append(f"Quellspalte: {model_warning['source_column']}")
        output_lines.append(f"Zielattribut: {model_warning['target_name']}")
        output_lines.append(f"Empfehlung: {model_warning['recommendation']}")

def append_many_to_many_warnings(output_lines, many_to_many_warnings):
    """
    Warnungen zu möglichen n:m-Beziehungen ergänzen
    """

    output_lines.append('')
    output_lines.append('MÖGLICHE N:M-BEZIEHUNGEN')
    output_lines.append('=' * 80)

    if len(many_to_many_warnings) == 0:
        output_lines.append('Keine möglichen n:m-Beziehungen gefunden.')
        return

    for many_to_many_warning in many_to_many_warnings:
        output_lines.append('')
        output_lines.append(f"WARNUNG: {many_to_many_warning['title']}")
        output_lines.append('-' * 80)
        output_lines.append(f"Quellspalte: {many_to_many_warning['source_column']}")
        output_lines.append(f"CSV-Zeile: {many_to_many_warning['row_number']}")
        output_lines.append(f"Wert: {many_to_many_warning['column_value']}")
        output_lines.append(f"Erkanntes Trennzeichen: {many_to_many_warning['separator_name']}")
        output_lines.append(f"Mögliche Ausgangstabelle: {many_to_many_warning['parent_table']}")
        output_lines.append(f"Mögliche Zieltabelle: {many_to_many_warning['target_table']}")
        output_lines.append(f"Mögliche Verbindungstabelle: {many_to_many_warning['connection_table']}")
        output_lines.append(f"Empfehlung: {many_to_many_warning['recommendation']}")
        output_lines.append('Hinweis: Die mögliche Beziehung wurde nicht')
        output_lines.append('automatisch in den Datenmodellvorschlag übernommen.')

def append_unrecognized_columns(output_lines, unrecognized_columns):
    """
    Hinweise zu Spalten ergänzen, die keiner bekannten
    Tabellen- und Attributregel zugeordnet werden konnten
    """

    output_lines.append('')
    output_lines.append('NICHT ZUGEORDNETE SPALTEN')
    output_lines.append('=' * 80)

    if len(unrecognized_columns) == 0:
        output_lines.append('Alle Spalten konnten regelbasiert zugeordnet werden.')
        return

    for unrecognized_column in unrecognized_columns:
        output_lines.append('')
        output_lines.append('WARNUNG: Keine bekannte Attributregel gefunden')
        output_lines.append('-' * 80)
        output_lines.append(f"Quellspalte: {unrecognized_column['original_name']}")
        output_lines.append(f"Normalisierter Name: {unrecognized_column['normalized_name']}")
        output_lines.append('Vorläufige Tabelle: nicht_zugeordnet')
        output_lines.append('Empfehlung: Prüfen und das Regelwerk bei Bedarf erweitern.')
