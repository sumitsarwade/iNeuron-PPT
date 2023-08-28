-- Q 11 12 13 ANS

create database students;

use students;

-- Q11 ANS
-- Create Student table
CREATE TABLE Student (
    ID INT PRIMARY KEY NOT NULL,
    Name VARCHAR(20) NOT NULL,
    Age INT NOT NULL,
    Address VARCHAR(25)
);

-- Insert records with Indian names
INSERT INTO Student (ID, Name, Age, Address) VALUES
(1, 'Rahul Sharma', 20, '123 Main St'),
(2, 'Priya Patel', 22, '456 Elm Ave'),
(3, 'Amit Verma', 21, '789 Oak Rd'),
(4, 'Neha Gupta', 19, '567 Pine St'),
(5, 'Sandeep Kumar', 23, '890 Maple Ln');


-- Q12 ANS
SELECT Name, Age
FROM Student
ORDER BY Age ASC
LIMIT 1;


-- Q 13 ANS
SELECT
    p.FirstName,
    p.LastName,
    a.City,
    a.State
FROM
    Person p
JOIN
    Address a ON p.PersonId = a.PersonId;

