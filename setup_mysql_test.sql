CREATE DATABASE IF NOT EXISTS linkup_test_db;
CREATE USER IF NOT EXISTS 'linkup_test'@'localhost' IDENTIFIED BY 'linkup_test_pwd';
GRANT ALL PRIVILEGES ON linkup_test_db.* TO 'linkup_test'@'localhost';
