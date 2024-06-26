# Write your MySQL query statement below
with first as (
select * from delivery 
where (customer_id,order_date) in (select customer_id, min(order_date) from delivery 
group by customer_id)
)

select round(sum(if(order_date = customer_pref_delivery_date,1,0))/ count(customer_id) * 100,2) as immediate_percentage from first