-- SQL script to lists all records with a score >= 10 in the table second_table
-- Select score and name columns from the second_table and Filter results where score is greater than or equal to 10 and Order results by score in descending order
SELECT score, name FROM second_table WHERE score >= 10
ORDER BY score DESC;
