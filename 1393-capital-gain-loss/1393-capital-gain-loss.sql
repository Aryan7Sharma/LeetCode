# Write your MySQL query statement below
Select
    Stock_name,
    Sum(
        Case 
            When operation = 'Buy' Then -price 
            Else price
        End
        ) As capital_gain_loss
From
    Stocks
Group By 1;
    