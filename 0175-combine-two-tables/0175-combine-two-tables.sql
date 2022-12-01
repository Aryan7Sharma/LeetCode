# Write your MySQL query statement below
Select
    firstName,
    lastName,
    city,
    state
From
    Person Left Join Address
    On Person.PersonID = Address.PersonID