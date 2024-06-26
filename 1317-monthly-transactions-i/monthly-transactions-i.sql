# Write your MySQL query statement below
select date_format(trans_date,'%Y-%m') as month,
country,
count(*) as trans_count, 
sum(IF(state='approved',1,0)) as approved_count, 
sum(amount) as trans_total_amount, 
sum(IF(state='approved', amount,0)) as approved_total_amount
from Transactions
group by month, country