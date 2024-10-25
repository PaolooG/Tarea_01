import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('src/dataset.csv')  # Cargar el dataset

# Verificar las columnas del dataset
print("Columnas disponibles:", df.columns)

columna_dominios = 'domain'  # Ajusta si el nombre es diferente
frecuencia = df[columna_dominios].value_counts()  # Calcular frecuencia

print(frecuencia.head(10))  # Mostrar las primeras 10 frecuencias

# Crear gráfico de barras
plt.figure(figsize=(10, 6))
frecuencia.plot(kind='bar', color='skyblue')
plt.title('Distribución de Frecuencias de las Consultas DNS')
plt.xlabel('Dominios')
plt.ylabel('Frecuencia de Consultas')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
