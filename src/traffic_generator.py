import time
from utils import read_domains_from_dataset
from dns_cache import handle_dns_request

# Generador de tráfico secuencial
def generate_traffic(domains, rate=10):
    """
    Genera tráfico secuencialmente para los dominios proporcionados.
    Parámetros:
    - domains: lista de dominios.
    - rate: tasa de solicitudes por segundo.
    """
    total_domains = len(domains)
    index = 0
    
    while True:
        domain = domains[index]  # Toma el dominio secuencialmente
        handle_dns_request(domain)  # Llama a la función que gestiona el caché y el DNS
        
        # Mover al siguiente dominio
        index += 1
        if index >= total_domains:
            index = 0  # Vuelve al principio si llega al final
        
        time.sleep(1 / rate)  # Controla la tasa de solicitudes (10 por segundo en este caso)

# Simulación
if __name__ == "__main__":
    dataset_file = 'dataset.csv'
    domains = read_domains_from_dataset(dataset_file, limit=100000)
    generate_traffic(domains, rate=10)
