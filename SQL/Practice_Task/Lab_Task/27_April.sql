-- 27th april (Labtask)

use tops_labtask;
CREATE TABLE client_master (
    client_id INT PRIMARY KEY,
    client_name VARCHAR(50),
    city VARCHAR(50),
    email VARCHAR(100),
    join_date DATE
);

CREATE TABLE product_catalog (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(30),
    price DECIMAL(10,2),
    stock INT
);

CREATE TABLE sales_orders (
    order_id INT PRIMARY KEY,
    client_id INT,
    order_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (client_id) REFERENCES client_master(client_id)
);

CREATE TABLE Final_order_details (
    order_detail_id INT PRIMARY KEY,
    order_id_1 INT,
    product_id_1 INT,
    quantity INT,
    FOREIGN KEY (order_id_1) REFERENCES sales_orders(order_id),
    FOREIGN KEY (product_id_1) REFERENCES product_catalog(product_id)
);

INSERT INTO client_master VALUES
(1, 'Amit Sharma', 'Delhi', 'amit@gmail.com', '2022-01-15'),
(2, 'Sneha Patel', 'Mumbai', 'sneha@gmail.com', '2023-03-10'),
(3, 'Rahul Mehta', 'Ahmedabad', 'rahul@gmail.com', '2024-01-05'),
(4, 'Simran Kaur', 'Mumbai', 'simran@gmail.com', '2022-11-20'),
(5, 'Suresh Kumar', 'Chennai', 'suresh@gmail.com', '2023-07-15');

INSERT INTO product_catalog VALUES
(101, 'Laptop', 'Electronics', 65000, 50),
(102, 'Phone', 'Electronics', 30000, 100),
(103, 'Headphones', 'Electronics', 2000, 200),
(104, 'Table', 'Furniture', 7000, 30),
(105, 'Chair', 'Furniture', 3000, 50);

INSERT INTO sales_orders VALUES
(1001, 1, '2024-05-20', 'Delivered'),
(1002, 2, '2024-08-10', 'Delivered'),
(1003, 3, '2024-08-15', 'Cancelled'),
(1004, 1, '2024-01-12', 'Delivered'),
(1005, 4, '2024-08-25', 'Delivered');

INSERT INTO final_order_details VALUES
(1, 1001, 101, 1),
(2, 1002, 102, 2),
(3, 1002, 103, 3),
(4, 1003, 104, 1),
(5, 1004, 101, 1),
(6, 1005, 103, 2),
(7, 1005, 105, 1);

-- Basic level

-- 1)Show all customers who live in Mumbai.
SELECT * FROM client_master
WHERE city = 'Mumbai';

-- 2)Display names of all products in the “Electronics” category. 
SELECT product_name
FROM product_catalog
WHERE category = 'Electronics';

-- 3)List all orders that were delivered.
SELECT * FROM sales_orders
WHERE status = 'Delivered';

-- 4)Find customers who joined after January 2023. 
SELECT * FROM client_master
WHERE join_date > '2023-01-01';

-- 5)Display products whose price is greater than ₹10,000. 
SELECT * FROM product_catalog
WHERE price > 10000;

-- 6)Show the total number of customers. 
SELECT COUNT(*) FROM client_master;

-- 7)Display product names with their stock quantity. 
SELECT product_name, stock
FROM product_catalog;

-- 8)List orders placed in August 2024. 
SELECT * FROM sales_orders
WHERE order_date BETWEEN '2024-08-01' AND '2024-08-31';

-- 9)Show customers whose name starts with “S”. 
SELECT * FROM client_master
WHERE client_name LIKE 'S%';

-- 10)Display the cheapest product.
SELECT * FROM product_catalog
ORDER BY price ASC;

-- Intermediate Level

-- 1)Count how many orders each customer has placed.
SELECT client_id, COUNT(order_id) AS total_orders
FROM sales_orders
GROUP BY client_id;

-- 2)Find the total quantity of products ordered in each order.
SELECT order_id_1, SUM(quantity) AS total_quantity
FROM final_order_details
GROUP BY order_id_1;

-- 3)Show each customer’s name and the total value of their delivered orders.


-- 4)Display the most expensive product in each category.
SELECT category, MAX(price) AS highest_price
FROM product_catalog
GROUP BY category;

-- 5)Find customers who have never placed an order.

-- 6)Show total sales (price × quantity) of each product.
SELECT product_name,
SUM(price * quantity) AS total_sales
FROM product_catalog 
JOIN final_order_details f ON product_id = product_id_1
GROUP BY product_name;

-- 7)List all products that have been ordered more than 2 times.
SELECT product_id_1, SUM(quantity) AS total_qty
FROM final_order_details
GROUP BY product_id_1
WHERE SUM(quantity) > 2;

-- 8)Find the total revenue generated in 2024.

-- 9)Display all orders along with customer names and order status.
SELECT order_id, client_name, status
FROM sales_orders 
JOIN client_master c ON client_id = client_id;

-- 10)Show the number of “Delivered” vs “Cancelled” orders.
SELECT status, COUNT(*) AS total
FROM sales_orders
GROUP BY status;


-- Advanced Level

-- Find the top 3 customers with the highest total spending. 

-- Display the product categories ranked by total sales.

-- Find customers who have purchased both “Laptop” and “Headphones”.

-- Show products that were never ordered.

-- Find orders with multiple products from different categories.

-- Calculate each month’s total revenue and show a running total.

-- Display the average order value per customer.

-- Show the most frequently ordered product.

-- List customers who placed orders in at least 3 different months.

-- Find products that are out of stock or nearly out of stock (less than 10 units).
SELECT * FROM product_catalog
WHERE stock < 10;
