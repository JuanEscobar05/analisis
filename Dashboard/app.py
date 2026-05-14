import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from connection.conexion import obtener_conexion

st.set_page_config(
    page_title="Dashboard de Ventas",
    layout="wide"
)

st.title("Dashboard de Ventas")
conexion = obtener_conexion()


query = """
SELECT 
     YEAR(OrderDate) AS año, 
     MONTH(OrderDate) AS mes, 
     SUM(TotalDue) AS TotalVentas 
FROM Sales.SalesOrderHeader
GROUP BY YEAR(OrderDate), MONTH(OrderDate)
ORDER BY Año, Mes;
"""


df = pd.read_sql(query, conexion)
total_ventas = df["TotalVentas"].sum()
promedio_ventas = df["TotalVentas"].mean()
max_ventas = df["TotalVentas"].max()

col1, col2, col3 = st.columns(3)
col1.metric("Total Ventas", f"${total_ventas:,.2f}")
col2.metric("Promedio Ventas", f"${promedio_ventas:,.2f}")
col3.metric("Máxima Venta", f"${max_ventas:,.2f}")

st.subheader("tabla de ventas")

st.dataframe(df)

st.subheader("Gráfico de Ventas")

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(df["TotalVentas"])

ax.set_title("Ventas por mes")
ax.set_xlabel("Mes")
ax.set_ylabel("Ventas")

st.pyplot(fig)

st.subheader("Ventas en Barra")

fig2, ax2 = plt.subplots(figsize=(10, 5))

ax2.bar(df.index, df["TotalVentas"])

st.pyplot(fig2)