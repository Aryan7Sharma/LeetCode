# Write your MySQL query statement below
select 
    a.id
From 
    weather a, weather b
Where 
    Datediff(a.recordDate, b.recordDate) = 1 
    And a.temperature>b.temperature