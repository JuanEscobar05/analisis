import matplotlib.pyplot as plt
import pandas as pd
from connection.conexion import obtener_conexion

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

plt.plot(df["TotalVentas"])

plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Ventas")

plt.show()