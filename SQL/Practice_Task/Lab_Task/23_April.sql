use tops_labtask;
Create table Customer_LT (CID int primary key, c_name varchar(20), Address varchar(20));
Create table product_LT (PID int primary key,p_name varchar(20),descrpition varchar(100),price decimal(20));
create table order_details_LT (OID int primary key, CID_1 int,PID_1 int, qty int, or_date date, 
foreign key (CID_1) references Customer_LT(CID),
foreign key (PID_1) references product_LT (PID));

insert into Customer_LT values 
(1,'Aarav','Ahmedabad'),
(2,'Riya','Surat'),
(3,'Kunal','Vadodara'),
(4,'Neha','Rajkot'),
(5,'Rahul','Mumbai'),
(6,'Priya','Delhi'),
(7,'Arjun','Jaipur'),
(8,'Kavya','Kochi'),
(9,'Aman','Lucknow'),
(10,'Sneha','Chandigarh');
 
 select * from Customer_LT;
 
insert into Product_LT values 
(101, "Laptop", "High performance laptop for work & study", 55000),
(102, "Smartphone", "Latest Android smartphone with great camera", 25000),
(103, "Headphones", "Noise-cancelling wireless headphones", 3500),
(104, "Backpack", "Durable backpack for travel and college", 1200),
(105, "Smartwatch", "Fitness tracking smartwatch with Bluetooth", 4500);

INSERT INTO order_details_lt (oid, CID_1, PID_1, qty, or_date) VALUES
(441, 1, 101, 2, '2024-01-01'),
(542, 2, 102, 5, '2024-01-02'),
(673, 3, 103, 1, '2024-01-03'),
(134, 4, 104, 4, '2024-01-04'),
(465, 5, 105, 2, '2024-01-05'),

(656, 6, 101, 3, '2024-01-06'),
(167, 7, 102, 6, '2024-01-07'),
(638, 8, 103, 2, '2024-01-08'),
(349, 9, 104, 5, '2024-01-09'),
(130, 10, 105, 1, '2024-01-10'),

(131, 1, 101, 4, '2024-01-11'),
(122, 2, 102, 2, '2024-01-12'),
(153, 3, 103, 3, '2024-01-13'),
(104, 4, 104, 7, '2024-01-14'),
(185, 5, 105, 2, '2024-01-15'),

(176, 6, 101, 5, '2024-01-16'),
(157, 7, 102, 1, '2024-01-17'),
(198, 8, 103, 6, '2024-01-18'),
(139, 9, 104, 2, '2024-01-19'),
(280, 10, 105, 4, '2024-01-20');
select * from order_Details_lt;
-- fetch order details with product name and customer name 

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

SELECT order_details_lt.*, customer_lt.c_name, order_details_lt.qty
FROM customer_lt
LEFT JOIN order_details_lt 
ON customer_lt.CID = order_details_lt.CID_1;

select count(*),c_name from customer_LT,order_details_lt
where customer_lt.CID=order_details_lt.CID_1 group by c_name;

select sum(qty),c_name from customer_LT, order_details_LT
where customer_LT.CID=order_details_LT.CID_1 group by c_name;


