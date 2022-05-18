DROP DATABASE menagerie;
CREATE DATABASE menagerie;
USE menagerie;

CREATE TABLE pet(
    name VARCHAR(20), 
    owner VARCHAR(20), 
    species VARCHAR(20),
    sex CHAR(1),
    birth DATE,
    death DATE
);

LOAD DATA LOCAL INFILE '16-load-data-from-file/pet.txt' INTO TABLE pet
  FIELDS TERMINATED BY ' ' LINES TERMINATED BY '\n';
