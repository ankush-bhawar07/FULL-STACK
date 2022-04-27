-- find a list of employee and branch names;
SELECT first_name AS difrent_names FROM employee 
UNION 
SELECT branch_name FROM branch
UNION 
SELECT client_name FROM client;

-- find a list of all client and branch suppliers names
SELECT client_name AS client_and_branch_suppliers, client.branch_id FROM client
UNION
SELECT supplier_name, branch_supplier.branch_id FROM branch_supplier;

-- find a list of all money spent or earned by the company
SELECT salary AS total_in_out FROM employee
UNION
SELECT total_sale FROM works_with;