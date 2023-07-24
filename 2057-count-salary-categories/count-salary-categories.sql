With CT as (SELECT 'Low Salary' AS category, COUNT(*) AS accounts_count, 1 as ordN
FROM Accounts
WHERE income < 20000

UNION ALL

SELECT 'Average Salary' AS category, COUNT(*) AS accounts_count, 2 as ordN
FROM Accounts
WHERE income >= 20000 AND income <= 50000

UNION ALL

SELECT 'High Salary' AS category, COUNT(*) AS accounts_count, 3 as ordN
FROM Accounts
WHERE income > 50000)

select category,accounts_count From CT 
Order By ordN

