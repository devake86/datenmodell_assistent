def map_column_analyses_to_tables(column_analyses, model_config):
    """
    Zuordnung der Analyseergebnisse zu den entsprechenden
    Tabellen und Attributen der Datenmodellkonfiguration
    Rückgabe der Zuordnungen als Liste von Dictionaries
    """

    mapped_tables = []

    for table_config in model_config['tables']:
        mapped_attributes = []

        for attribute_config in table_config['attributes']:
            # Name der CSV-Spalte holen aus Datenmodellkonfiguration holen
            source_column = attribute_config['source_column']

            # Passendes Dictionary im Analyseergebnis suchen
            column_analysis = find_column_analysis(column_analyses, source_column)

            # Attribut Dictionaries erstellen und Liste hinzufügen
            mapped_attribute = create_mapped_attribute(attribute_config, column_analysis)
            mapped_attributes.append(mapped_attribute)

        # Table Dictionaries mit den entsprechenden Attribut Dictionaries erstellen und Liste hinzufügen
        mapped_table = {
            'name': table_config['name'],
            'table_type': table_config['table_type'],
            'attributes': mapped_attributes
        }
        mapped_tables.append(mapped_table)

    return mapped_tables

def find_column_analysis(column_analyses, source_column):
    """
    Analyse einer bestimmten CSV-Spalte suchen und zurückgeben
    Rückgabe None, wenn keine entsprechende Spalte gefunden wurde
    """

    for column_analysis in column_analyses:
        if column_analysis['column_name'] == source_column:
            return column_analysis

    return None

def create_mapped_attribute(attribute_config, column_analysis):
    """
    Verbindung von Attributskonfiguration mit
    entsprechender Analyse der CSV-Spalte
    Vorherige Prüfung ob Spalte in der Datenmodellkonfiguration
    auch in der CSV vorhanden ist, wenn nicht, dann Konfigurationsproblem
    """

    mapped_attribute = {
        'source_column': attribute_config['source_column'],
        'target_name': attribute_config['target_name'],
        'key_candidate': attribute_config['key_candidate'],
        'source_column_found': column_analysis is not None
    }

    if column_analysis is None:
        mapped_attribute['suggested_sql_data_type'] = 'UNBEKANNT'
        mapped_attribute['maximum_length'] = 0
        mapped_attribute['empty_value_count'] = 0
        mapped_attribute['unique_value_count'] = 0
        mapped_attribute['duplicate_value_count'] = 0

        return mapped_attribute

    # Für Datenmodellvorschlag benötigte Informationen aus Analyse Dictionary übernehmen
    mapped_attribute['suggested_sql_data_type'] = column_analysis['suggested_sql_data_type']
    mapped_attribute['maximum_length'] = column_analysis['maximum_length']
    mapped_attribute['empty_value_count'] = column_analysis['empty_value_count']
    mapped_attribute['unique_value_count'] = column_analysis['unique_value_count']
    mapped_attribute['duplicate_value_count'] = column_analysis['duplicate_value_count']

    return mapped_attribute
