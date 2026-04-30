-- 28th april 

USE tops_labtask;

CREATE TABLE Course_Master (
    cid INT PRIMARY KEY,
    cname VARCHAR(100),
    fees DECIMAL(10,2)
);

CREATE TABLE Student_Master (
    sid INT PRIMARY KEY,
    sname VARCHAR(100),
    address VARCHAR(150),
    contact_number VARCHAR(15)
);

CREATE TABLE Enrollment_Records (
    eid INT PRIMARY KEY,
    cid INT,
    sid INT,
    enrolment_date DATE,
    
    FOREIGN KEY (cid) REFERENCES Course_Master(cid),
    FOREIGN KEY (sid) REFERENCES Student_Master(sid)
);

INSERT INTO Course_Master (cid, cname, fees) VALUES
(1, 'Web Development', 25000),
(2, 'Data Science', 30000),
(3, 'Cyber Security', 28000),
(4, 'Digital Marketing', 20000),
(5, 'UI/UX Design', 22000),
(6, 'Cloud Computing', 32000),
(7, 'AI & ML', 35000),
(8, 'Software Testing', 18000),
(9, 'DevOps', 33000),
(10, 'Mobile App Development', 27000);

INSERT INTO Student_Master (sid, sname, address, contact_number) VALUES
(101, 'Netra', 'Ahmedabad', '9016217332'),
(102, 'Krish', 'Gota', '8907654321'),
(103, 'Neha', 'Satellite', '9876543210'),
(104, 'Lata', 'Navrangpura', '9123456780'),
(105, 'Neel', 'Maninagar', '9988776655'),
(106, 'Tamana', 'Bopal', '9090909090'),
(107, 'Bhavesh', 'Vastrapur', '9111222233'),
(108, 'Mahesh', 'Chandkheda', '9222333444'),
(109, 'Krunal', 'Paldi', '9333444555'),
(110, 'Niyati', 'SG Highway', '9444555666');

INSERT INTO Enrollment_Records (eid, cid, sid, enrolment_date) VALUES
(1, 1, 101, '2024-01-10'),
(2, 2, 102, '2024-01-11'),
(3, 3, 103, '2024-01-12'),
(4, 4, 104, '2024-01-13'),
(5, 5, 105, '2024-01-14'),
(6, 6, 106, '2024-01-15'),
(7, 7, 107, '2024-01-16'),
(8, 8, 108, '2024-01-17'),
(9, 9, 109, '2024-01-18'),
(10, 10, 110, '2024-01-19');

CREATE TABLE Department (
    Did INT PRIMARY KEY,
    dname VARCHAR(50)
);

CREATE TABLE Employee (
    eid INT PRIMARY KEY,
    ename VARCHAR(50),
    email VARCHAR(50),
    salary DECIMAL(10,2),
    join_date DATE,
    did INT,
    FOREIGN KEY (did) REFERENCES Department(Did)
);

INSERT INTO Department VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Finance'),
(4, 'Marketing'),
(5, 'Sales');

INSERT INTO Employee VALUES
(101, 'NETRA', 'netra@gmail.com', 25000, '2022-01-10', 1),
(102, 'NEHA', 'neha@gmail.com', 30000, '2021-03-15', 2),
(103, 'KRISH', 'krish@gmail.com', 28000, '2020-07-20', 3),
(104, 'LATA', 'lata@gmail.com', 35000, '2019-11-05', 4),
(105, 'SAURABH', 'saurabh@gmail.com', 27000, '2023-02-18', 5),

(106, 'KAVYA', 'kavya@gmail.com', 32000, '2021-08-12', 1),
(107, 'MASUM', 'masum@gmail.com', 40000, '2018-06-25', 2),
(108, 'RIYA', 'riya@gmail.com', 29000, '2022-09-30', 3),
(109, 'NEEL', 'neel@gmail.com', 36000, '2020-12-14', 4),
(110, 'NIYATI', 'niyati@gmail.com', 31000, '2023-01-22', 5),

(111, 'FENIL', 'fenil@gmail.com', 33000, '2021-05-17', 1),
(112, 'YASH', 'yash@gmail.com', 37000, '2019-10-10', 2),
(113, 'ROHIT', 'rohit@gmail.com', 26000, '2022-04-08', 3),
(114, 'HARSH', 'harsh@gmail.com', 34000, '2020-03-19', 4),
(115, 'DEV', 'dev@gmail.com', 38000, '2018-07-11', 5);