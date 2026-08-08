# Write your MySQL query statement below
SELECT w1.id
FROM Weather as w1
join weather as w2
on w1.recordDate = DATE_ADD(w2.recordDate , interval 1 Day)
WHere w1.temperature > w2.temperature;