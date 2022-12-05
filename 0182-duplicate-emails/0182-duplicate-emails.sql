# Write your MySQL query statement below
select
    Distinct p2.email As Email
From
    Person p1, person p2
Where
    p1.email=p2.email And p2.id>p1.id;