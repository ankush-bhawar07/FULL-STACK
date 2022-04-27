DROP DATABASE students;

CREATE DATABASE students;

use students;

CREATE TABLE student (
    student_id INT PRIMARY KEY AUTO_INCREMENT ,
    name VARCHAR(20) NOT NULL UNIQUE,
    major VARCHAR(20)  DEFAULT 'undecided'
);
DESCRIBE student;

INSERT INTO student(name, major) VALUES('John', 'Biology');
SELECT * FROM student;

INSERT INTO student(name, major) VALUES('John2', 'Mathematics');
SELECT * FROM student;

INSERT INTO student(name) VALUES('John3');
SELECT * FROM student;

INSERT INTO student(name) VALUES('John4');
SELECT * FROM student;