-- primary-replica synchronization
-- Replicas can connect using any MySQL user profile that exists on the source
-- database and has the appropriate privileges
-- On your primary MySQL server (web-01), create a new user for the replica server.

CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'vagrant';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
