# Write your MySQL query statement below
SELECT name,bonus 
FROM Employee as E LEFT  JOIN Bonus as B 
ON E.empID = B.empID 
WHERE B.bonus < 1000 OR B.bonus is NULL ;