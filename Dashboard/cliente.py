import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from connection.conexion import obtener_conexion

st.set_page_config(
    page_title="Dashboard de Clientes",
    layout="wide"
)

st.title("Dashboard de Clientes")
conexion = obtener_conexion()

query = """
SELECT TOP 50
      c.CustomerID,
      CONCAT(
        p.FirstName,
        ' ',
        p.LastName
      ) AS Cliente,
      COUNT (soh.SalesOrderID) AS TotalOrdenes,
      SUM(soh.TotalDue) AS TotalGastado,
      AVG(soh.TotalDue) AS TotalPromedio,
      MAX(soh.TotalDue) AS CompraMaxima
FROM Sales.Customer c
JOIN Sales.SalesOrderHeader soh
    ON c.CustomerID = soh.CustomerID
JOIN Person.Person p
    ON c.PersonID = p.BusinessEntityID
GROUP BY
      c.CustomerID,
      p.FirstName,
      p.LastName
ORDER BY TotalGastado DESC
"""

st.sidebar.title("Filtros")

top_n = st.sidebar.slider(
    "Cantidad de Clientes",
    5,
    50,
    10
)

df = pd.read_sql(query, conexion)
df = df.head(top_n)


total_ordenes = df["TotalOrdenes"].sum()
maximo_gastado = df["TotalGastado"].max()
promedio_gastado = df["TotalGastado"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Ordenes:", f"{total_ordenes}")
col2.metric("Maximo Gastado:", f"${maximo_gastado:,.2f}")
col3.metric("Promedio Gastado:", f"${promedio_gastado:,.2f}")


st.subheader("Tabla de Clientes")
st.dataframe(df)

st.subheader("Top Clientes por Gasto")

fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(
    df["Cliente"],
    df["TotalGastado"]
)

ax.set_title("Clientes con mayor gasto")
ax.set_xlabel("Clientes")
ax.set_ylabel("Total Gastado")

plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader("Promedio de compra por cliente")

fig2, ax2 = plt.subplots(figsize=(12, 6))

ax2.plot(
    df["Cliente"],
    df["TotalPromedio"]
)

ax2.set_title("Promedio de Compra")
ax2.set_xlabel("Clientes")
ax2.set_ylabel("Promedio")

plt.xticks(rotation=45)
st.pyplot(fig2)

st.subheader("Participación de Clientes")

top10 = df.head(10)

fig3, ax3 = plt.subplots(figsize=(8, 8))

ax3.pie(
    top10["TotalGastado"],
    labels=top10["Cliente"],
    autopct="%1.1f%%",
)

st.pyplot(fig3)