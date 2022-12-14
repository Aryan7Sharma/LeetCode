# Write your MySQL query statement below
Select 
    product_id,
    product_name
From
    Product
Where product_id in (select 
                            product_id 
                        from 
                            Sales 
                        Group By product_id
                        Having min(sale_date)>='2019-01-01' And max(sale_date)<='2019-03-31'
                        )