from src.csv_reader import read_csv_records
from src.column_analyzer import analyze_columns
from src.quality_checker import find_possible_non_atomic_values, find_missing_information_values
from src.config_reader import read_model_config
from src.attribute_mapper import map_column_analyses_to_tables
from src.model_generator import generate_physical_model
from src.report_writer import create_physical_model_text, create_analysis_report_text, write_text_file

def main():
    """
    CSV-Quelldatei einlesen
    JSON-Datenmodellkonfiguration einlesen
    CSV-Spalten analysieren
    Analysen den Konfigurationstabellen zuordnen
    Vorschlag für physisches Datenmodell erzeugen
    Datenqualität überprüfen
    Ausgabe von Informationen
    """

    csv_file_path = 'data/customer_data.csv'
    config_file_path = 'config/model_config.json'

    physical_model_file_path = 'output/physical_model.txt'
    analysis_report_file_path = 'output/analysis_report.txt'

    # Datensatz- und Spaltennamenliste aus CSV-Datei holen
    data_records, column_names = read_csv_records(csv_file_path)

    # Konfiguration für den Datenmodellvorschlag laden
    model_config = read_model_config(config_file_path)

    # Analyse aller CSV-Spalten
    column_analyses = analyze_columns(data_records, column_names)

    # Spaltenanalysen den Tabellen zuordnen
    mapped_tables = map_column_analyses_to_tables(column_analyses, model_config)

    # Vorschlag für physisches Datenmodell erzeugen
    physical_model, model_warnings = generate_physical_model(mapped_tables, model_config)

    # Mögliche nicht atomare Werte suchen
    quality_warnings = find_possible_non_atomic_values(data_records)

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
        model_warnings,
    )

    # Ausgabedateien schreiben und gegebenenfalls überschreiben
    write_text_file(physical_model_file_path, physical_model_text)
    write_text_file(analysis_report_file_path, analysis_report_text)

    # Konsolenausgabe
    print('=' * 80)
    print('DATENMODELL ASSISTENT')
    print('=' * 80)
    print()
    print(f"Quelldatei: {csv_file_path}")
    print(f"SQL-Dialekt: {physical_model["database_dialect"]}")
    print()
    print(f"{len(data_records)} Datensätze eingelesen.")
    print(f"{len(column_names)} Spalten analysiert.")
    print(f"{len(physical_model['tables'])} Tabellen für den Datenmodellvorschlag erzeugt.")

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

    if len(model_warnings) == 1:
        print('1 Datenmodellwarnung gefunden.')
    else:
        print(f"{len(model_warnings)} Datenmodellwarnungen gefunden.")

    print()
    print('AUSGABEDATEIEN')
    print('=' * 80)
    print(f"- {physical_model_file_path}")
    print(f"- {analysis_report_file_path}")
    print()
    print('Alle Vorschläge und Warnungen müssen geprüft werden.')

if __name__ == '__main__':
    main()
 