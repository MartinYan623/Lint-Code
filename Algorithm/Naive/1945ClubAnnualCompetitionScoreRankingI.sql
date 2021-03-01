-- Write your SQL Query here --
-- example: SELECT * FROM XX_TABLE WHERE XXX --
SELECT name, year, score from rankings, categories WHERE rankings.category_id = categories.id