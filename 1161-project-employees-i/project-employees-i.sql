-- Write your PostgreSQL query statement below
select project_id,round(cast(sum(experience_years) as decimal)/count(project_id), 2) as average_years
From Project p join Employee e
on p.employee_id=e.employee_id
group by project_id