# Write your MySQL query statement below
SELECT p.project_id , ROUND(AVG(E.experience_years),2) AS average_years
FROM project AS p join Employee AS E ON p.employee_id = E.employee_id 
GROUP BY project_id; 