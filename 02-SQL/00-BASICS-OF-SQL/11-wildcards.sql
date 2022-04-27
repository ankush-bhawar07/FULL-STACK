-- % = any # charecters, _ = one charecter
-- find any client's who are an LLC
SELECT * FROM client WHERE client_name LIKE '%LLC';

-- find any branch suppliers who are in the lable business
SELECT * FROM branch_supplier WHERE supplier_name LIKE '% Label%';

-- find any employee born in october
SELECT * FROM employee  WHERE birth_day LIKE '____-10%';

-- find any clients who are school
SELECT * FROM client WHERE client_name LIKE ('%school%');