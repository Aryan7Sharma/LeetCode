# Write your MySQL query statement below
select
    Distinct l1.num As ConsecutiveNums
From
    Logs l1,
    Logs l2,
    Logs l3
Where l1.id = l2.id-1 And
      l2.id = l3.id-1 And
      l1.num = l2.num And
      l2.num = l3.num