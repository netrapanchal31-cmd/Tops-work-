-- 12th may 
USE tops_labtask;

-- find employee who earn more than avg salary 
SELECT ename,salary
FROM employee
WHERE salary > (SELECT AVG(salary) FROM Employee);

-- find employee who earn more than the avg salary of their own dept 
SELECT ename,salary
FROM employee e1
WHERE salary > ( SELECT AVG (salary) FROM employee e2
WHERE e1.DID=e2.DID);

-- Find dept names with more than 2 employees
SELECT d.dname, emp_count.num_employee
FROM department d
JOIN (SELECT did, COUNT(*) AS num_employee FROM employee GROUP BY did) AS emp_Count
ON d.did=emp_Count.DID
WHERE emp_Count.num_employee > 2;

-- Display department with more than 2 employee 
SELECT did,dname 
FROM department D 
WHERE 2 < 
(SELECT COUNT(*)
FROM employee 
WHERE did=D.did);


