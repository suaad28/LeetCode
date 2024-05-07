# Write your MySQL query statement below
select e.name, b.bonus 
from employee e 
LEFT join bonus b using (empId)
where b.bonus < 1000 or b.bonus is NULL