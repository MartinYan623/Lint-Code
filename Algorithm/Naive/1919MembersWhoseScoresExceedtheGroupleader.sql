-- Write your SQL Query here --
-- example: SELECT * FROM XX_TABLE WHERE XXX --
SELECT name from group_members as a WHERE score > (SELECT score from group_members as b
where a.group_leader_id = b.id)
