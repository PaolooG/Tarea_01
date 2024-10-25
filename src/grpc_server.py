import grpc
from concurrent import futures
import os
import dns_service_pb2
import dns_service_pb2_grpc
from dns_cache import handle_dns_request

class DNSCacheService(dns_service_pb2_grpc.DNSCacheServicer):
    def GetDNSResponse(self, request, context):
        """
        Implementación del método gRPC para obtener la respuesta DNS.
        """
        ip = handle_dns_request(request.domain)  # Obtiene la respuesta desde el caché
        return dns_service_pb2.DNSResponse(ip_address=ip or "No se encontró IP")

def serve():
    """
    Inicia el servidor gRPC.
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dns_service_pb2_grpc.add_DNSCacheServicer_to_server(DNSCacheService(), server)

    # Configura el puerto para el servidor gRPC
    port = os.getenv('GRPC_PORT', '50051')
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    print(f"Servidor gRPC corriendo en el puerto {port}...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
