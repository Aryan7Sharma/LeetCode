Select product_id, 10 as price From Products where (product_id) not in (Select product_id from Products where change_date<='2019-08-16' Group By product_id)
Union 
Select product_id,new_price as price From Products where (product_id,change_date) in (Select product_id,max(change_date) from Products where change_date<='2019-08-16' Group By product_id)

Order By product_id