# Write your MySQL query statement below
Select
    user_id As buyer_id,
    join_date,
    count(buyer_id) As orders_in_2019
From Users u Left Join
                    (
                        Select 
                            *
                        From
                            Orders
                        Where Year(order_date)=2019    
                    ) o
                    ON u.user_id = o.buyer_id
Group By user_id;