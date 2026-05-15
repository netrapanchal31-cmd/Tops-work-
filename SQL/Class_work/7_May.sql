-- 7may 
-- windows function (create windown) for compersion with each or set  row  and corresponding data each row 

-- find minimum salary for each dept
use tops_labtask;


-- each dept avg salary 
SELECT avg(salary) 
FROM employee, Department 
WHERE department.DID = employee.did
group by dname;

-- find avg salary for each dept (without using group by) 
select e.ename,d.dname,e.salary,
avg(e.salary)
OVER (partition by D.DNAME) 
AS AVG_DEPT_SALARY 
FROM EMPLOYEE E 
JOIN DEPARTMENT D ON E.DID =D.DID;

-- count employee in each dept (without group by ) 
select e.ename,d.dname,
count(e.ename)
over (partition by d.dname)
as count_employee_name
from employee e
join department d 
on e.did= d.did;

-- row_number()     assigns a unique number to eachrow 
select ename,salary,
row_number()
over (order by ename)
as salary_rank
from employee;

-- rank()   gives rank with gaps if duplicate values exist (if a person get same salary than he got 1 twise and 2 remove)
select ename,salary,
rank()
over (order by salary desc)
as salary_rank
from employee;

-- dense_Rank() similar to rank but no gaps

select ename,salary,
dense_rank()
over (order by salary desc)
as salary_rank
from employee;

-- rank employees department -wise  

select e.ename,d.dname,e.salary,
rank() over (partition by d.dname order by e.salary desc)
as dept_rank
from employee e 
join department d 
on e.did=d.did;





