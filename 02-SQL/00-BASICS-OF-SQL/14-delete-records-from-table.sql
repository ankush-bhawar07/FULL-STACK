USE coders;

DELETE FROM coder WHERE cid = 7;
SELECT * FROM coder;

DELETE FROM coder WHERE name = "John Doe" AND lang = "Java";
SELECT * FROM coder;

DELETE FROM coder; -- delete all records
SELECT * FROM coder;