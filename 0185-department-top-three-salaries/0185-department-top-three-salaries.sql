# Write your MySQL query statement below
With t2 AS (Select
    name AS Employee,
    salary,
    departmentId,
    Dense_Rank() Over(Partition By departmentId Order By salary Desc) As sal_rank
From
    Employee)
Select 
    name As Department,
    Employee,
    salary
From 
    t2 Left Join Department d
    ON t2.departmentId=d.id
Where sal_rank in (1,2,3);
    
