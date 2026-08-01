# Write your MySQL query statement below
SELECT firstName, lastName, city, state
FROM Person as P LEFT join Address as A 
ON P.personId = A.personId;