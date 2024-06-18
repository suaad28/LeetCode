# Write your MySQL query statement below
select em.unique_id, e.name 
from Employees e
left join  EmployeeUni em
on e.id=em.id
