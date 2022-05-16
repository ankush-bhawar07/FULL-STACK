DROP DATABASE students; -- drop database
CREATE DATABASE students; -- create database
USE students; -- use database

CREATE TABLE student(
    student_id INT PRIMARY KEY,
    name VARCHAR(20),
    major VARCHAR(20)
); -- create table