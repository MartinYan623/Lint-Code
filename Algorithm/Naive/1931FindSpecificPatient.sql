-- Write your SQL Query here --
-- example: SELECT * FROM XX_TABLE WHERE XXX --
SELECT name from patients where infected_by_id!=2 or infected_by_id is null