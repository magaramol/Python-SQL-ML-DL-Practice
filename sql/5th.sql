-- ### **1. What is the total revenue generated by each customer?**


select sum(OrderAmount),CustomerID from orders
group by CustomerID;

-- ---

-- ### **2. Which employee handled the maximum number of orders?**


select count(OrderID),EmployeeID from orders
group by EmployeeID
order by count(OrderID) desc limit 1;
-- ---

-- ### **3. Find the average order amount for all orders placed in February 2024.**



select avg(OrderAmount) from orders

where OrderDate between '2024-02-01' and '2024-02-29';
-- ---

-- ### **4. Identify the customer who has spent the highest total amount across all their orders.**


select sum(OrderAmount),CustomerID from orders
group by CustomerID
order by sum(OrderAmount) desc
limit 1;

-- ---

-- ### **5. Determine the number of orders placed, total revenue, and average order amount for each employee.**
select count(OrderID),sum(OrderAmount),avg(OrderAmount),EmployeeID from orders
group by EmployeeID;