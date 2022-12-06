# Write your MySQL query statement below
Select
    *
From
    Cinema
Where 
    id%2!=0 And description<>'boring'
Order By rating DESC;