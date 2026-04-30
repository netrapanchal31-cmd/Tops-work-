-- 30th april 

use tops_labtask;

select * from employee;
select concat(ename,' ',email) as 'Name email' from employee;

select ename,length(ename) as 'total no of letters',upper(ename) from employee;

select ename,length(ename) as 'total no of letters',lower(ename) from employee;
-- substring name of row,starting,end
select substring(ename,1,4) from employee;
-- remove space 
select * from employee where trim(ename)='netra';
-- replace (make me understand) 
select replace(ename,'Neha','srusti') from employee;
-- current and time 
select now();
-- want date where we do syntax -- curent date
select curdate();

-- current time 
select curtime();

-- year month date
select year(join_date) from employee;

-- fetch emplotyee details who register in 2020 year 
select * from employee where year (join_date)=2020;

-- fetch employee details who register on 19th date 
select * from employee where day (join_date)=19;

