-- SQL script to create a table called first_table in the current database

-- Check if the table first_table exists, and create it only if it does not exist
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
