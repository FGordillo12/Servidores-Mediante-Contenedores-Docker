import os
import socket

from fastapi import FastAPI

app = FastAPI(title="API Servidores Docker")

# Variable de entorno que diferencia cada instancia desplegada
SERVIDOR = os.getenv("SERVIDOR", "Servidor sin nombre")


@app.get("/")
def raiz():
    return {
        "mensaje": "El servidor está funcionando correctamente",
        "servidor": SERVIDOR,
        "contenedor": socket.gethostname(),
    }


@app.get("/salud")
def salud():
    return {
        "estado": "saludable",
        "servidor": SERVIDOR,
    }
