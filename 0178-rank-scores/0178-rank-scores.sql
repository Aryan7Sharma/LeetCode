# Write your MySQL query statement below
Select
    score,
    Dense_rank() Over(Order By score desc) AS 'rank'
From
    Scores;
