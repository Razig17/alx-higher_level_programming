-- SQL script to list all cities with corresponding state names from the database hbtn_0d_usa
-- Select cities along with their corresponding state names using a JOIN operation
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
