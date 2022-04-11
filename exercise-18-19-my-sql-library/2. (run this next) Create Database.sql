create database if not exists getintotech_library;

use getintotech_library;

show tables;

create table students(
student_id int primary key,
student_email varchar(40) not null,
student_firstname varchar(20) not null,
student_lastname varchar(20) not null);

create table books(
id int primary key auto_increment,
book_title varchar(50) not null,
book_author varchar(40) not null,
book_isbn varchar(16) not null);

create table loans(
id int primary key auto_increment,
loan_bookid integer,
loan_studentid integer,
foreign key (loan_bookid) references books(id),
foreign key (loan_studentid) references students(student_id),
loan_date datetime not null,
loan_due datetime not null);

insert into students values 
("201234", "ben.smith@uni.com", "Ben", "Smith"),
("198458", "steve.black@uni.com", "Steve", "Black"),
("222340", "laura.stuart@uni.com", "Laura", "Stuart"),
("229560", "betty.law@uni.com", "Betty", "Law"),
("214239", "robert.wayne@uni.com", "Robert", "Wayne");

select * from students;

insert into books (book_title, book_author, book_isbn) values
("Introduction to Coding", "John Smith", "162584675436"),
("Introduction to Python", "John Smith", "438443843864"),
("Macroeconomics", "Martha Smith", "438435684384"),
("Introduction to SQL", "John Smith", "438445754365"),
("Software Engineering for Dummies", "John Smith", "354366848436");

select * from books;

insert into loans (loan_bookid, loan_studentid, loan_date, loan_due) values
("1", "201234", "2022/04/02 10:00:00", "2022/05/05 00:00:00"),
("2", "198458", "2022/03/03 10:30:00", "2022/05/06 00:00:00"),
("3", "222340", "2022/01/04 10:11:00", "2022/05/07 00:00:00"),
("4", "229560", "2022/04/01 11:00:00", "2022/03/08 00:00:00"),
("5", "214239", "2022/03/28 01:00:00", "2022/05/09 00:00:00");

select * from loans;


