-- 16 april 
create database class_work;
use class_work;



create table customer (
	cid int primary key,
    cname varchar(20) not null,
    c_no int(10) unique key,
    email varchar(20)  unique key
 );

insert into customer values
	(101, 'cust1', 12345, 'cust@gmail.com'),
    (102, 'cust2', 12354, 'cust2@gmail.com');

select * from customer;

insert into customer values
	(103, 'cust3', 13245, 'cust3@gmail.com');
select * from customer;

delete from customer where cid=102;

select * from customer;

select cname, c_no from customer;

select * from  customer where cid=103;

insert into customer values
	(104, 'Krunal', 99249, 'krunal@gmail.com'),
    (105, 'neel', 12346, 'neel@gmail.com'),
    (106, 'Netra', 98765, 'netra@gmail.com');

select * from customer where cname = 'krunal' or cname='neel';

select * from customer where cname='neel' and c_no=12346;
