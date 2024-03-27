-- SQL script to create the MySQL server user user_0d_1

-- Create the user user_0d_1 if it does not already exist and Grant all privileges to user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
