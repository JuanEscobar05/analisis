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