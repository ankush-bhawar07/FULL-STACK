DROP DATABASE students;

CREATE DATABASE students;
USE students;

CREATE TABLE student(
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL UNIQUE,
    major VARCHAR(20) DEFAULT 'undecided'
);
DESCRIBE student;

-- insert records into table
INSERT INTO student(name, major) VALUES('John Doe', 'Mathematics');
INSERT  INTO student(name, major) VALUES('John Doe2', 'Biology');
INSERT INTO student(name) VALUES('John Doe3');
INSERT INTO student(name, major) VALUES('John Doe4', 'Computer Science');
SELECT * FROM student;

-- update records
UPDATE student SET major = 'Bio' WHERE major = "Biology";
UPDATE student SET major = 'Comp Sci' WHERE student_id = 4;
UPDATE student SET major = 'Science' WHERE major = 'Mathematics' OR major = 'Comp Sci';
UPDATE student SET name = "John", major = 'cs' WHERE student_id = 1;
SELECT *FROM student;

-- delete row
-- DELETE FROM student; delete all rows

DELETE FROM student WHERE student_id = 3;

DELETE FROM student WHERE name = 'John Doe2' AND major = 'Bio';
SELECT * FROM student;