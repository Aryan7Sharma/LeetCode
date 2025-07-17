-- Write your PostgreSQL query statement below
Select book_id,title,author,genre,publication_year,current_borrowers From 
(Select l.book_id,title,author,genre,publication_year,
count(b.book_id) as  current_borrowers, Max(borrow_date) as latest_borrow_date
From borrowing_records b right join library_books l
on l.book_id=b.book_id AND b.return_date IS NULL
GROUP BY l.book_id, l.title, l.author, l.genre, l.publication_year, l.total_copies
having count(b.book_id)=l.total_copies) as sub
ORDER BY 
    sub.current_borrowers DESC,
    sub.title ASC;