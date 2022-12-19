# Write your MySQL query statement below
Select 
    Case
        When mod(id, 2)!=0 And Counts!=id Then id+1
        When mod(id, 2)!=0 And Counts = id Then id
        Else id-1
    End As id,
    student
From 
    seat,
    (
        select 
            count(*) As Counts
        From
            seat
    ) As total_seat
Order By id