-- SQL script to list all the cities of California from the database hbtn_0d_usa
-- Select cities of California by filtering using the id of California fetched from the states table
SELECT *
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;
