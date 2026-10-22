import csv

def read_csv_records(csv_file_path):
    """
    CSV-Datei einlesen
    Spaltennamen und Datensätze zurückgeben
    Datensätze mit Spaltennamen als Schlüssel in Dictionary speichern
    """

    data_records = []

    # newline='' Zeilenumbrüche werden durch CSV-Modul verarbeitet
    with open(csv_file_path, mode='r', encoding='utf-8', newline='') as csv_file:
        # DictReader verwendet die Werte der CSV-Kopfzeile als Schlüssel
        csv_reader = csv.DictReader(csv_file, delimiter=';')

        # fieldnames enthält CSV-Kopfzeile als Liste
        column_names = csv_reader.fieldnames

        for data_record in csv_reader:
            data_records.append(data_record)

    return data_records, column_names
