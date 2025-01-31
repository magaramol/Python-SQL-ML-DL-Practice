# Write your MySQL query statement below
with min_order as (
select min(order_date) as order_date,customer_id from delivery
group by customer_id),
cte as (select *,case when order_date=customer_pref_delivery_date then 1 else 0 end as pref  from delivery)
select round((sum(pref)/count(*)*100),2) as immediate_percentage  from cte a inner join min_order b on a.customer_id=b.customer_id and a.order_date=b.order_date
