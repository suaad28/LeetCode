# Write your MySQL query statement below
select machine_id, round(avg(processes),3) as processing_time
from (
    select a1.machine_id, a2.timestamp - a1.timestamp as processes
    from activity a1
    join activity a2 using (machine_id)
        where a1.process_id = a2.process_id
        and a2.timestamp > a1.timestamp
        group by machine_id, a1.process_id
) temp
group by machine_id;

