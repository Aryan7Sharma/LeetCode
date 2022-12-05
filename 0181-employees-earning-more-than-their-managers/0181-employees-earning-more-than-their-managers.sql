# Write your MySQL query statement below
Select
    e1.name As Employee
From 
    Employee e1,employee e2
where 
    e1.managerId=e2.id And e1.salary>e2.salary;
