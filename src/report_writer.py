def write_text_file(output_file_path, text_content):
    """
    Text in Datei schreiben
    Bereits vorhandene Datei überschreiben
    """

    with open(output_file_path, mode='w', encoding='utf-8') as output_file:
        output_file.write(text_content)

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
    output_lines.append('und der bereitgestellten Datenmodellkonfiguration erzeugt.')
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
                attribute_details = (f"-> {physical_attribute['references']}")

            output_lines.append(f"{physical_attribute['name']:<21} {physical_attribute['key_type']:<11} {physical_attribute['sql_data_type']:<17} {attribute_details}")

    output_lines.append('')
    output_lines.append('BEZIEHUNGEN')
    output_lines.append('=' * 80)

    for relationship in physical_model['relationships']:
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
        model_warnings):
    """
    Textdarstellung der Datenanalyse und alle gefundenen Warnungen erzeugen
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
        output_lines.append(f"Mehrfachwerte: {column_analysis['duplicate_value_count']}")
        output_lines.append(f"Maximale Zeichenlänge: {column_analysis['maximum_length']}")
        output_lines.append(f"Vorgeschlagener SQL-Datentyp: {column_analysis['suggested_sql_data_type']}")

    append_quality_warnings(output_lines, quality_warnings)

    append_missing_information_warnings(output_lines, missing_information_warnings)

    append_model_warnings(output_lines, model_warnings)

    output_lines.append('')
    output_lines.append('ABSCHLIESSENDER HINWEIS')
    output_lines.append('=' * 80)
    output_lines.append('Alle erkannten Probleme und erzeugten Vorschläge')
    output_lines.append('müssen vor einer Datenbankübernahme geprüft werden.')

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
    output_lines.append('DATENMODELLWARNUNGEN')
    output_lines.append('=' * 80)

    if len(model_warnings) == 0:
        output_lines.append('Keine Auffälligkeiten gefunden.')
        return

    for model_warning in model_warnings:
        output_lines.append('')
        output_lines.append(f"WARNUNG: {model_warning['title']}")
        output_lines.append('-' * 80)
        output_lines.append(f"Tabelle: {model_warning['table_name']}")
        output_lines.append(f"Quellspalte: {model_warning['source_column']}")
        output_lines.append(f"Zielattribut: {model_warning['target_name']}")
        output_lines.append(f"Empfehlung: {model_warning['recommendation']}")
