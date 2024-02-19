-- Lists number or records with same score in second table
-- Score should be display in descending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;