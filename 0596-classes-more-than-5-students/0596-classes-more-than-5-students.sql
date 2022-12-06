# Write your MySQL query statement below
Select
    class
From
    (
        Select
            class,
            count(Distinct student) As total_stu
        From
            Courses
        Group By class
    ) t2
Where
    total_stu>=5;
