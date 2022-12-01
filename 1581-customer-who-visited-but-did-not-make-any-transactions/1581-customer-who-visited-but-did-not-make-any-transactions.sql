# Write your MySQL query statement below
Select 
    customer_id,
    count(customer_id) AS count_no_trans
From
        (Select
                customer_id
        From Visits v Left Join Transactions t
            ON v.visit_id=t.visit_id
        Where transaction_id is Null
        ) t2
Group BY customer_id
    