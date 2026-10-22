def normalize_column_name(column_name):
    """
    Normalisierung eines Spaltennamens für spätere
    Vergleiche mit dem Regelwerk ohne Veränderung
    des ursprünglichen Spaltennamens
    """

    normalized_column_name = column_name.strip().lower()

    # Umlaute und Eszett vereinheitlichen
    character_replacements = {
        'ä': 'ae',
        'ö': 'oe',
        'ü': 'ue',
        'ß': 'ss'
    }

    for original_character in character_replacements:
        replacement_character = character_replacements[original_character]
        normalized_column_name = normalized_column_name.replace(original_character, replacement_character)

    cleaned_column_name = ''

    # Nur Buchstaben und Ziffern
    for character in normalized_column_name:
        # .isalnum() prüft, ob das Zeichen ein Buchstabe oder eine Ziffer ist
        if character.isalnum():
            cleaned_column_name += character

    return cleaned_column_name

def create_normalized_column_names(column_names):
    """
    Zuordnung aus ursprünglichen und normalisierten
    Spaltennamen für alle CSV-Spalten als Liste
    von Dictionaries zurückgeben
    """

    normalized_columns = []

    for column_name in column_names:
        normalized_column_name = normalize_column_name(column_name)

        normalized_column = {
            'original_name': column_name,
            'normalized_name': normalized_column_name
        }

        normalized_columns.append(normalized_column)

    return normalized_columns

# Tests für die Normalisierung
# if __name__ == '__main__':
#     print(normalize_column_name('Kundennummer'))
#     print(normalize_column_name('Kunden-Nummer'))
#     print(normalize_column_name('Kunden_Nr.'))
#     print(normalize_column_name('E-Mail'))
#     print(normalize_column_name('e_mail'))
#     print(normalize_column_name('Straße'))
#     print(normalize_column_name('Geschäftsbereich 2'))
