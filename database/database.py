import sqlite3
from pathlib import Path

# Ruta de la base de datos
RUTA_BASE_DATOS = Path(__file__).resolve().parent / "ecommerce.db"


def obtener_conexion():
    conexion = sqlite3.connect(RUTA_BASE_DATOS)
    conexion.row_factory = sqlite3.Row
    return conexion


def inicializar_base_datos():
    conexion = obtener_conexion()

    try:
        ruta_schema = Path(__file__).resolve().parent / "schema.sql"

        with open(ruta_schema, "r", encoding="utf-8") as archivo:
            conexion.executescript(archivo.read())

    finally:
        conexion.close()