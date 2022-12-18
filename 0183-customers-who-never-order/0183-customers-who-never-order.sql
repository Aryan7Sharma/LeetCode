# Write your MySQL query statement below
Select
    name AS Customers
From 
    Customers
Where
 id not in (Select CustomerID from Orders);
    
