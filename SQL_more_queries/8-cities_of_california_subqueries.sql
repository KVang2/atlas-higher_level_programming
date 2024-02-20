-- List all cities of california found in the database
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id =
(
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY cities.id ASC;