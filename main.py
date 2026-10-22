from src.csv_reader import read_csv_records
from src.column_analyzer import analyze_columns
from src.quality_checker import find_possible_non_atomic_values, find_missing_information_values, find_possible_many_to_many_relationships
from src.attribute_mapper import map_column_analyses_to_tables
from src.model_generator import generate_physical_model
from src.report_writer import create_physical_model_text, create_analysis_report_text, write_text_file
from src.file_selector import select_csv_file
from src.column_name_normalizer import create_normalized_column_names
# from src.config_reader import read_model_config
from src.config_generator import recognize_columns, create_dynamic_table_assignments, generate_model_config
from src.config_writer import write_model_config

def main():
    """
    CSV-Quelldatei einlesen
    # JSON-Datenmodellkonfiguration einlesen
    Ausgabe Konsolenheader
    CSV-Auswahlmenü
    CSV-spezifische Pfade für Ausgabedateien erstellen
    Spaltennamen normalisieren
    Normalisierte Spaltennamen mit Regelwerk vergleichen
    Dynamische Tabellenzuordnung der Attribute erzeugen
    # Konfiguration für den Datenmodellvorschlag laden
    Dynamische Datenmodellkonfiguration aus erkannten Tabellen und Attributen erzeugen
    Spalten und Mehrfachwerte auf mögliche n:m-Beziehungen prüfen
    CSV-Spalten analysieren
    Analysen den Konfigurationstabellen zuordnen
    Vorschlag für physisches Datenmodell erzeugen
    Datenqualität überprüfen
    Dynamisch erzeugte Datenmodellkonfiguration zusätzlich als JSON speichern
    Ausgabe von Informationen
    """

    data_directory_path = 'data'
    # config_file_path = 'config/model_config.json'

    # Ausgabe Konsolenheader
    print('=' * 80)
    print('DATENMODELL ASSISTENT')
    print('=' * 80)
    print()

    # CSV-Datei über Konsolenmenü auswählen
    csv_file_path, csv_base_name = select_csv_file(data_directory_path)

    # CSV-spezifische Pfade für Ausgabedateien erstellen
    generated_config_file_path = f"config/generated/{csv_base_name}_model_config.json"
    physical_model_file_path = f"output/{csv_base_name}_physical_model.txt"
    analysis_report_file_path = f"output/{csv_base_name}_analysis_report.txt"

    # Datensatz- und Spaltennamenliste aus CSV-Datei holen
    data_records, column_names = read_csv_records(csv_file_path)

    # Spaltennamen für spätere Vergleiche normalisieren
    normalized_columns = create_normalized_column_names(column_names)

    # Normalisierte Spaltennamen mit dem Regelwerk vergleichen
    recognized_columns, unrecognized_columns = recognize_columns(normalized_columns)

    # Dynamische Tabellenzuordnung für erkannte und unbekannte Attribute
    dynamic_table_assignments = create_dynamic_table_assignments(recognized_columns, unrecognized_columns)

    # Konfiguration für den Datenmodellvorschlag laden
    # model_config = read_model_config(config_file_path)

    # Dynamische Datenmodellkonfiguration aus erkannten Tabellen und Attributen erzeugen
    generated_model_config = generate_model_config(csv_file_path, dynamic_table_assignments)

    # Spalten und Mehrfachwerte auf mögliche n:m-Beziehungen prüfen
    many_to_many_warnings = find_possible_many_to_many_relationships(data_records, normalized_columns, dynamic_table_assignments)

    # Analyse aller CSV-Spalten
    column_analyses = analyze_columns(data_records, column_names)

    # Spaltenanalysen den Tabellen zuordnen
    mapped_tables = map_column_analyses_to_tables(column_analyses, generated_model_config)

    # Vorschlag für physisches Datenmodell erzeugen
    physical_model, model_warnings = generate_physical_model(mapped_tables, generated_model_config)

    # Mögliche nicht atomare Werte suchen
    quality_warnings = find_possible_non_atomic_values(data_records, recognized_columns)

    # Fehlende oder unbekannte Informationen suchen
    missing_information_warnings = find_missing_information_values(data_records, column_names)

    # Textdarstellung des vorgeschlagenen physischen Datenmodells erzeugen
    physical_model_text = create_physical_model_text(physical_model)

    # Textdarstellung der Datenanalyse und alle gefundenen Warnungen erzeugen
    analysis_report_text = create_analysis_report_text(
        csv_file_path,
        data_records,
        column_analyses,
        quality_warnings,
        missing_information_warnings,
        unrecognized_columns,
        many_to_many_warnings,
        model_warnings
    )

    # Dynamisch erzeugte Datenmodellkonfiguration zusätzlich als JSON speichern
    write_model_config(generated_config_file_path, generated_model_config)

    # Ausgabedateien schreiben und gegebenenfalls überschreiben
    write_text_file(physical_model_file_path, physical_model_text)
    write_text_file(analysis_report_file_path, analysis_report_text)

    # Konsolenausgabe
    print()
    print(f'Quelldatei: {csv_file_path}')
    print(f"SQL-Dialekt: {generated_model_config['database']['dialect']}")
    print()
    print(f"{len(data_records)} Datensätze eingelesen.")
    print(f"{len(column_names)} Spalten analysiert.")
    print(f"{len(generated_model_config['tables'])} Tabellen für den Datenmodellvorschlag erzeugt.")
    print(f"{len(generated_model_config['relationships'])} 1:n-Beziehungen vorgeschlagen.")

    print()
    print('DATENQUALITÄT')
    print('=' * 80)

    if len(quality_warnings) == 1:
        print('1 möglicherweise nicht atomarer Wert gefunden.')
    else:
        print(f"{len(quality_warnings)} möglicherweise nicht atomare Werte gefunden.")

    if len(missing_information_warnings) == 1:
        print('1 fehlende oder unbekannte Information gefunden.')
    else:
        print(f"{len(missing_information_warnings)} fehlende oder unbekannte Informationen gefunden.")

    if len(unrecognized_columns) == 1:
        print('1 Spalte konnte nicht automatisch zugeordnet werden.')
    else:
        print(f"{len(unrecognized_columns)} Spalten konnten nicht automatisch zugeordnet werden.")

    if len(many_to_many_warnings) == 1:
        print('1 mögliche n:m-Beziehung gefunden.')
    else:
        print(f"{len(many_to_many_warnings)} mögliche n:m-Beziehungen gefunden.")

    if len(model_warnings) == 1:
        print('1 Datenmodellwarnung gefunden.')
    else:
        print(f"{len(model_warnings)} Datenmodellwarnungen gefunden.")

    print()
    print('AUSGABEDATEIEN')
    print('=' * 80)
    print(f'- {generated_config_file_path}')
    print(f'- {physical_model_file_path}')
    print(f'- {analysis_report_file_path}')
    print()
    print('Alle Zuordnungen, Vorschläge und Warnungen müssen geprüft werden.')

if __name__ == '__main__':
    main()
