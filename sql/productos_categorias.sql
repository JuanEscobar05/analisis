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