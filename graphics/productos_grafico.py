import pandas as pd
import matplotlib.pyplot as plt
from connection.conexion import obtener_conexion

conexion = obtener_conexion()

query = """

SELECT TOP 10  
     p.Name AS Producto, 
     SUM(d.OrderQty) AS CantidadVendida 
FROM Sales.SalesOrderDetail d
JOIN Production.Product p 
     ON d.ProductID = p.ProductID 
GROUP BY p.Name 
ORDER BY CantidadVendida DESC;
"""

df = pd.read_sql(query, conexion)

plt.figure(figsize=(12,6))

plt.bar(df["Producto"], df["CantidadVendida"])

plt.xticks(rotation=45)

plt.title("Top 10 productos más vendidos")
plt.xlabel("Productos")
plt.ylabel("Cantidad Vendida")

plt.tight_layout()

plt.show()