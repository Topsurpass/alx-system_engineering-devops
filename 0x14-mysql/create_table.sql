-- Set up replication and  have a database with at least one table
-- and one row in your primary MySQL server (web-01) to replicate from.

CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (
	id INT PRIMARY KEY,
	name VARCHAR(255)
);
INSERT INTO nexus6 (id, name) VALUES(1, "Leon");
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
SELECT * FROM nexus6;
