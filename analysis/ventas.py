import pandas as pd
from connection.conexion import obtener_conexion

conexion = obtener_conexion()

with open("sql/ventas_por_mes.sql", "r", encoding="utf-8") as archivo:
    query = archivo.read()

df = pd.read_sql(query, conexion)

print(df)