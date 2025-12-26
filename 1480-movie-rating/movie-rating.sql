(Select 
    name as results 
From
    MovieRating mr left join Users u
    On mr.user_id = u.user_id
    Group By mr.user_id
    Order By count(u.user_id) desc, name Limit 1)
Union All
(
    Select 
    title as results 
From
    MovieRating mr left join Movies m
    On mr.movie_id = m.movie_id
    where created_at>='2020-02-01' and created_at<'2020-03-01'
    Group By mr.movie_id
    Order By Avg(rating) desc, title Limit 1
)