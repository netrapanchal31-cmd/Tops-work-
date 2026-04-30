-- 18 april
use student;
drop table employee;

create table employee(
eid int primary key auto_increment,
ename varchar(20),
salary int
);

insert into employee(ename, salary) 
values('netra', 25000),
('krish', 40000),
('lata',20000);

alter table employee add city varchar(20);
select * from employee;

update employee set city='Ahmedabad' where eid=1;
update employee set city='Gandhinagar' where eid=2;
update employee set city='Surat' where eid=3;

-- Show Table
select * from employee;

-- Fetch Employee Details Whose Salary Between 20000 to 30000
select * from employee where salary between 20000 and 25000;

-- Fetch Employee  names who are belongs to Ahmedabad and Gandhinagar
select ename, city from employee where city in ('Ahmedabad','Gandhinagar');


-- Fetch Employee Details in Assending Order of ename
select * from employee order by ename;

-- Desending
select * from employee order by ename desc;