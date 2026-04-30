-- 28th april 

use tops_labtask;

-- find no of order by each product 
select count(*) as 'no of product ordered', p_name as 'product name' from product_lt, order_details_lt
where product_lt.PID=order_details_lt.pid_1
group by p_name;

-- find no of orderd product is more than 5 
select count(order_details_lt.PID_1) as 'no of product ordered_1', p_name as 'product name_1' from product_lt,order_details_lt
where product_lt.PID=order_details_lt.pid_1
group by p_name having count(order_details_lt.PID_1)>3;

-- find no of ordered customer whose has give more then 1 time ordered 
SELECT COUNT(order_details_lt.CID_1), c_name FROM customer_lt,order_details_lt
WHERE customer_lt.cID = order_details_lt.cid_1
GROUP BY c_name having count(order_details_lt.cid_1)>1;