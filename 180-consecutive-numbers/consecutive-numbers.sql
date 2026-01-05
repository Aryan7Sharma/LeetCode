Select distinct num as "ConsecutiveNums" From 
(SELECT
        num,
        LAG(num) OVER (ORDER BY id) AS prev_num,
        LEAD(num) OVER (ORDER BY id) AS next_num
FROM Logs) t
where prev_num=num
and next_num=num