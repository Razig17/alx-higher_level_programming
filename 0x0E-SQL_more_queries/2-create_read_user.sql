-- SQL script to create the database hbtn_0d_2 and the user user_0d_2

-- Create the database hbtn_0d_2 and Create the user user_0d_2 and Grant SELECT privilege to user_0d_2 on the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
