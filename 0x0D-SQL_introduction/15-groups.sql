-- SQL script to list the number of records with the same score in the table second_table from the database hbtn_0c_0
-- Select the score and the count of records for each score, and order by the number of records (descending)
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
