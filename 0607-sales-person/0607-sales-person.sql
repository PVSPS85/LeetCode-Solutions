# Write your MySQL query statement below
SELECT S.name
FROM SalesPerson AS S
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders AS O
    JOIN Company AS C
    ON O.com_id = C.com_id
    WHERE C.name = 'RED'
      AND O.sales_id = S.sales_id
);