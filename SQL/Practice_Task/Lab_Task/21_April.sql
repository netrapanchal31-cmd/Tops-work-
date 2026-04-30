USE tops_labtask;
CREATE TABLE STUDENTS (
student_id INT PRIMARY KEY,
			name_students VARCHAR(50),
			age INT,
			grade VARCHAR(5),
			city VARCHAR(50),
			marks INT
);

INSERT INTO STUDENTS(student_id,name_students,age,grade,city,marks)
  VALUES
(101,'Netra',21,'A','Ahmedabad',95),
(102,'Neel',20,'A','Mumbai',80),
(103,'Krish',22,'B','Pune',75),
(104,'Lata',18,'B','Delhi',70),
(105,'Krunal',17,'C','Mumbai',65),
(106,'Angle','20','A','Mumbai',85),
(107,'Anuj',26,'B','Ahmedabad',76),
(108,'Riya',20,'C','Ahmedabad',65),
(109,'Neha',25,'B','Delhi',76),
(110,'Anket',32,'C','Pune',63);

SELECT * FROM STUDENTS;

-- Display only the names and ages of students.
SELECT name_students,age FROM STUDENTS;

-- Show details of students who live in Ahmedabad.
SELECT * FROM STUDENTS WHERE city= 'Ahmedabad';

-- List all students with grade 'A'.
SELECT * FROM STUDENTS WHERE grade='A';

-- Find students who scored more than 80 marks.
SELECT * FROM STUDENTS WHERE marks >= 80;

-- Display students aged between 18 and 21.
SELECT * FROM STUDENTS WHERE age BETWEEN 18 AND 21;

-- List students who are from Mumbai and have marks above 70.
SELECT * FROM STUDENTS WHERE city= 'Mumbai' AND marks >= 70;

-- Find students whose names start with the letter 'A'.
SELECT * FROM STUDENTS WHERE name_students like 'A%';

-- Display all students sorted by marks in descending order.
select * from STUDENTS order by name_students desc;

--  List students sorted by age in ascending order.
SELECT * FROM STUDENTS ORDER BY age ASC;

--  Show students sorted by city and then by marks (highest first).
SELECT * FROM STUDENTS ORDER BY city ASC, marks DESC;