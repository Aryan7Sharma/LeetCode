# Write your MySQL query statement below
select st.student_id,
st.student_name,
sub.subject_name,
count(ex.subject_name) as attended_exams
From Students st
Cross Join Subjects sub
left join Examinations ex
on ex.student_id = st.student_id
and ex.subject_name = sub.subject_name
group by st.student_id,sub.subject_name
order by st.student_id,sub.subject_name;