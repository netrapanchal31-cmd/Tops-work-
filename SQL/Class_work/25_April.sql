
-- 25th april
 
-- fetch order details with product name and customer name 
use tops_labtask;
select OID,c_name,p_name,qty,or_date
from order_details_LT, Customer_LT, product_LT
where Customer_LT.CID=order_details_LT.CID_1 and product_LT.PID=order_details_LT.PID_1;

-- left join from product 
SELECT order_details_lt.*, product_lt.p_name, order_details_lt.qty
FROM product_lt
LEFT JOIN order_details_lt
ON product_lt.PID = order_details_lt.PID_1;

insert into Customer_LT (CID,c_name,address) values
(111,'Netra','ranip');

-- left join
SELECT order_details_lt.*, customer_lt.c_name, order_details_lt.qty
FROM customer_lt
LEFT JOIN order_details_lt 
ON customer_lt.CID = order_details_lt.CID_1;

-- union 
SELECT c_name FROM Customer_LT
UNION
SELECT qty FROM order_details_lt;

select count(*),c_name from customer_LT,order_details_lt
where customer_lt.CID=order_details_lt.CID_1 group by c_name;

select sum(qty),c_name from customer_LT, order_details_LT
where customer_LT.CID=order_details_LT.CID_1 group by c_name;