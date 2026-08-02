# Write your MySQL query statement below
SELECT email as Email
FROM person
GROUP BY Email
HAVING count(*) > 1;
