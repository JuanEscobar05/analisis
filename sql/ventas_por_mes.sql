
/*Guardar la consulta de ventas por mes*/

SELECT YEAR(OrderDate) AS año, MONTH(OrderDate) AS mes, SUM(TotalDue) AS TotalVentas FROM Sales.SalesOrderHeader
GROUP BY YEAR(OrderDate), MONTH(OrderDate) ORDER BY Año, Mes;