# Write your MySQL query statement below
Select
    name,
    sum(amount) AS balance
From
    Transactions t Left Join Users u
    ON t.account=u.account
Group BY t.account
having balance>10000;