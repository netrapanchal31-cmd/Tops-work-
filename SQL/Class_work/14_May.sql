-- 14 MAY
USE TOPS_LABTASK;

-- CTE Function (common table expression) it is a temporary result set that exists only during the exection of a query 
-- It is created using WITH clause 

-- Find employees whoes salary is greater than the average salary 

WITH avgsalaryCTE AS 
( SELECT AVG(Salary) AS Avg_salary 
FROM Employee
)
SELECT 
E.EID,
E.ENAME,
E.SALARY 
FROM Employee E 
JOIN avgsalaryCTE 
ON E.SALARY > avgsalaryCTE.Avg_salary; 

-- WITHOUT JOIN 

WITH avgsalaryCTE AS 
( SELECT AVG(Salary) AS Avg_salary 
FROM Employee
)
SELECT ENAME,EID,SALARY 
FROM EMPLOYEE 
WHERE SALARY > 
(
SELECT AVG_SALARY
FROM AVGSALARYCTE
);

-- Find employee with max salary from each dept 

WITH MAXSALARYCTE AS 
(
SELECT MAX(SALARY) as MAX_salary FROM EMPLOYEE 
GROUP BY DID
)
SELECT 
E.EID,
E.ENAME,
E.SALARY,
E.DID
FROM EMPLOYEE E 
JOIN MAXSALARYCTE 
ON E.salary = MAXSALARYCTE.MAX_salary;

select * from department;
select * from employee;

-- using with ROWNUMBER
-- This method is usesful when multiple ranking is needed 
-- find the highest salary and rank them according to dept 

WITH RankedemployeesCTE AS 
(
SELECT 
EID,
ENAME,
DID,
SALARY,
row_number()OVER
(partition by DID 
ORDER BY SALARY DESC )
AS M 
FROM EMPLOYEE
)
SELECT 
EID,ENAME,DID,SALARY
FROM RankedemployeesCTE
WHERE M=1;

 