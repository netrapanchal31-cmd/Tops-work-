-- 2nd may 
-- parameter means it given by users 
use tops_labtask

DELIMITER //
create function square (num  int)
returns int 
deterministic
begin 
declare ans int;
set ans:=num*num;
return ans;
end//
Delimiter ;

-- test wheter the function work or not-- dual is temporary table inbuilt  
select square (20) from dual;

-- applying in QTY 
select qty,square(qty) as 'Square of Quantity' from order_details_lt;

-- function that give me total price 

DELIMITER //

CREATE FUNCTION total_price(qty DECIMAL, price INT)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE ans_1 INT;
    SET ans_1 = qty * price;
    RETURN ans_1;
END //
DELIMITER ;

CREATE TABLE Calculate_total(
    name_product VARCHAR(50),
    qty_1 INT,
    product_price INT
);

INSERT INTO Calculate_total VALUES
('Laptop',65,50000),
('Phone',3,10000),
('Headphones',20,200),
('Tablet',7,30000),
('Makeup',3,50);

SELECT name_product,qty_1,product_price,total_price(qty_1,product_Price)
FROM Calculate_total;

-- rather than joining if we want data everytime use VIEW 
create view view_event as select client_name from client_master;
select * from view_event
