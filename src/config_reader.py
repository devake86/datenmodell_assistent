import json

def read_model_config(config_file_path):
    """
    JSON-Konfigurationsdatei einlesen
    Konfiguration als Dictionary zurückgeben
    """

    # JSON-Datei zum Lesen öffnen
    with open(config_file_path, mode='r', encoding='utf-8') as config_file:
        # JSON-Inhalt in Python-Dictionaries und Listen umwandeln
        model_config = json.load(config_file)

    return model_config
