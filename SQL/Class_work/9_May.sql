-- 9 May 
-- over define he window(set of row)
-- partition by 
-- order by 
USE TOPS_LABTASK;

-- category (7000 more than salary and want to give high salary than want to give average and than low)
-- categorize employees by salary level -- case statement

SELECT ENAME,SALARY,
AVG(SALARY) OVER () AS AVG_SALARY,
CASE 
WHEN SALARY>AVG(SALARY) OVER()
THEN 'ABOVE AVERAGE' 
WHEN SALARY<AVG(SALARY) OVER()
THEN 'BELOW AVERAGE' 
ELSE 'EQUAL'
END AS SALARY_STATUS
FROM EMPLOYEE;

select * from department; 
-- Mark top peformer in each department 

SELECT ENAME,DID,SALARY,
CASE
WHEN RANK() OVER (partition by DID ORDER BY SALARY DESC) =1
THEN 'TOP PERFOMER'
WHEN RANK() OVER (partition by DID ORDER BY SALARY DESC) =2
THEN 'SECOND PERFOMER'
ELSE 'OTHER'
END AS PERFORMACE 
FROM EMPLOYEE;

-- flag employees earning more than department average AVERGAE DEPT ACCORDING

SELECT ENAME,DID,SALARY,
  CASE 
    WHEN SALARY > AVG(SALARY) OVER 
(partition by DID)
    THEN 'ABOVE DEPT AVG'
    ELSE 'BELOW DEPT AVG'
  END AS STATUS_ACCORDING_TO_DEPT
FROM EMPLOYEE;

select ename,did,salary,
   case 
   when salary=max(salary) over 
(partition by did) then 'Higher'
 when salary=min(salary) over 
 (partition by did) then 'Lower'
else 'average'
 end as Salary_Status 
 From employee;

-- SUBQUERIES (query within query) or nested query
-- it execute first inner query than outer query 
-- find employees who earn more than average salary 




