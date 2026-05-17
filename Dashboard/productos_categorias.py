import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from connection.conexion import obtener_conexion

st.set_page_config(
    page_title="Dashboard de Productos y Categorias",
    layout="wide"
)

st.title("Dashboard de Productos y Categorias")
conexion = obtener_conexion()

query = """
SELECT TOP 100
    pc.Name AS Categoria,
    p.Name AS Producto,
    SUM(sod.OrderQty) AS CantidadVendida,
    SUM(sod.LineTotal) AS TotalVenTAS,
    AVG(sod.UnitPrice) AS PrecioPromedio,
    MAX(sod.UnitPrice) AS PrecioMaximo,
    MIN(sod.UnitPrice) AS PrecioMinimo
FROM Sales.SalesOrderDetail sod
JOIN Production.Product p
    ON sod.ProductID = p.ProductID
JOIN Production.ProductSubcategory ps
    ON p.ProductSubcategoryID = ps.ProductSubcategoryID
JOIN Production.ProductCategory pc
    ON ps.ProductCategoryID = pc.ProductCategoryID
GROUP BY 
    pc.Name,
    p.Name
ORDER BY TotalVenTAS DESC;
"""

st.sidebar.title("Filtros")
top_n = st.sidebar.slider(
    "Cantidad de Productos",
    5,
    100,
    10
)

df = pd.read_sql(query, conexion)
df = df.head(top_n)

total_cantidad = df["CantidadVendida"].sum()
total_ventas = df["TotalVenTAS"].sum()
total_promedio = df["PrecioPromedio"].mean()
total_maximo = df["PrecioMaximo"].max()
total_minimo = df["PrecioMinimo"].min()

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Cantidad Vendida:", f"{total_cantidad}")
col2.metric("Total Ventas:", f"${total_ventas:,.2f}")
col3.metric("Precio Promedio:", f"${total_promedio:,.2f}")
col4.metric("Precio Máximo:", f"${total_maximo:,.2f}")
col5.metric("Precio Mínimo:", f"${total_minimo:,.2f}")


st.subheader("Tabla de Productos y Categorias")
st.dataframe(df)


