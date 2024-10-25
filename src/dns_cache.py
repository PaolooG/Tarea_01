import redis
import subprocess

# Conexión a Redis
r = redis.Redis(host='localhost', port=6379, db=0)

def query_dns(domain):
    """
    Realiza una consulta DNS para el dominio dado usando el comando DIG.
    Devuelve la dirección IP si se resuelve correctamente.
    """
    try:
        # Ejecuta el comando DIG para consultar el DNS
        result = subprocess.run(['dig', '+short', domain], capture_output=True, text=True)
        ip_address = result.stdout.strip()  # Obtiene la salida y la limpia
        
        if ip_address:
            return ip_address
        else:
            print(f"No se encontró respuesta para {domain}")
            return None
    except Exception as e:
        print(f"Error en la consulta DNS para {domain}: {e}")
        return None

def handle_dns_request(domain):
    """
    Gestiona la solicitud DNS para el dominio, consultando el caché y el DNS si es necesario.
    """
    # Verifica si el dominio está en el caché
    cached_ip = r.get(domain)
    if cached_ip:
        print(f"Cache HIT: {domain} -> {cached_ip.decode()}")
    else:
        print(f"Cache MISS: {domain}. Consultando DNS...")
        # Realiza la consulta DNS si no está en el caché
        ip_address = query_dns(domain)
        if ip_address:
            # Almacena en el caché
            r.set(domain, ip_address)
            print(f"{domain} -> {ip_address} (almacenado en caché)")
        else:
            print(f"Error: No se pudo resolver {domain}")
