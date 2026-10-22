from src.config_generator import get_existing_table_names
from src.type_detector import is_missing_information

POSSIBLE_MANY_TO_MANY_RULES = [
    {
        'alternative_names': [
            'qualifikation',
            'qualifikationen',
            'kenntnis',
            'kenntnisse',
            'faehigkeit',
            'faehigkeiten',
            'skills'
        ],
        'possible_parent_tables': [
            'mitarbeiter'
        ],
        'target_table': 'qualifikation'
    },
    {
        'alternative_names': [
            'projekt',
            'projekte',
            'projects'
        ],
        'possible_parent_tables': [
            'mitarbeiter'
        ],
        'target_table': 'projekt'
    },
    {
        'alternative_names': [
            'rolle',
            'rollen',
            'roles'
        ],
        'possible_parent_tables': [
            'mitarbeiter',
            'ansprechpartner'
        ],
        'target_table': 'rolle'
    },
    {
        'alternative_names': [
            'berechtigung',
            'berechtigungen',
            'permissions'
        ],
        'possible_parent_tables': [
            'mitarbeiter'
        ],
        'target_table': 'berechtigung'
    },
    {
        'alternative_names': [
            'kategorie',
            'kategorien',
            'category',
            'categories'
        ],
        'possible_parent_tables': [
            'produkt',
            'kunde'
        ],
        'target_table': 'kategorie'
    },
    {
        'alternative_names': [
            'branche',
            'branchen',
            'wirtschaftszweig',
            'wirtschaftszweige',
            'industry',
            'industries'
        ],
        'possible_parent_tables': [
            'kunde'
        ],
        'target_table': 'branche'
    }
]

def find_possible_non_atomic_values(data_records, recognized_columns):
    """
    Erkannte Kontaktattribute auf möglicherweise
    nicht atomare Werte prüfen
    Alle gefundenen nicht atomaren Werte
    als Liste von Dictionaries zurückgeben
    """

    quality_warnings = []

    # Spalten mit möglichen durch Trennzeichen getrennten nicht atomaren Werten
    checked_target_names = [
        'telefon',
        'mobiltelefon',
        'email',
        'faxnummer'
    ]

    # Mögliche Trennzeichen
    separators = {
        '/': 'Schrägstrich',
        ';': 'Semikolon',
        '|': 'senkrechter Strich',
        '\n': 'Zeilenumbruch',
    }

    checked_source_columns = []

    for recognized_column in recognized_columns:
        if recognized_column['target_name'] in checked_target_names:
            checked_source_columns.append(recognized_column['original_name'])

    # enumerate() gibt die CSV-Zeilennummer und den zugehörigen Datensatz zurück
    # start=2 berücksichtigt die Kopfzeile in CSV-Zeile 1
    for row_number, data_record in enumerate(data_records, start=2):
        for source_column in checked_source_columns:
            # get() gibt bei nicht existierender Spalte None zurück
            column_value = data_record.get(source_column)

            # Fehlende oder leere Werte überspringen
            if column_value is None or column_value.strip() == '':
                continue

            for separator in separators:
                if separator in column_value:
                    # Datenqualitätswarnung erzeugen
                    quality_warning = create_non_atomic_value_warning(row_number, source_column, column_value, separators[separator])

                    quality_warnings.append(quality_warning)

                    # Nach dem ersten gefundenen Trennzeichen die Suche in diesem Wert beenden
                    break

    return quality_warnings

def find_missing_information_values(data_records, column_names):
    """
    Nach leeren oder als unbekannt bezeichneten Werten suchen
    Alle gefundenen Werte mit Spalten- und Zeilennummer
    als Liste von Dictionaries zurückgeben
    """

    missing_information_warnings = []

    for row_number, data_record in enumerate(data_records, start=2):
        for column_name in column_names:
            column_value = data_record.get(column_name)

            if is_missing_information(column_value):
                missing_information_warning = create_missing_information_warning(row_number, column_name, column_value)
                missing_information_warnings.append(missing_information_warning)

    return missing_information_warnings

def create_missing_information_warning(row_number, column_name, column_value):
    """
    Warnung für fehlende oder unbekannte Information erstellen
    """

    displayed_value = column_value

    # Behandlung von komplett leerem Wert
    if column_value is None or column_value.strip() == '':
        displayed_value = '[LEER]'

    missing_information_warning = {
        'warning_type': 'missing_information',
        'title': 'Fehlende oder unbekannte Information',
        'row_number': row_number,
        'column_name': column_name,
        'column_value': displayed_value,
        'recommendation': 'Wert vor dem Datenbankimport prüfen und gegebenenfalls durch NULL ersetzen'
    }

    return missing_information_warning

def create_non_atomic_value_warning(row_number, source_column, column_value, separator_name):
    """
    Warnung für möglichen nicht atomaren Wert erstellen
    """

    quality_warning = {
        'warning_type': 'possible_non_atomic_value',
        'title': 'Möglicher nicht atomarer Wert',
        'row_number': row_number,
        'column_name': source_column,
        'column_value': column_value,
        'separator_name': separator_name,
        'recommendation': 'Auf Möglichkeit mehrerer Einzelwerte prüfen'
    }

    return quality_warning

def find_possible_many_to_many_relationships(data_records, normalized_columns, dynamic_table_assignments):
    """
    Nach Spalten und Werten suchen, die auf eine mögliche
    n:m-Beziehung hindeuten
    Gefundene Beziehungen nur als Warnung zurückgeben
    und nicht automatisch erzeugen
    """

    many_to_many_warnings = []

    separators = {
        '/': 'Schrägstrich',
        ';': 'Semikolon',
        '|': 'senkrechter Strich',
        '\n': 'Zeilenumbruch'
    }

    existing_table_names = get_existing_table_names(dynamic_table_assignments)

    for normalized_column in normalized_columns:
        relationship_rule = find_many_to_many_rule(normalized_column['normalized_name'])

        # Ohne passende Regel Spalte nicht weiter prüfen
        if relationship_rule is None:
            continue

        source_column = normalized_column['original_name']

        parent_table = find_possible_parent_table(relationship_rule, existing_table_names)

        for row_number, data_record in enumerate(data_records, start=2):
            column_value = data_record.get(source_column)

            # Leere Werte können keine Mehrfachwerte enthalten
            if column_value is None or column_value.strip() == '':
                continue

            for separator in separators:
                if separator in column_value:
                    many_to_many_warning = create_many_to_many_warning(
                        row_number,
                        source_column,
                        column_value,
                        separators[separator],
                        parent_table,
                        relationship_rule['target_table'])

                    many_to_many_warnings.append(many_to_many_warning)

                    # Nur eine Warnung pro Zelle
                    break

    return many_to_many_warnings

def find_many_to_many_rule(normalized_column_name):
    """
    Passende n:m-Regel für normalisierten Spaltennamen suchen
    Gefundene Regel oder None zurückgeben
    """

    for relationship_rule in POSSIBLE_MANY_TO_MANY_RULES:
        alternative_names = relationship_rule['alternative_names']

        if normalized_column_name in alternative_names:
            return relationship_rule

    return None

def find_possible_parent_table(relationship_rule, existing_table_names):
    """
    Unter den vorhandenen Tabellen nach einer möglichen
    Ausgangstabelle für die n:m-Beziehung suchen
    Wenn keine passende Tabelle gefunden wurde,
    nicht_bestimmt zurückgeben
    """

    possible_parent_tables = relationship_rule['possible_parent_tables']

    for possible_parent_table in possible_parent_tables:
        if possible_parent_table in existing_table_names:
            return possible_parent_table

    return 'nicht_bestimmt'

def create_connection_table_name(parent_table, target_table):
    """
    Möglichen Namen für eine Verbindungstabelle erzeugen
    """

    if parent_table == 'nicht_bestimmt':
        return 'manuell_bestimmen'

    return f"{parent_table}_{target_table}"

def create_many_to_many_warning(
        row_number,
        source_column,
        column_value,
        separator_name,
        parent_table,
        target_table):
    """
    Warnung für mögliche n:m-Beziehung erstellen
    """

    connection_table = create_connection_table_name(parent_table, target_table)

    many_to_many_warning = {
        'warning_type': 'possible_many_to_many_relationship',
        'title': 'Mögliche n:m-Beziehung erkannt',
        'row_number': row_number,
        'source_column': source_column,
        'column_value': column_value,
        'separator_name': separator_name,
        'parent_table': parent_table,
        'target_table': target_table,
        'connection_table': connection_table,
        'recommendation': 'Möglichkeit einer n:m-Beziehung und Verbindungstabelle manuell überprüfen.'
    }

    return many_to_many_warning
