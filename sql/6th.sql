select * from products

# 1. Find the total stock of all products across all categories.
;
select sum(Stock) from products;

# 2. Identify the most expensive product in each category.
select * from (select * , rank() over(partition by Category order by price desc) as rnk from products) a
where a.rnk=1;

# 3. Calculate the total revenue that can be generated if all products in stock are sold (Price × Stock).
select sum(Stock*Price) as tl_rev from products;

# 4. List all categories that have an average product price greater than 10,000.
select avg(Price),Category from products
group by Category
having avg(Price)>10000;
# 5. Find the product with the least stock across all categories.

SELECT * 
FROM Products 
WHERE Stock = (SELECT MIN(Stock) FROM Products);
