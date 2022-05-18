USE coders;

INSERT INTO coder(name, lang) VALUES("John", "Python");
INSERT INTO coder(name, lang) VALUES("John Doe", "PHP");
INSERT INTO coder(name, lang) VALUES("Jack", "Java");
INSERT INTO coder(name, lang) VALUES("Sam", "JavaScript");

SELECT * FROM coder;
SELECT NAME FROM coder;
SELECT cid FROM coder;
SELECT lang FROM coder;
SELECT name, lang FROM coder;
SELECT name, lang FROM coder WHERE cid = 11;
SELECT * FROM coder ORDER BY name;
SELECT * FROM coder ORDER BY name DESC;
SELECT * FROM coder ORDER BY name, cid;
SELECT * FROM coder ORDER BY cid DESC LIMIT 2;
SELECT cid, lang FROM coder WHERE lang = "Python" ORDER BY cid DESC LIMIT 2;
SELECT * FROM coder WHERE lang In("Python", "Java");