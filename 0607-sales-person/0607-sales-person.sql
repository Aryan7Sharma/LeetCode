# Write your MySQL query statement below
Select 
    name
From 
    SalesPerson
Where 
    SalesPerson.sales_id Not IN (Select 
        sales_id
    From 
        Orders o Inner join Company c
        On o.com_id=c.com_id
    Where name = "RED") 