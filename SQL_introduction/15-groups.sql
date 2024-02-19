-- In second table lists number of records with same score
-- Numbers of records should have the label number sorted in descending
SELECT score,
COUNT(*)
AS number FROM second_table
GROUP BY score
ORDER By number DESC;