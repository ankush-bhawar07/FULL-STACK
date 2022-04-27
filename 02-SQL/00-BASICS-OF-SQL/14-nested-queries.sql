-- find names of all employees who have
-- sold over 30,000 to a single client

SELECT employee.first_name, employee.last_name
FROM employee
WHERE employee.emp_id IN (
    SELECT works_with.emp_id FROM works_with
    WHERE works_with.total_sale > 30000
);

-- find all clients wo are handeled by the branch
-- that Michal Scott manages
-- assume you know Michal's id

SELECT client.client_name
FROM client
WHERE client.branch_id = (
SELECT branch.branch_id
FROM branch
WHERE branch.mgr_id = 102
LIMIT 1
);
