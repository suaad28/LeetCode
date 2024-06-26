# Write your MySQL query statement below
select p.project_id, round((sum(e.experience_years)/count(e.employee_id)),2) as average_years
from Project p
join Employee e using (employee_id)
group by project_id