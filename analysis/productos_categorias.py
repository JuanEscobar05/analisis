import pandas as pd
from connection.conexion import obtener_conexion

conexion = obtener_conexion()

with open("sql/productos_categorias.sql", "r", encoding="utf-8") as archivo:
    query = archivo.read()

df = pd.read_sql(query, conexion)

print(df)

df.to_excel(
    "exports/reportes_excel/productos_categorias.xlsx",
    index=False
)