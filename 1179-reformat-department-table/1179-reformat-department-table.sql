# Write your MySQL query statement below
Select
    id,
    Sum(IF(month = 'Jan', revenue, null)) AS Jan_Revenue,
    Sum(IF(month = 'Mar', revenue, null)) AS Mar_Revenue,
    Sum(IF(month = 'Feb', revenue, null)) AS Feb_Revenue,
    Sum(IF(month = 'Apr', revenue, null)) AS Apr_Revenue,
    Sum(IF(month = 'May', revenue, null)) AS May_Revenue,
    Sum(IF(month = 'Jun', revenue, null)) AS Jun_Revenue,
    Sum(IF(month = 'Jul', revenue, null)) AS Jul_Revenue,
    Sum(IF(month = 'Aug', revenue, null)) AS Aug_Revenue,
    Sum(IF(month = 'Sep', revenue, null)) AS Sep_Revenue,
    Sum(IF(month = 'Oct', revenue, null)) AS Oct_Revenue,
    Sum(IF(month = 'Nov', revenue, null)) AS Nov_Revenue,
    Sum(IF(month = 'Dec', revenue, null)) AS Dec_Revenue
From
    Department
Group By
    id;