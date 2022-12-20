CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
     With hs As (select
                    *,
                    Dense_Rank() Over(Order By salary DESC) AS sal_rank
                 From
                    Employee
                )
      select
        salary
      From 
        hs
      where sal_rank = N
      Limit 1
  );
END