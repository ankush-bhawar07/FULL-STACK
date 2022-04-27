DROP DATABASE students; -- drop database

CREATE DATABASE students; -- create database

use students; -- use database

CREATE TABLE student (
    student_id INT PRIMARY KEY,
    name VARCHAR(20),
    major VARCHAR(20)
); -- create table

DESCRIBE student; -- descibe table

ALTER TABLE student ADD gpa DECIMAL(3, 2); -- add column to table

DESCRIBE student; 

ALTER TABLE student DROP COLUMN gpa; -- drop column from table

DESCRIBE student;