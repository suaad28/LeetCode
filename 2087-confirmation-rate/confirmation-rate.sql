# Write your MySQL query statement below
select s.user_id,
case when c.requested > 0 then round(c.confirmed/c.requested,2)
else 0.00
end as confirmation_rate
from signups s
left join (
    select user_id,
    sum(case when action = 'confirmed' then 1 else 0 end) as confirmed,
    count(*) as requested
    from confirmations
    group by user_id
) c on s.user_id = c.user_id
















-- SELECT 
--     s.user_id,
--     CASE 
--         WHEN c.total_requested > 0 THEN ROUND(c.confirmed / c.total_requested, 2)
--         ELSE 0.00
--     END AS confirmation_rate
-- FROM 
--     Signups s
-- LEFT JOIN (
--     SELECT 
--         user_id,
--         SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) AS confirmed,
--         COUNT(*) AS total_requested
--     FROM 
--         Confirmations
--     GROUP BY 
--         user_id
-- ) c ON s.user_id = c.user_id;
