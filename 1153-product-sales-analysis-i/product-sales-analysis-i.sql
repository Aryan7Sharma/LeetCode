-- Write your PostgreSQL query statement below
select product_name,year,price
From Sales s
Left Join Product p
on s.product_id=p.product_id