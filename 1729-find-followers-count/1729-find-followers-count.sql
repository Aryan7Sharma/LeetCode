# Write your MySQL query statement below
Select 
    user_id,
    count(follower_id) AS followers_count
From
    Followers
Group BY user_id
Order By 1;