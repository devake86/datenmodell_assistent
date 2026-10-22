import json
from pathlib import Path

def write_model_config(config_file_path, generated_model_config):
    """
    Dynamisch erzeugte Datenmodellkonfiguration als formatierte JSON-Datei speichern
    Bereits vorhandene Dateien werden überschrieben
    """

    config_path = Path(config_file_path)

    # Erstelle bei Bedarf übergeordnetes Verzeichnis automatisch mit
    # (allen nötigen Überverzeichnisse, und ohne Fehler bei bereits bestehendem Verzeichnis)
    config_path.parent.mkdir(parents=True, exist_ok=True)

    with open(config_path, mode='w', encoding='utf-8') as config_file:
        # Speichere in einer JSON-Datei
        # (das Python-Dictionary, in der geöffneten Zieldatei, mit lesbaren Umlauten, mit zwei Leerzeichen Einrückung)
        json.dump(generated_model_config, config_file, ensure_ascii=False, indent=2)
        # Zeilenumbruch am Dateiende für saubere Git-Darstellung ergänzen
        config_file.write('\n')
