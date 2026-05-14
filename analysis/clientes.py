import pandas as pd
from connection.conexion import obtener_conexion

conexion = obtener_conexion()

with open("sql/clientes_ventas.sql", "r", encoding="utf-8") as archivo:
    query = archivo.read()

df = pd.read_sql(query, conexion)

print(df)

df.to_excel(
    "exports/reportes_excel/clientes_ventas.xlsx",
    index=False
)

print("Excel exportado correctamente")