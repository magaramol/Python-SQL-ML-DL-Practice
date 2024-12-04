-- 1. Categorize Employees Based on Their Salary Range
select * ,

case when Salary <50000 then 'low' when salary between 50000 and 70000 then 'mid' else 'high' end as rangee
from employees

-- 2. Add a Sales Performance Rating Based on Sale Amount

select *,

case when SaleAmount<500 then 'low' when SaleAmount between 500 and 700 then 'mid' else 'high' end as rangee
 from sales


 -- 3. Identify Project Allocation Status
-- Show the allocation percentage for employees on projects, 
-- with a label: "Under Allocated" (<100%), "Fully Allocated" (=100%), and "Over Allocated" (>100%).
select EmployeeID, sum(AllocationPercentage), case when sum(AllocationPercentage)<100 then 'under' 
when sum(AllocationPercentage)=100 then 'fully' else 'over' end as statuss
from employeeprojects
group by EmployeeID


-- Generate Employee Bonus Category Based on Sales
-- For each employee, classify their bonus category based on their total sales: "No Bonus" (<$500), 
-- "Small Bonus" ($500–$1000), and "Big Bonus" (>$1000).

select EmployeeID, sum(SaleAmount)
,case when sum(SaleAmount)<500 then 'no_bonus' when sum(SaleAmount) between 500 and 1000 then 'small_bonus' else 'big_bonus' end as bonus
from sales
group by EmployeeID