-- Write your SQL Query here --
-- example: SELECT * FROM XX_TABLE WHERE XXX --
SELECT rooms.id, rent, name from rooms left join tenants on rooms.tenant_id = tenants.id