- SQL script to display the maximum temperature of each state ordered by state name
SELECT state, MAX(value) as max_temp FROM temperatures
GROUP BY state
ORDER BY state;
