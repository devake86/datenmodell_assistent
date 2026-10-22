from datetime import datetime
from decimal import Decimal, InvalidOperation

def is_missing_information(column_value):
    """
    Prüfung auf fehlende oder unbekannte
    Information eines Werts
    """

    if column_value is None:
        return True

    normalized_value = column_value.strip().lower()

    missing_information_values = [
        '',
        'unbekannt',
        'nicht bekannt',
        'k. a.',
        'k.a.',
        'n/a'
    ]

    return normalized_value in missing_information_values

def suggest_sql_data_type(column_name, column_values):
    """
    SQL-Datentyp anhand enthaltener Werte einer Spalte vorschlagen
    SQL-Datentyp ist nur ein Vorschlag und sollte vor der Verwendung
    in einer Datenbank entsprechend geprüft werden
    """

    filled_values = []

    for column_value in column_values:
        # Fehlende oder unbekannte Informationen bei automatischer Datentyperkennung nicht berücksichtigen
        if is_missing_information(column_value):
            continue

        filled_values.append(column_value.strip())

    # Datentyp für leere Spalte
    if len(filled_values) == 0:
        return 'VARCHAR(10)'

    # Wenn die Spalte einen Textdatentyp benötigt, schlage VARCHAR oder TEXT vor
    if requires_text_data_type(column_name):
        return suggest_varchar_or_text_data_type(filled_values)

    if contains_only_boolean_values(filled_values):
        return 'BOOLEAN'

    if contains_only_integer_values(filled_values):
        return 'INT'

    if contains_only_decimal_values(filled_values):
        return 'DECIMAL(10,2)'

    if contains_only_date_values(filled_values):
        return 'DATE'

    return suggest_varchar_or_text_data_type(filled_values)

def requires_text_data_type(column_name):
    """
    Prüfung auf Grund von bestimmten Spaltennamen
    ob Werte als Zeichenketten behandelt werden sollen
    """

    normalized_column_name = column_name.lower()

    # Keyword Liste
    text_column_keywords = [
        'nummer',
        'telefon',
        'plz',
        'postleitzahl'
    ]

    for text_column_keyword in text_column_keywords:
        if text_column_keyword in normalized_column_name:
            return True

    return False

def contains_only_boolean_values(column_values):
    """
    Prüfung auf Wahrheitswerte
    """

    accepted_boolean_values = [
        'ja',
        'nein',
        'true',
        'false',
        '1',
        '0',
    ]

    for column_value in column_values:
        normalized_value = column_value.lower()

        if normalized_value not in accepted_boolean_values:
            return False

    return True

def contains_only_integer_values(column_values):
    """
    Prüfung auf Ganzzahlen
    """

    for column_value in column_values:
        try:
            int(column_value)
        except ValueError:
            return False

    return True

def contains_only_decimal_values(column_values):
    """
     Prüfung auf Dezimalzahlen
    """

    for column_value in column_values:
        normalized_value = column_value.replace(',', '.')

        try:
            Decimal(normalized_value)
        except InvalidOperation:
            return False

    return True

def contains_only_date_values(column_values):
    """
    Prüfung auf Datumsformat YYYY-MM-DD
    """

    for column_value in column_values:
        try:
            datetime.strptime(column_value, '%Y-%m-%d')
        except ValueError:
            return False

    return True

def suggest_varchar_or_text_data_type(column_values):
    """
    Je nach Länge des Werts eine bestimmte VARCHAR-Länge bis 255
    oder TEXT Datentyp wenn über 255 vorschlagen
    """

    maximum_length = 0

    for column_value in column_values:
        current_value_length = len(column_value)

        if current_value_length > maximum_length:
            maximum_length = current_value_length

    if maximum_length <= 10:
        return 'VARCHAR(10)'

    if maximum_length <= 20:
        return 'VARCHAR(20)'

    if maximum_length <= 50:
        return 'VARCHAR(50)'

    if maximum_length <= 100:
        return 'VARCHAR(100)'

    if maximum_length <= 255:
        return 'VARCHAR(255)'

    return 'TEXT'

# Datentyp Check Tests
# if __name__ == '__main__':
#     print(suggest_sql_data_type('Anzahl', ['10', '20', '30']))
#     print(suggest_sql_data_type('Preis', ['10.50', '20.25']))
#     print(suggest_sql_data_type('Datum', ['2025-01-01', '2025-02-01']))
#     print(suggest_sql_data_type('Aktiv', ['Ja', 'Nein', '1']))
#     print(suggest_sql_data_type('PLZ', ['01234', '76669']))
#     print(suggest_sql_data_type('Umsatz', ['12500.50', '8400.00', 'unbekannt']))
#     print(suggest_sql_data_type('Vertragsbeginn', ['2024-02-15', '2025-01-10', 'nicht bekannt']))
