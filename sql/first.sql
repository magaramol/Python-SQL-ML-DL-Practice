-- first code
-- day 1
-- List employees along with their department names.

select concat(a.FirstName, ' ',a.LastName) as namess ,b.DepartmentName from employees a

left join departments b
on a.DepartmentID=b.DepartmentID;

-- Find employees who are working on projects, including project names and allocation percentages.


select * from employeeprojects a right join employees b
on a.EmployeeID=b.EmployeeID
left join projects c 
on a.ProjectID=c.ProjectID
where a.ProjectID is not null ;

-- Get a list of all projects and the departments they belong to.


select a.ProjectName,b.DepartmentName from projects a left join departments b
on a.DepartmentID=b.DepartmentID

-- Find employees who are not assigned to any project.
select * from employees a left join employeeprojects b
on a.EmployeeID=b.EmployeeID
where ProjectID is null


-- List employees and the total number of projects they are assigned to.
select FirstName,count(ProjectID) as cnt
 from employees a left join employeeprojects b
on a.EmployeeID=b.EmployeeID
group by FirstName

-- Find the department name with the highest number of employees.

select d.* from departments d join (
select DepartmentID from employees
group by DepartmentID
order by count(EmployeeID) desc
limit 1) a
on d.DepartmentID=a.DepartmentID

-- List employees earning more than the average salary.
select * from employees
where Salary > (select avg(salary) from employees);


-- Find projects that belong to departments located in 'New York'.

select a.ProjectName from projects a 
left join departments b
on a.DepartmentID=b.DepartmentID
where b.Location='New York';

-- Get employees who are working on more than one project.
select EmployeeID  from employeeprojects
group by EmployeeID
having count(ProjectID)>1

-- Identify employees whose total allocation across all projects is less than 100%.

select EmployeeID from employees where EmployeeID in (
select EmployeeID from employeeprojects
group by EmployeeID
having  sum(AllocationPercentage)<100)
