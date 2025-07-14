-- Write your PostgreSQL query statement below
update Salary 
set sex = Case
    When sex='m' then 'f'
    When sex='f' then 'm'
    Else sex
End;