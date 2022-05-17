USE coders;

UPDATE coder SET lang = "JavaScript" WHERE cid = 2;
UPDATE coder SET lang = "PHP" WHERE lang = "undecided";
UPDATE coder SET name = "John Doe", lang = "Java" WHERE cid = 1;
SELECT * FROM coder;