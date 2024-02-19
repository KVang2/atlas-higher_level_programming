-- Lists all records with score >= 10
-- Display both score name in order in second table
SELECT name, score
FROM second_table
WHERE score >= 10
ORDER BY score DESC;