Select l.book_id,title,author,genre,publication_year,
count(b.book_id) as  current_borrowers
From borrowing_records b right join library_books l
on l.book_id=b.book_id AND b.return_date IS NULL
GROUP BY l.book_id, l.title, l.author, l.genre, l.publication_year, l.total_copies
having count(b.book_id)=l.total_copies
ORDER BY 
    current_borrowers DESC,
    title ASC;