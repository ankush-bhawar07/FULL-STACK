-- find the number of employees
SELECT COUNT(emp_id) FROM employee;
SELECT COUNT(super_id) FROM employee;

-- find the number of female employees born after 1970
SELECT COUNT(emp_id) FROM employee WHERE sex = 'F' AND birth_day > '1970-01-01';

-- find the avarage of all employees salaries
SELECT AVG(salary) FROM employee;

SELECT AVG(salary) FROM employee WHERE sex = 'M';
SELECT AVG(salary) FROM  employee WHERE sex = 'F';

-- find the sum of all employee's salaries
SELECT SUM(salary) FROM employee;

-- find out how many males and females there are
SELECT COUNT(SEX), sex FROM employee GROUP BY sex;

-- find the totals of each salesman
SELECT SUM(total_sale), emp_id FROM works_with GROUP BY emp_id;
SELECT SUM(total_sale), client_id FROM works_with GROUP BY client_id;