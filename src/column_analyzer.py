from src.type_detector import suggest_sql_data_type

def analyze_columns(data_records, column_names):
    """
    Werte aller CSV-Spalten analysieren
    Für jede Spalte Anzahl gefüllter, leerer, eindeutiger,
    mehrfach vorkommender Werte und maximale Zeichenlänge ermitteln
    Ergebnisse als Liste von Dictionaries zurückgeben
    """

    # Liste aller Spaltenanalysen
    column_analyses = []

    for column_name in column_names:
        column_values = []

        # Alle Werte der aktuellen Spalte in Liste sammeln
        for data_record in data_records:
            column_value = data_record[column_name]
            column_values.append(column_value)

        # Einzelspaltenanalyse als Dictionary
        column_analysis = analyze_column_values(column_name, column_values)

        column_analyses.append(column_analysis)

    return column_analyses

def analyze_column_values(column_name, column_values):
    """
    Werte einzelner CSV-Spalten analysieren
    Leere Werte bei der Bestimmung eindeutiger und
    mehrfach vorkommender Werte nicht berücksichtigen
    """

    record_count = len(column_values)
    filled_values = []
    empty_value_count = 0
    maximum_length = 0

    for column_value in column_values:
        # Behandlung leerer Werte
        if column_value is None or column_value.strip() == '':
            empty_value_count += 1
            continue

        filled_values.append(column_value)

        # Länge des aktuellen Wertes
        current_value_length = len(column_value)

        # Maximale Zeichenlänge bestimmen
        if current_value_length > maximum_length:
            maximum_length = current_value_length

    filled_value_count = len(filled_values)

    # Set um Werte einmalig zu machen
    unique_values = set(filled_values)
    unique_value_count = len(unique_values)

    # Anzahl Duplikate berechnen
    duplicate_value_count = filled_value_count - unique_value_count

    # SQL-Datentyp vorschlagen
    suggested_sql_data_type = suggest_sql_data_type(column_name, column_values)

    # Einzelspaltenanalyse Dictionary befüllen
    column_analysis = {
        'column_name': column_name,
        'record_count': record_count,
        'filled_value_count': filled_value_count,
        'empty_value_count': empty_value_count,
        'unique_value_count': unique_value_count,
        'duplicate_value_count': duplicate_value_count,
        'maximum_length': maximum_length,
        'suggested_sql_data_type': suggested_sql_data_type
    }

    return column_analysis
