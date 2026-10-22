from pathlib import Path

def select_csv_file(data_directory_path):
    """
    Alle CSV-Dateien im Verzeichnis suchen
    und als nummeriertes Auswahlmenü anzeigen
    Pfad der CSV-Datei und Dateiname ohne Dateiendung zurückgeben
    """

    # Path() Pfadobjekt erstellen
    data_directory = Path(data_directory_path)

    # Prüfen, ob das angegebene Datenverzeichnis vorhanden ist
    if not data_directory.exists():
        raise FileNotFoundError(f"Das Datenverzeichnis '{data_directory_path}' wurde nicht gefunden.")

    # Alle CSV-Dateien suchen und alphabetisch sortieren
    # glob() liefert ein durchlaufbares Ergebnis
    # sorted() liest das Ergebnis ein und gibt eine sortierte Liste zurück
    csv_file_paths = sorted(data_directory.glob('*.csv'))

    # Behandlung, wenn keine CSV-Dateien vorhanden sind
    if len(csv_file_paths) == 0:
        raise FileNotFoundError(f"Keine CSV-Datei im Verzeichnis '{data_directory_path}' gefunden.")

    print('VERFÜGBARE CSV-DATEIEN')
    print('=' * 80)

    # Auswahlmenü mit Auswahlnummer und Dateinamen
    for file_number, csv_file_path in enumerate(csv_file_paths, start=1):
        # .name um nur den Dateinamen ohne Pfad zu erhalten
        print(f"{file_number}: {csv_file_path.name}")

    print()

    while True:
        selected_file_input = input('CSV-Datei auswählen: ')

        try:
            selected_file_number = int(selected_file_input)
        except ValueError:
            print('Ungültige Eingabe. Bitte eine Zahl eingeben.')
            continue

        if selected_file_number < 1 or selected_file_number > len(csv_file_paths):
            print(f"Bitte eine Zahl zwischen 1 und {len(csv_file_paths)} eingeben.")
            continue

        # Auswahl an Listenindex anpassen
        selected_csv_file_path = csv_file_paths[selected_file_number - 1]

        # .stem gibt den Dateinamen ohne Dateiendung zurück
        csv_base_name = selected_csv_file_path.stem

        return str(selected_csv_file_path), csv_base_name
