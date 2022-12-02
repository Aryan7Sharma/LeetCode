# Write your MySQL query statement below
Select
    activity_date AS day,
    count(Distinct user_id) AS active_users
From 
    Activity
Where 
    activity_date between '2019-06-28' And '2019-07-27'
Group By activity_date
Order By activity_date