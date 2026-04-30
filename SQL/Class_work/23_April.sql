
-- 23 april 

use Tops_Labtask;

create table customer(
cust_name varchar(20),
cust_num decimal(10),
cust_address varchar(30),
cust_email varchar(20)
);
ALTER TABLE customer
MODIFY cust_email VARCHAR(100);

ALTER TABLE customer
MODIFY cust_num DECIMAL(10,0);

INSERT INTO customer (cust_name, cust_num, cust_address, cust_email) VALUES
('Netra',9016217332,'ranip','netra@email.com'),
('Krish',8907654321,'Gota','krish@email.com'),
('Lata',8765678907,'S.G Highway','lata@email.com'),
('Neha',1324562314,'New ranip','neha@email.com'),
('Niyati',9870090098,'Vastral','niyati@email.com'),
('Krunal',8899776655,'Nardo','krunal@email.com'),
('Zayan',9876501234,'Ahmedabad','zayan.kapoor@gmail.com'),
('Aarohi',9123405678,'Surat','aarohi.trivedi@gmail.com'),
('Vivaan',9988701122,'Vadodara','vivaan.oberoi@gmail.com'),
('Myra',9012304567,'Rajkot','myra.bhatt@gmail.com'),
('Ishaan',9090807060,'Pune','ishaan.k@gmail.com'),
('Kiara',8888701234,'Mumbai','kiara.f@gmail.com'),
('Reyansh',7777609876,'Delhi','reyansh.m@gmail.com'),
('Anika',9666504321,'Hyderabad','anika.reddy@gmail.com'),
('Kabir',9555406789,'Chandigarh','kabir.anand@gmail.com'),
('Saanvi',9444301234,'Kochi','saanvi.nair@gmail.com');


-- fetch a at ending
select * from customer where cust_name like '%a';

-- fetch record of the customer whose name having letter u
select * from customer where cust_name like '%u%';

-- fetch record of  customer whose name having 5 letters
select * from customer where cust_name like '_____';

-- fetch record of  customer whose name starts with k and ends with l
select * from customer where cust_name like 'k%l';

-- fetch record of  customer whose name second letter  must be r
select * from customer where cust_name like '_r%';
