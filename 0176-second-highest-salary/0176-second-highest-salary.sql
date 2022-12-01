# Write your MySQL query statement below
Select(
        select 
            distinct(salary)
        From 
            employee
        Order By Salary Desc 
        Limit 1
        OFFSET 1
    )
     AS SecondHighestSalary;