# Write your MySQL query statement below
select person_name from (
    select person_name, sum(weight) over (order by turn)  as total_weight
    from queue
    order by total_weight DESC
) as t
where total_weight<=1000 
limit 1
