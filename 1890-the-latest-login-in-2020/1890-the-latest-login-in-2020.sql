# Write your MySQL query statement below
Select
    user_id,
    max(time_stamp) As last_stamp
From
    Logins
Where time_stamp Like '2020%'
Group By user_id