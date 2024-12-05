-- 1. Count the Total Number of Days Each Employee was Present


select count(Status),EmployeeID from attendance
where Status='Present'
group by EmployeeID;



-- 2. Find Employees Who Have Never Been Absent
select * from attendance where EmployeeID not in (
select EmployeeID from attendance where Status='Absent')



-- 3. Identify Employees Who Have Worked on More Than One Project

select count(ProjectID), EmployeeID from employeeprojects
group by EmployeeID
having count(ProjectID)>1


-- 4. Find the Average Sales Amount for Each Employee

select EmployeeID,avg(SaleAmount) from sales
group by EmployeeID


-- 5. Calculate the Overall Attendance Percentage for Each Employee
select EmployeeID, count(AttendanceDate),
sum(case when status='Present' then 1 else 0 end ) as days,
(sum(case when status='Present' then 1 else 0 end ) /count(AttendanceDate) ) *100 as a
-- case when 
 from attendance
 group by EmployeeID