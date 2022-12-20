CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
     Select 
        Distinct salary
     From Employee e1
     Where n-1 = (select count(distinct salary) from Employee e2 where e2.salary>e1.salary)
  );
END