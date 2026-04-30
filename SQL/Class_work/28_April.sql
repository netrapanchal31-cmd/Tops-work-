-- 28th april 
use tops_labtask;
-- fetch employee details with dept e_name 
SELECT Department.dname, Employee.ename, Employee.email, Employee.salary
FROM Employee, Department
WHERE Employee.did = Department.Did;

-- count no of emplyoees in each department 
SELECT COUNT(eid) AS 'no of employee', dname
FROM Employee, Department
WHERE Employee.did = Department.Did
GROUP BY dname;

-- fetch dept name whose has more than 4 employees 
select count(*) as 'no of employee_1', dname
from Employee,Department
where employee.did=department.Did
group by dname having count(*)>=3;

-- avg salary of employees in each department 
select avg(salary) as "Average of salary", dname
from employee,department
where employee.did=department.Did 
group by dname;









