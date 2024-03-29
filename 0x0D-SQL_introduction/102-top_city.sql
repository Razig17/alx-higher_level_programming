-- SQL script to display the top 3 cities temperature during July and August ordered by temperature (descending)
-- Select the city, calculate the average temperature in Fahrenheit, and order by temperature (descending)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
