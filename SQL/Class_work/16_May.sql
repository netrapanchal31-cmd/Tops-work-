-- 16th may
use tops_labtask;

-- Indexing (searching become easy / fast ) for optimization purpose we have to use indexing 
CREATE INDEX IDX_ENAME
ON Employee(ename);

EXPLAIN 
SELECT * FROM employee 
WHERE ENAME= "Krish";

CREATE INDEX IDX_Department 
ON employee (DID);

EXPLAIN 
SELECT * FROM Employee
WHERE DID = 2;

DROP INDEX IDX_ENAME 
ON Employee;

SHOW indexes FROM employee;
