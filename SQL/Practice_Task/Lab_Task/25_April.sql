
use tops_labtask;

-- Create a right join

SELECT order_details_lt.*, product_lt.p_name, order_details_lt.qty
FROM order_details_lt
RIGHT JOIN product_lt
ON product_lt.PID = order_details_lt.PID_1;

-- Find number of orders by each product

SELECT PID_1, COUNT(*) AS number_of_orders
FROM order_details_lt
GROUP BY PID_1;

-- Find average of orders by each product

SELECT PID_1, AVG(qty) AS avg_of_orders
FROM order_details_lt
GROUP BY PID_1;