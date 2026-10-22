from src.type_detector import is_missing_information

def find_possible_non_atomic_values(data_records):
    """
    In bestimmten Spalten nach Werten suchen
    die mehrere Einzelwerte haben könnten
    Alle gefundenen nicht atomaren Werte
    als Liste von Dictionaries zurückgeben
    """

    quality_warnings = []

    # Spalten mit möglichen durch Trennzeichen getrennten nicht atomaren Werten
    checked_column_names = [
        'Telefon',
        'E-Mail'
    ]

    # Mögliche Trennzeichen
    separators = {
        '/': 'Schrägstrich',
        ';': 'Semikolon',
        '|': 'senkrechter Strich',
        '\n': 'Zeilenumbruch',
    }

    # enumerate() gibt CSV-Zeilennummer (startend bei Zeile 2 exklusive Kopfzeile 1) und zugehörigen Datensatz zurück
    for row_number, data_record in enumerate(data_records, start=2):
        for column_name in checked_column_names:
            # get() gibt bei nicht existierender Spalte None zurück
            column_value = data_record.get(column_name)

            # Fehlende oder leere Werte überspringen
            if column_value is None or column_value.strip() == '':
                continue

            for separator in separators:
                if separator in column_value:
                    separator_name = separators[separator]

                    # Datenqualitätswarnung erzeugen
                    quality_warning = create_non_atomic_value_warning(row_number, column_name, column_value, separator_name)

                    quality_warnings.append(quality_warning)

                    # Sobald ein Trennzeichen gefunden suche in diesem Wert beenden
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

def create_non_atomic_value_warning(row_number, column_name, column_value, separator_name):
    """
    Warnung für möglichen nicht atomaren Wert erstellen
    """

    quality_warning = {
        'warning_type': 'possible_non_atomic_value',
        'title': 'Möglicher nicht atomarer Wert',
        'row_number': row_number,
        'column_name': column_name,
        'column_value': column_value,
        'separator_name': separator_name,
        'recommendation': 'Auf Möglichkeit mehrerer Einzelwerte prüfen'
    }

    return quality_warning
