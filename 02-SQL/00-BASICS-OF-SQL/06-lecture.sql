INSERT INTO student(name, major) VALUES('XYZ', 'stats');
INSERT INTO student(name, major) VALUES('abc', 'BA');
INSERT INTO student(name, major) VALUES('johnDoe', 'cs');

SELECT * FROM student;
SELECT name FROM student;
SELECT student_id FROM student;
SELECT major FROM student;
SELECT name, major FROM student;
SELECT name, major FROM student WHERE student_id = 1;
SELECT * FROM student ORDER BY name;
SELECT * FROM student ORDER BY name DESC;

SELECT * FROM student ORDER BY major, student_id;

SELECT * FROM student ORDER BY student_id DESC LIMIT 2;

SELECT student_id, major FROM student WHERE major = 'cs' ORDER BY student_id DESC LIMIT 2;

SELECT * FROM student WHERE major IN ('cs', 'science');