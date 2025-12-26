# Write your MySQL query statement below
Select id,
Case
    When p_id is null Then 'Root'
    When id in (select p_id from Tree where P_id is not null) Then 'Inner'
    Else 'Leaf'
End as type
From Tree;