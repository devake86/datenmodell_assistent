import csv

def read_csv_records(csv_file_path):
    """
    CSV-Datei einlesen
    Spaltennamen und Datensätze zurückgeben
    Datensätze mit den Spaltennamen als Schlüssel in Dictionaries speichern
    """

    data_records = []

    # newline='' überlässt die Verarbeitung der Zeilenumbrüche dem CSV-Modul
    with open(csv_file_path, mode='r', encoding='utf-8', newline='') as csv_file:
        # DictReader verwendet die Werte der CSV-Kopfzeile als Schlüssel
        csv_reader = csv.DictReader(csv_file, delimiter=';')

        # fieldnames enthält CSV-Kopfzeile als Liste
        column_names = csv_reader.fieldnames

        # Ohne Kopfzeile können keine Spalten und Datensätze zugeordnet werden
        if column_names is None:
            raise ValueError('Die CSV-Datei enthält keine Kopfzeile.')

        for data_record in csv_reader:
            data_records.append(data_record)

    return data_records, column_names
