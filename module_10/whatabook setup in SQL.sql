# create whatabook_user on the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

# asign all rights to  whatabook_user 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

#drop tables if they are present
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;



# create the store table 
CREATE TABLE store (
    store_id     INT             NOT NULL        AUTO_INCREMENT,
    location  VARCHAR(250)     NOT NULL,
    PRIMARY KEY(store_id)
); 

#create the book table and set the foreign key
CREATE TABLE book (
    book_id   INT             NOT NULL        AUTO_INCREMENT,
    book_name  VARCHAR(250)     NOT NULL,
    details   VARCHAR(1000)     NOT NULL,
    author     VARCHAR(250)           NOT NULL,
    PRIMARY KEY(book_id),
);

CREATE TABLE user (
    user_id   INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(100)     NOT NULL,
    last_name  VARCHAR(100)     NOT NULL,
    email     VARCHAR(100)           NOT NULL,
    PRIMARY KEY(user_id),
);

CREATE TABLE wishlist (
    wishlist_id   INT             NOT NULL        AUTO_INCREMENT,
    user_id  INT     NOT NULL,
    book_id   INT             NOT NULL,
    author     VARCHAR(250)           NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);
