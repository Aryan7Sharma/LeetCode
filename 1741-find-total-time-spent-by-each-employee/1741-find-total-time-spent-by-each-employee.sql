# Write your MySQL query statement below
Select
    event_day As day,
    emp_id,
    sum(out_time)-sum(in_time) As total_time
From
    Employees
Group BY event_day,emp_id