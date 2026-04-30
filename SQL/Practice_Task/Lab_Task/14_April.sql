
-- 14th April
create database Tops_Labtask;

use Tops_Labtask;

create table customer(
cust_name varchar(20),
cust_num int(10),
cust_address varchar(30),
cust_email varchar(20)
);

-- when we want to add the other colume into the presented table use "alter"
alter table customer add( cid int, c_num int(10));
-- to know the data type and colume in the given table 
describe customer;
-- to add the values in the alter colume which we add just now 
insert into customer (cid, cust_name, cust_num) values(1,"netra",9924);
describe customer;

-- drop table (to delete)

-- print table 
select * from customer;
-- if we make new row after the present table than if we want to add the values in that we use this syntax
update customer set cust_email = "netra@gmail.com" where cid=1;

-- to delete the row 
delete from customer where cid=1; 




