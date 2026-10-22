"""
Regelwerk für Attributzuordnungen
"""
ATTRIBUTE_RULES = [
    # Unternehmens-, Kunden- und Lieferantendaten
    {
        'table_name': 'kunde',
        'target_name': 'kundennummer',
        'key_candidate': True,
        'alternative_names': [
            'kundennummer',
            'kundennr',
            'kundenid',
            'customerid',
            'customernumber',
            'customerno'
        ]
    },
    {
        'table_name': 'kunde',
        'target_name': 'firmenname',
        'key_candidate': False,
        'alternative_names': [
            'firmenname',
            'firma',
            'unternehmen',
            'unternehmensname',
            'kundenname',
            'company',
            'companyname'
        ]
    },
    {
        'table_name': 'kunde',
        'target_name': 'kundentyp',
        'key_candidate': False,
        'alternative_names': [
            'kundentyp',
            'kundenart',
            'customerclassification',
            'customertype'
        ]
    },
    {
        'table_name': 'kunde',
        'target_name': 'umsatz',
        'key_candidate': False,
        'alternative_names': [
            'umsatz',
            'jahresumsatz',
            'kundenumsatz',
            'revenue',
            'annualrevenue'
        ]
    },
    {
        'table_name': 'kunde',
        'target_name': 'vertragsbeginn',
        'key_candidate': False,
        'alternative_names': [
            'vertragsbeginn',
            'vertragsstart',
            'vertragsdatum',
            'contractstart',
            'contractdate'
        ]
    },
    {
        'table_name': 'kunde',
        'target_name': 'aktiv',
        'key_candidate': False,
        'alternative_names': [
            'aktiv',
            'istaktiv',
            'kundenaktiv',
            'active',
            'isactive'
        ]
    },
    {
        'table_name': 'kunde',
        'target_name': 'lieferantennummer',
        'key_candidate': True,
        'alternative_names': [
            'lieferantennummer',
            'lieferantennr',
            'lieferantenid',
            'supplierid',
            'suppliernumber'
        ]
    },

    # Ansprechpartner und Kontaktdaten
    {
        'table_name': 'ansprechpartner',
        'target_name': 'name',
        'key_candidate': False,
        'alternative_names': [
            'ansprechpartner',
            'kontaktperson',
            'kontaktname',
            'contactperson',
            'contactname'
        ]
    },
    {
        'table_name': 'ansprechpartner',
        'target_name': 'vorname',
        'key_candidate': False,
        'alternative_names': [
            'ansprechpartnervorname',
            'kontaktvorname',
            'contactfirstname'
        ]
    },
    {
        'table_name': 'ansprechpartner',
        'target_name': 'nachname',
        'key_candidate': False,
        'alternative_names': [
            'ansprechpartnernachname',
            'kontaktnachname',
            'contactlastname'
        ]
    },
    {
        'table_name': 'ansprechpartner',
        'target_name': 'email',
        'key_candidate': True,
        'alternative_names': [
            'email',
            'emailadresse',
            'mail',
            'mailadresse',
            'contactemail'
        ]
    },
    {
        'table_name': 'ansprechpartner',
        'target_name': 'telefon',
        'key_candidate': False,
        'alternative_names': [
            'telefon',
            'telefonnummer',
            'tel',
            'phone',
            'phonenumber'
        ]
    },
    {
        'table_name': 'ansprechpartner',
        'target_name': 'mobiltelefon',
        'key_candidate': False,
        'alternative_names': [
            'mobiltelefon',
            'mobilnummer',
            'handynummer',
            'handy',
            'mobile',
            'mobilephone'
        ]
    },
    {
        'table_name': 'ansprechpartner',
        'target_name': 'faxnummer',
        'key_candidate': False,
        'alternative_names': [
            'fax',
            'faxnummer',
            'faxnumber'
        ]
    },

    # Adressdaten
    {
        'table_name': 'adresse',
        'target_name': 'strasse',
        'key_candidate': False,
        'alternative_names': [
            'strasse',
            'strassenname',
            'street',
            'streetname'
        ]
    },
    {
        'table_name': 'adresse',
        'target_name': 'hausnummer',
        'key_candidate': False,
        'alternative_names': [
            'hausnummer',
            'hausnr',
            'housenumber',
            'streetnumber'
        ]
    },
    {
        'table_name': 'adresse',
        'target_name': 'plz',
        'key_candidate': False,
        'alternative_names': [
            'plz',
            'postleitzahl',
            'postalcode',
            'postcode',
            'zipcode'
        ]
    },
    {
        'table_name': 'adresse',
        'target_name': 'ort',
        'key_candidate': False,
        'alternative_names': [
            'ort',
            'stadt',
            'wohnort',
            'city',
            'town'
        ]
    },
    {
        'table_name': 'adresse',
        'target_name': 'land',
        'key_candidate': False,
        'alternative_names': [
            'land',
            'staat',
            'country'
        ]
    },

    # Mitarbeiterdaten
    {
        'table_name': 'mitarbeiter',
        'target_name': 'personalnummer',
        'key_candidate': True,
        'alternative_names': [
            'personalnummer',
            'personalnr',
            'mitarbeiternummer',
            'mitarbeiternr',
            'mitarbeiterid',
            'employeeid',
            'employeenumber'
        ]
    },
    {
        'table_name': 'mitarbeiter',
        'target_name': 'vorname',
        'key_candidate': False,
        'alternative_names': [
            'mitarbeitervorname',
            'personalvorname',
            'employeefirstname'
        ]
    },
    {
        'table_name': 'mitarbeiter',
        'target_name': 'nachname',
        'key_candidate': False,
        'alternative_names': [
            'mitarbeiternachname',
            'personalnachname',
            'employeelastname'
        ]
    },
    {
        'table_name': 'mitarbeiter',
        'target_name': 'eintrittsdatum',
        'key_candidate': False,
        'alternative_names': [
            'eintrittsdatum',
            'eintritt',
            'beschaeftigungsbeginn',
            'employmentstart',
            'startdate'
        ]
    },
    {
        'table_name': 'mitarbeiter',
        'target_name': 'austrittsdatum',
        'key_candidate': False,
        'alternative_names': [
            'austrittsdatum',
            'austritt',
            'beschaeftigungsende',
            'employmentend',
            'enddate'
        ]
    },
    {
        'table_name': 'mitarbeiter',
        'target_name': 'gehalt',
        'key_candidate': False,
        'alternative_names': [
            'gehalt',
            'bruttogehalt',
            'monatsgehalt',
            'salary'
        ]
    },

    # Abteilungsdaten
    {
        'table_name': 'abteilung',
        'target_name': 'abteilungsnummer',
        'key_candidate': True,
        'alternative_names': [
            'abteilungsnummer',
            'abteilungsnr',
            'abteilungsid',
            'departmentid',
            'departmentnumber'
        ]
    },
    {
        'table_name': 'abteilung',
        'target_name': 'bezeichnung',
        'key_candidate': False,
        'alternative_names': [
            'abteilungsname',
            'abteilungsbezeichnung',
            'department',
            'departmentname'
        ]
    },

    # Produkt- und Artikeldaten
    {
        'table_name': 'produkt',
        'target_name': 'artikelnummer',
        'key_candidate': True,
        'alternative_names': [
            'artikelnummer',
            'artikelnr',
            'artikelid',
            'produktnummer',
            'produktnr',
            'produktid',
            'productid',
            'productnumber',
            'sku'
        ]
    },
    {
        'table_name': 'produkt',
        'target_name': 'bezeichnung',
        'key_candidate': False,
        'alternative_names': [
            'artikelbezeichnung',
            'produktbezeichnung',
            'produktname',
            'productname'
        ]
    },
    {
        'table_name': 'produkt',
        'target_name': 'preis',
        'key_candidate': False,
        'alternative_names': [
            'preis',
            'verkaufspreis',
            'einzelpreis',
            'unitprice',
            'price'
        ]
    },
    {
        'table_name': 'produkt',
        'target_name': 'bestand',
        'key_candidate': False,
        'alternative_names': [
            'bestand',
            'lagerbestand',
            'mengebestand',
            'stock',
            'stockquantity'
        ]
    },

    # Auftragsdaten
    {
        'table_name': 'auftrag',
        'target_name': 'auftragsnummer',
        'key_candidate': True,
        'alternative_names': [
            'auftragsnummer',
            'auftragsnr',
            'auftragid',
            'orderid',
            'ordernumber'
        ]
    },
    {
        'table_name': 'auftrag',
        'target_name': 'auftragsdatum',
        'key_candidate': False,
        'alternative_names': [
            'auftragsdatum',
            'bestelldatum',
            'orderdate'
        ]
    },
    {
        'table_name': 'auftrag',
        'target_name': 'gesamtbetrag',
        'key_candidate': False,
        'alternative_names': [
            'auftragswert',
            'gesamtbetrag',
            'bestellwert',
            'ordertotal',
            'totalamount'
        ]
    },

    # Rechnungsdaten
    {
        'table_name': 'rechnung',
        'target_name': 'rechnungsnummer',
        'key_candidate': True,
        'alternative_names': [
            'rechnungsnummer',
            'rechnungsnr',
            'rechnungid',
            'invoiceid',
            'invoicenumber'
        ]
    },
    {
        'table_name': 'rechnung',
        'target_name': 'rechnungsdatum',
        'key_candidate': False,
        'alternative_names': [
            'rechnungsdatum',
            'invoicedate'
        ]
    },
    {
        'table_name': 'rechnung',
        'target_name': 'rechnungsbetrag',
        'key_candidate': False,
        'alternative_names': [
            'rechnungsbetrag',
            'bruttobetrag',
            'invoiceamount'
        ]
    },

    # Vertragsdaten
    {
        'table_name': 'vertrag',
        'target_name': 'vertragsnummer',
        'key_candidate': True,
        'alternative_names': [
            'vertragsnummer',
            'vertragsnr',
            'vertragid',
            'contractid',
            'contractnumber'
        ]
    },
    {
        'table_name': 'vertrag',
        'target_name': 'beginn',
        'key_candidate': False,
        'alternative_names': [
            'vertragslaufzeitbeginn',
            'laufzeitbeginn',
            'contractbegin'
        ]
    },
    {
        'table_name': 'vertrag',
        'target_name': 'ende',
        'key_candidate': False,
        'alternative_names': [
            'vertragslaufzeitende',
            'laufzeitende',
            'contractend'
        ]
    }
]

RELATIONSHIP_RULES = [
    {
        'parent_table': 'kunde',
        'child_table': 'ansprechpartner',
        'foreign_key': 'kunde_id',
        'cardinality': '1:n'
    },
    {
        'parent_table': 'kunde',
        'child_table': 'adresse',
        'foreign_key': 'kunde_id',
        'cardinality': '1:n'
    },
    {
        'parent_table': 'abteilung',
        'child_table': 'mitarbeiter',
        'foreign_key': 'abteilung_id',
        'cardinality': '1:n'
    },
    {
        'parent_table': 'kunde',
        'child_table': 'auftrag',
        'foreign_key': 'kunde_id',
        'cardinality': '1:n'
    },
    {
        'parent_table': 'kunde',
        'child_table': 'rechnung',
        'foreign_key': 'kunde_id',
        'cardinality': '1:n'
    },
    {
        'parent_table': 'kunde',
        'child_table': 'vertrag',
        'foreign_key': 'kunde_id',
        'cardinality': '1:n'
    },
    {
        'parent_table': 'auftrag',
        'child_table': 'rechnung',
        'foreign_key': 'auftrag_id',
        'cardinality': '1:n'
    }
]

def recognize_columns(normalized_columns):
    """
    Normalisierte CSV-Spaltennamen mit Regelwerk vergleichen
    Erkannte und nicht erkannte Spalten als jeweils eine
    eigene Liste von Dictionaries zurückgeben
    """

    recognized_columns = []
    unrecognized_columns = []

    for normalized_column in normalized_columns:
        matching_attribute_rule = find_attribute_rule(normalized_column['normalized_name'])

        if matching_attribute_rule is None:
            unrecognized_column = {
                'original_name': normalized_column['original_name'],
                'normalized_name': normalized_column['normalized_name']
            }

            unrecognized_columns.append(unrecognized_column)
            continue

        recognized_column = {
            'original_name': normalized_column['original_name'],
            'normalized_name': normalized_column['normalized_name'],
            'table_name': matching_attribute_rule['table_name'],
            'target_name': matching_attribute_rule['target_name'],
            'key_candidate': matching_attribute_rule['key_candidate'],
        }

        recognized_columns.append(recognized_column)

    return recognized_columns, unrecognized_columns

def find_attribute_rule(normalized_column_name):
    """
    Im Regelwerk nach einer passenden alternativen
    Bezeichnung für den normalisierten Spaltennamen suchen
    Gefundene Attributregel oder None zurückgeben
    """

    for attribute_rule in ATTRIBUTE_RULES:
        alternative_names = attribute_rule['alternative_names']

        if normalized_column_name in alternative_names:
            return attribute_rule

    return None

def create_dynamic_table_assignments(recognized_columns, unrecognized_columns):
    """
    Erkannte Spalten nach vorgeschlagenen Zieltabellen gruppieren
    Nicht erkannte Spalten der Auffangtabelle nicht_zugeordnet zuweisen
    """

    dynamic_table_assignments = []

    for recognized_column in recognized_columns:
        table_name = recognized_column['table_name']

        table_assignment = find_table_assignment(dynamic_table_assignments, table_name)

        # Wenn passendes Tabellen-Dictionary zum aktuellen Attribut in CSV-Datei
        # noch nicht in dynamic_table_assignments Liste
        # entsprechendes Tabellen-Dictionary erzeugen und der Liste hinzufügen
        # Tabellen-Dictionaries sollen nur erzeugt werden, wenn mindestens
        # ein zuordnungsbares Attribut in der CSV-Datei gefunden wurde
        if table_assignment is None:
            table_assignment = create_table_assignment(table_name)

            dynamic_table_assignments.append(table_assignment)

        attribute_assignment = create_recognized_attribute_assignment(recognized_column)

        table_assignment['attributes'].append(attribute_assignment)

    # Nicht erkannte Spalten zuweisen
    if len(unrecognized_columns) > 0:
        unrecognized_table_assignment = create_table_assignment('nicht_zugeordnet', 'review')

        for unrecognized_column in unrecognized_columns:
            attribute_assignment = create_unrecognized_attribute_assignment(unrecognized_column)

            unrecognized_table_assignment['attributes'].append(attribute_assignment)

        dynamic_table_assignments.append(unrecognized_table_assignment)

    return dynamic_table_assignments

def find_table_assignment(dynamic_table_assignments, table_name):
    """
    Bereits erstellte Tabellenzuordnung anhand des Tabellennamens suchen
    Wenn die Tabelle noch nicht vorhanden ist, None zurückgeben
    """

    for table_assignment in dynamic_table_assignments:
        if table_assignment['name'] == table_name:
            return table_assignment

    return None

def create_table_assignment(table_name, table_type='entity'):
    """
    Neue Tabellenzuordnung mit leerer Attributsliste erstellen
    """

    table_assignment = {
        'name': table_name,
        'table_type': table_type,
        'attributes': []
    }

    return table_assignment

def create_recognized_attribute_assignment(recognized_column):
    """
    Attributszuordnung aus erkannter regelbasierter CSV-Spalte erstellen
    """

    attribute_assignment = {
        'source_column': recognized_column['original_name'],
        'target_name': recognized_column['target_name'],
        'key_candidate': recognized_column['key_candidate'],
        'assignment_status': 'recognized'
    }

    return attribute_assignment

def create_unrecognized_attribute_assignment(unrecognized_column):
    """
    Vorläufige Attributszuordnung für unbekannte CSV-Spalte erstellen
    """

    attribute_assignment = {
        'source_column': unrecognized_column['original_name'],
        'target_name': unrecognized_column['normalized_name'],
        'key_candidate': False,
        'assignment_status': 'unrecognized'
    }

    return attribute_assignment

def generate_model_config(csv_file_path, dynamic_table_assignments):
    """
    Erzeugung einer Datenmodellkonfiguration aus den dynamischen Tabellenzuordnungen
    In die Datenmodellkonfiguration werden nur Beziehungen aufgenommen,
    für die die entsprechenden Tabellen vorhanden sind
    """

    generated_relationships = create_dynamic_relationships(dynamic_table_assignments)

    generated_model_config = {
        'source': {
            'file': csv_file_path,
            'delimiter': ';',
            'encoding': 'utf-8'
        },
        'database': {
            'dialect': 'mysql',
            'default_primary_key': {
                'name': 'id',
                'data_type': 'INT',
                'auto_increment': True
            }
        },
        'tables': dynamic_table_assignments,
        'relationships': generated_relationships
    }

    return generated_model_config

def get_existing_table_names(dynamic_table_assignments):
    """
    Namen aller dynamisch erzeugten Tabellen als Liste zurückgeben
    """

    existing_table_names = []

    for table_assignment in dynamic_table_assignments:
        existing_table_names.append(table_assignment['name'])

    return existing_table_names

def create_dynamic_relationships(dynamic_table_assignments):
    """
    Bekannte 1:n-Beziehungen zwischen vorhandenen Tabellen erzeugen
    Beziehungen nur aufnehmen, wenn sowohl übergeordnete als auch
    untergeordnete Tabellen vorhanden sind
    """

    dynamic_relationships = []

    existing_table_names = get_existing_table_names(dynamic_table_assignments)

    for relationship_rule in RELATIONSHIP_RULES:
        parent_table_name = relationship_rule['parent_table']
        child_table_name = relationship_rule['child_table']

        parent_table_exists = parent_table_name in existing_table_names
        child_table_exists = child_table_name in existing_table_names

        if parent_table_exists and child_table_exists:
            dynamic_relationship = {
                'parent_table': parent_table_name,
                'child_table': child_table_name,
                'foreign_key': relationship_rule['foreign_key'],
                'cardinality': relationship_rule['cardinality']
            }

            dynamic_relationships.append(dynamic_relationship)

    return dynamic_relationships

# Tests auf doppelte Alternativbezeichnungen im Regelwerk
# if __name__ == '__main__':
#     used_alternative_names = []
#     duplicate_alternative_names = []
#
#     for attribute_rule in ATTRIBUTE_RULES:
#         alternative_names = attribute_rule['alternative_names']
#
#         # Sicherstellen, dass die Alternativbezeichnungen als Liste vorliegen
#         if not isinstance(alternative_names, list):
#             continue
#
#         for alternative_name in alternative_names:
#             if alternative_name in used_alternative_names:
#                 duplicate_alternative_names.append(alternative_name)
#             else:
#                 used_alternative_names.append(alternative_name)
#
#     if len(duplicate_alternative_names) == 0:
#         print('Keine doppelten Alternativbezeichnungen gefunden.')
#     else:
#         for duplicate_alternative_name in duplicate_alternative_names:
#             print(f"Doppelte Alternativbezeichnung: {duplicate_alternative_name}")
