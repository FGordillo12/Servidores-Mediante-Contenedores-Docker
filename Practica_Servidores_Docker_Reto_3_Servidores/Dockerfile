# Imagen base de Python (versión ligera)
FROM python:3.12-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalación de las dependencias
RUN pip install --no-cache-dir fastapi uvicorn

# Copia de los archivos de la aplicación
COPY app.py .

# Puerto en el que escucha la aplicación
EXPOSE 8000

# Comando para iniciar el servidor mediante Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
