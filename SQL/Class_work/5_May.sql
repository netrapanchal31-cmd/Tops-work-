-- 5 may 

use tops_labtask;
select*from employee;
select*from department;

-- view create
create view view_dept_emp_1 as
select ename,salary,dname from employee,department
where employee.Did=department.Did;

-- how to use view
select dname,ename from view_dept_emp where dname='HR';

-- commit,savepoint and rollback as TCL

select * from employee;

-- rollback quries 
start transaction;
delete from employee where eid=106;
rollback;

-- commit
start transaction;
delete from employee where eid=107;
commit;

-- savepoint 
start transaction;
savepoint sp1;
update employee set ename='Masum' where eid =105;

savepoint sp2;
delete from employee where eid=111;

rollback to sp2;
commit;

savepoint sp3;
update employee set email='masum@gmail.com' where eid=105;
savepoint sp5;
update employee set ename='krish' where eid=101;
rollback to sp5;
savepoint sp4;
delete from employee where eid=115;
commit;
savepoint sp6;
update employee set ename='NETRA' WHERE EID=101;
COMMIT;



