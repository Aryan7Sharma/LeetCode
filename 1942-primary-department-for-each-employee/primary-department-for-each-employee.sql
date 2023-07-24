Select 
    employee_id,department_id
From Employee
where
    primary_flag = 'Y'
Union
Select 
    employee_id,department_id
From Employee
Group By employee_id
having count(department_id) = 1

Order By employee_id
