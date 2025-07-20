SELECT strftime('%Y-%m', InvoiceDate) AS Month, SUM(Quantity * UnitPrice) AS Revenue
FROM transactions
GROUP BY Month
ORDER BY Month;

SELECT Country, SUM(Quantity * UnitPrice) AS Revenue
FROM transactions
GROUP BY Country
ORDER BY Revenue DESC;

SELECT StockCode, Description, SUM(Quantity * UnitPrice) AS TotalRevenue
FROM transactions
GROUP BY StockCode, Description
ORDER BY TotalRevenue DESC
LIMIT 5;

SELECT CustomerID, 
       (strftime('%s', MAX(InvoiceDate)) - strftime('%s', (SELECT MAX(InvoiceDate) FROM transactions))) / 86400 AS Recency, -- В днях
       COUNT(DISTINCT InvoiceNo) AS Frequency,
       SUM(Quantity * UnitPrice) AS Monetary
FROM transactions
GROUP BY CustomerID;