-- 1. Find departments that have no projects assigned.
select * from projects a
right join departments b
on a.DepartmentID=b.DepartmentID
where a.ProjectID is null

-- 2. List employees who work on projects in a different department than their own.
select * from employees a left join employeeprojects b on a.EmployeeID=b.EmployeeID
left join projects c on b.ProjectID=c.ProjectID
where a.DepartmentID!=c.DepartmentID

-- 3. Calculate the total salary of employees in each department, including departments with no employees.

select sum(salary),DepartmentID from employees
group by DepartmentID;
