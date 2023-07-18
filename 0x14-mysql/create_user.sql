-- Create new user and grant REPLICATE CLIENT Privilege

CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'holberton_user'@'localhost'
