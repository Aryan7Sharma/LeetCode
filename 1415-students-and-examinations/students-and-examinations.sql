# Write your MySQL query statement below
select stsub.student_id,
stsub.student_name,
stsub.subject_name,
count(ex.subject_name) as attended_exams
from (Select * From Students st
Cross Join Subjects sub) as stsub 
left join Examinations ex
on ex.student_id = stsub.student_id
and ex.subject_name = stsub.subject_name
group by stsub.student_id,stsub.subject_name
order by stsub.student_id,stsub.subject_name;