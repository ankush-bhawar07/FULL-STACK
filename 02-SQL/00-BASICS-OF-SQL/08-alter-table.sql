USE students; -- use database
ALTER TABLE student ADD gpa DECIMAL(3, 2); -- add gpa column to table

ALTER TABLE student DROP COLUMN gpa; -- drop gpa column from table