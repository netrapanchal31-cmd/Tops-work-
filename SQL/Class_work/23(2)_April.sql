-- 23 april

use class_work;
Create table department ( DID int primary key , dname varchar(20));
 
create table employee_1 (EID int primary key auto_increment, ename varchar (20), email varchar(20), salary int, e_no decimal(10),dept_id int,
foreign key (dept_id) references department(DID));


insert into department values (101,'sales'),
(102,'marketing'),(103,'HR'),(104,'Admin');

insert into employee_1(ename,email,salary,e_no,dept_id) values
('neel','neel@gamil.com',250000,1234567891,101),
('netra','netra@gmail.com',300000,2763876476,102),
('bhavesh','bhavesh@gmail.com',67899,2435271890,103),
('krish','krish@gmail.com',677299,5689009876,104);

select * from employee_1;

alter table employee_1 modify EID int auto_increment;



 
 



