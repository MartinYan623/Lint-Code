-- Write your SQL Query here --
-- example: SELECT * FROM XX_TABLE WHERE XXX --
select student_name, phone, hometown, address from students left join enrollments on students.id = enrollments.student_id