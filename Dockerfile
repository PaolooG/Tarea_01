# Usar una imagen base ligera de Python
FROM python:3.8-slim

# Instalar dnsutils para usar dig
RUN apt-get update && apt-get install -y dnsutils && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar requirements.txt al contenedor
COPY requirements.txt .

# Instalar las dependencias sin usar caché para evitar conflictos
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código fuente al contenedor
COPY src/ ./src/

# Comando para ejecutar el servidor gRPC
CMD ["python", "./src/grpc_server.py"]
