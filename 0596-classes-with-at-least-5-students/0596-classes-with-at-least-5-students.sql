# Write your MySQL query statement below
SELECT class from Courses  
group by class 
HAving count(student) >= 5; 