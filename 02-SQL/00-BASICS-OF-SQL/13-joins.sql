-- INSERT INTO branch VALUES(4, 'buffalo', NULL, NULL);
-- find all branches and the names of their managers
-- noraml join
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
JOIN branch
ON employee.emp_id = branch.mgr_id;

-- left join
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
LEFT JOIN branch
ON employee.emp_id = branch.mgr_id;

-- right join
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
RIGHT  JOIN branch
ON employee.emp_id = branch.mgr_id;