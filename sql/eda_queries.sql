SELECT strftime('%Y-%m', InvoiceDate) AS Month, SUM(Quantity * UnitPrice) AS Revenue
FROM transactions
GROUP BY Month
ORDER BY Month;