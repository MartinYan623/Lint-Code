-- Write your SQL Query here --
-- example: SELECT * FROM XX_TABLE WHERE XXX --
select name from users where users.id not in (select user_id from recharges)