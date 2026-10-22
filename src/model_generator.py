def generate_physical_model(mapped_tables, model_config):
    """
    Aus zugeordneten Tabellen und der Datenmodellkonfiguration
    einen Vorschlag für ein physisches Datenmodell erzeugen
    Das physische Datenmodell und gefundene Datenmodellwarnungen zurückgeben
    """

    physical_tables = []
    model_warnings = []

    default_primary_key = model_config['database']['default_primary_key']

    for mapped_table in mapped_tables:
        physical_attributes = []

        # Technischen Primärschlüssel für Entitätstabellen erzeugen und Attributsliste hinzufügen
        if mapped_table['table_type'] == 'entity':
            primary_key_attribute = create_primary_key_attribute(default_primary_key)
            physical_attributes.append(primary_key_attribute)

        # Attribute erzeugen und Attributsliste hinzufügen
        for mapped_attribute in mapped_table['attributes']:
            physical_attribute = create_physical_attribute(mapped_attribute)
            physical_attributes.append(physical_attribute)

            # Warnung für nicht gefundene Quellspalten erzeugen
            if not mapped_attribute['source_column_found']:
                model_warning = create_missing_source_column_warning(mapped_table['name'], mapped_attribute)
                model_warnings.append(model_warning)

        # Tabellen erzeugen und Tabellenliste hinzufügen
        physical_table = {
            'name': mapped_table['name'],
            'table_type': mapped_table['table_type'],
            'attributes': physical_attributes
        }
        physical_tables.append(physical_table)

    # Fremdschlüssel aus Datenmodellkonfiguration Beziehungen ergänzen
    add_foreign_keys(physical_tables, model_config['relationships'], default_primary_key)

    physical_model = {
        'database_dialect': model_config['database']['dialect'],
        'tables': physical_tables,
        'relationships': model_config['relationships']
    }

    return physical_model, model_warnings

def create_primary_key_attribute(default_primary_key):
    """
    Technischen Primärschlüssel einer Entitätstabelle erstellen
    """

    properties = []

    if default_primary_key['auto_increment']:
        properties.append('AUTO_INCREMENT')

    primary_key_attribute = {
        'name': default_primary_key['name'],
        'key_type': 'PK',
        'sql_data_type': default_primary_key['data_type'],
        'properties': properties,
        'references': None
    }

    return primary_key_attribute

def create_physical_attribute(mapped_attribute):
    """
    Erstellung eines physischen Datenmodellattributs
    aus entsprechendem CSV-Attribut
    """

    key_type = ''

    # Schlüsselkandidaten aus der Datenmodellkonfiguration Alternativschlüssel zur manuellen Prüfung zuweisen 'AK?'
    if mapped_attribute['key_candidate']:
        key_type = 'AK?'

    physical_attribute = {
        'name': mapped_attribute['target_name'],
        'key_type': key_type,
        'sql_data_type': mapped_attribute['suggested_sql_data_type'],
        'properties': [],
        'references': None
    }

    return physical_attribute

def add_foreign_keys(physical_tables, relationships, default_primary_key):
    """
    Ergänzung von Fremdschlüsseln bei entsprechenden Tabellen
    aus den Beziehungen der Datenmodellkonfiguration
    """

    for relationship in relationships:
        child_table = find_physical_table(physical_tables, relationship['child_table'])

        # Keiner Fremdschlüsselergänzung bei nicht gefundener Tabelle
        if child_table is None:
            continue

        foreign_key_attribute = {
            'name': relationship['foreign_key'],
            'key_type': 'FK',
            'sql_data_type': default_primary_key['data_type'],
            'properties': [],
            'references': f"{relationship[f'parent_table']}.{default_primary_key['name']}"
        }

        child_table['attributes'].append(foreign_key_attribute)

def find_physical_table(physical_tables, table_name):
    """
    Physische Tabelle anhand ihres Namens suchen
    None zurückgeben, wenn nicht gefunden
    """

    for physical_table in physical_tables:
        if physical_table['name'] == table_name:
            return physical_table

    return None

def create_missing_source_column_warning(table_name, mapped_attribute):
    """
    Erstellung einer Warnung, wenn eine Quellspalte aus der Datenmodellkonfiguration
    nicht in der CSV-Datei gefunden wurde
    """

    model_warning = {
        'warning_type': 'missing_source_column',
        'title': 'Quellspalte aus der Datenmodellkonfiguration nicht gefunden',
        'table_name': table_name,
        'source_column': mapped_attribute['source_column'],
        'target_name': mapped_attribute['target_name'],
        'recommendation': 'Spaltenname in CSV-Datei und Datenmodellkonfiguration prüfen'
    }

    return model_warning
