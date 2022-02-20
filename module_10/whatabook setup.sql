DROP USER IF EXISTS 'whatabook_user'@'localhost';


# create whatabook_user on the whatabook database 
CREATE USER'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';


# asign all rights to  whatabook_user 
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';


#drop tables if they are present
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS store;


# create the store table 
CREATE TABLE store (
    store_id     INT             NOT NULL        AUTO_INCREMENT,
    location  VARCHAR(250)     NOT NULL,
    PRIMARY KEY(store_id));


#create the book table
CREATE TABLE book (
    book_id   INT             NOT NULL        AUTO_INCREMENT,
    book_name  VARCHAR(250)     NOT NULL,
    details   VARCHAR(1000)     NOT NULL,
    author     VARCHAR(250)           NOT NULL,
    PRIMARY KEY(book_id));


#create the user table
CREATE TABLE user (
    user_id   INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(100)     NOT NULL,
    last_name  VARCHAR(100)     NOT NULL,
    email     VARCHAR(100)           NOT NULL,
    PRIMARY KEY(user_id));


#create the user table with foreign keys
CREATE TABLE wishlist (
    wishlist_id   INT             NOT NULL        AUTO_INCREMENT,
    user_id  INT     NOT NULL,
    book_id   INT             NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id));


# insert users
INSERT INTO user(first_name, last_name, email)
    VALUES('John', 'Doe', 'Jdoe@gmail.com');

INSERT INTO user(first_name, last_name, email)
    VALUES('Frank', 'Sinatra', 'SinatraStar@aol.com');

INSERT INTO user(first_name, last_name, email)
    VALUES('Fred', 'Smith', 'Unicornsparkles@hotmail.com');


#  insert store record 
INSERT INTO store(location)
    VALUES('410 Ave N, Seattle WA. 98109');


#  insert book records 
INSERT INTO book(book_name, author, details)
    VALUES('Anna Karenina', 'Leo Tolstoy', 'doomed love affair');

INSERT INTO book(book_name, author, details)
    VALUES('Madame Bovary', 'Gustave Flaubert', 'The most shocking content!');

INSERT INTO book(book_name, author, details)
    VALUES('War and Peace', 'Leo Tolstoy', 'details of the events leading up to the invasion of Russia');

INSERT INTO book(book_name, author, details)
    VALUES('The Great Gatsby', 'F. Scott Fitzgerald', 'American society post World War I');

INSERT INTO book(book_name, author, details)
    VALUES('Middlemarch', 'George Eliot', 'Fictionalized account of historically accurate events between 1829 to 1832');

INSERT INTO book(book_name, author, details)
    VALUES('The Adventures of Huckleberry Finn', 'Mark Twain', 'Coming of age story featuring adventures of a young boy.');

INSERT INTO book(book_name, author, details)
    VALUES('Hamlet', 'William Shakespeare', 'Tragedy about the murder of a monarch, and the revenge that ensues.');

INSERT INTO book(book_name, author, details)
	VALUES('Moby Dick', 'Herman Melville', 'the story of Captain Ahab and his maniacal pursuit of a white whale.');

INSERT INTO book(book_name, author, details)
    VALUES('The Odyssey', 'Homer', 'An epic Greek poem');


# create wishlist records 
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Fred'), 
        (SELECT book_id FROM book WHERE book_name = 'Anna Karenina'));

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'John'), 
        (SELECT book_id FROM book WHERE book_name = 'The Odyssey'));

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Frank'), 
        (SELECT book_id FROM book WHERE book_name = 'The Adventures of Huckleberry Finn'));
