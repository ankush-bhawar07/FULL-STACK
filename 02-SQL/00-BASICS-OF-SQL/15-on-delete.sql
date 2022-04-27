-- delete record ( on delete set null )
SELECT * FROM employee;
SELECT * FROM branch;
DELETE FROM employee WHERE emp_id = 102;
SELECT * FROM employee;
SELECT * FROM branch;


-- delete record ( on delete cascade 
SELECT * FROM branch;
SELECT * FROM branch_supplier;
-- DELETE FROM employee WHERE emp_id = 102;
DELETE FROM branch WHERE branch_id = 2;
SELECT * FROM branch;
SELECT * FROM branch_supplier;