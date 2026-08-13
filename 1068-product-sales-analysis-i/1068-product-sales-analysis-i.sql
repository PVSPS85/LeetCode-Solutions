# Write your MySQL query statement be
SELECT product_name , year , price 
from Product AS p JOIN Sales AS s
on p.product_id = s.product_id;