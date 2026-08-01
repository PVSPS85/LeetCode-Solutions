# Write your MySQL query statement below
Select E.name as Employee
FROM Employee as E
JOIN Employee as M 
on E.managerId = M.id 
Where E.salary > M.salary;
