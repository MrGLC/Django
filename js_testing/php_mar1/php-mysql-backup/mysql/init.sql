CREATE DATABASE IF NOT EXISTS backup_db;
USE backup_db;

CREATE TABLE IF NOT EXISTS test_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data VARCHAR(255) NOT NULL
);

INSERT INTO test_table (data) VALUES ('Sample data 1'), ('Sample data 2');

