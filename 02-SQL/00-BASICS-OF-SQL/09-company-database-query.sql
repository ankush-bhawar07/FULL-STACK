-- find all records from  tables
SELECT * FROM employee;
SELECT * FROM branch;
SELECT * FROM client;
SELECT * FROM works_with;
SELECT * FROM branch_supplier;

-- find all employee ordered by salary
SELECT * FROM employee ORDER BY salary;
SELECT * FROM employee ORDER BY salary DESC;

-- find all employees ordered by sex then name
SELECT * FROM employee ORDER BY sex, first_name, last_name;

-- find the first five employee in the table
SELECT * FROM employee LIMIT 5;

-- find the first and last name of all the employees
SELECT first_name, last_name FROM employee;

-- find the forename and surname of all the employees
SELECT first_name AS forename, last_name AS surname FROM employee;

-- find out all the difrent genders
SELECT DISTINCT sex FROM employee;