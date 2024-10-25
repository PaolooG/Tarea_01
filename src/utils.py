import csv

def read_domains_from_dataset(file_path, limit=100000):
    """
    Lee un archivo CSV y devuelve una lista con los dominios.
    Parámetros:
    - file_path: ruta del archivo CSV.
    - limit: número máximo de dominios a leer.
    """
    domains = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)  # Usar csv.reader para tratar el archivo por índice
        next(reader, None)  # Saltar la cabecera si existe
        for i, row in enumerate(reader):
            if i >= limit:
                break
            domains.append(row[0])  # Asume que los dominios están en la primera columna
    return domains
