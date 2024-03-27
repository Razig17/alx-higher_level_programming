-- SQL script to list all records of the table second_table from the database hbtn_0c_0
-- Select the score and name for rows where name is not null, and order by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
