CREATE DATABASE IF NOT EXISTS linkup_dev_db;
CREATE USER IF NOT EXISTS 'linkup_dev'@'localhost' IDENTIFIED BY 'linkup_dev_pwd';
GRANT ALL PRIVILEGES ON linkup_dev_db.* TO 'linkup_dev'@'localhost';
