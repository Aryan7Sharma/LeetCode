# Write your MySQL query statement below
Select
    customer_number
From
    (
        Select
            customer_number,
            count(order_number) as total_order  
        From
            Orders
        Group BY customer_number
        Order BY total_order DESC
        Limit 1
    )t2
