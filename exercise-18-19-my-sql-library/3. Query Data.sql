--  students.student_email, students.student_id, loans.loan_isbn as ISBN, loans.loan_date, loans.loan_due from students left join loans on students.student_number=loans.loan_studentid;

#

-- all bookings for author Ryan Turner
-- students: email, first name
-- books: book title, author
-- we know: the loan table

-- select students.student_email, students.student_firstname, books.book_title, books.book_author from students, books

select loans.*, students.student_email, students.student_firstname, books.book_title, books.book_author
	from loans 
	inner join students
    on loans.loan_studentid = students.student_id
    inner join books
    on loans.loan_bookid = books.id
	where books.book_author like "%Ryan Turner%";


-- sending receipts/confirmation emails with booking details
-- students: email, name
-- books: book title, author, isbn
-- loans: date, due date

select loans.loan_date, loans.loan_due, students.student_email, students.student_firstname, students.student_lastname, books.book_title, books.book_author, books.book_isbn
	from loans
    inner join students
     on loans.loan_studentid = students.student_id
    inner join books
    on loans.loan_bookid = books.id;


-- all Python books taken out in April
-- students: nothing
-- books: title, author
-- loans: date, due date

-- add "returned" 

select * from loans;

select books.id, books.book_title, books.book_author, loans.loan_date, loans.loan_due
	from books
    join loans
    on loans.loan_bookid = books.id
    where books.book_title like "%Python%"
    and loans.loan_date between "2022-04-01" and "2022-04-10";
