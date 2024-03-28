-- SQL script to create the database hbtn_0d_usa and the table states
-- Create the database hbtn_0d_usa if it does not already exist
-- Create the table states if it does not already exist

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(256) NOT NULL
);
