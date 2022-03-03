import sys
import mysql.connector
from mysql.connector import errorcode

#database configure
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#display the main menu to the user upon opening the application
def show_menu():
    print("\n Welcome to WhatABook Main Menu ")
    print("   1. See Our Books\n    2. Store Locations\n    3. Log into ‘My Account’\n    4. Exit Application")
try:
        choice = int(input("Please enter the number of the function you would like : "))
        return choice
except:
        print("\n  That is an invalid choice...")
        sys.exit(0)

user_input = show_menu()
    
while user_input != 4:
        if user_input == 1:
            show_books(cursor)

        if user_input == 2:
            show_location(cursor)

        if user_input == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

# User credentials request and check for validity 
def validate_user():

    try:
        user_id = int(input('\n      Enter a customer id <Example 1 for user_id 1>: '))

        if user_id < 0 or user_id > 3:
            print("\n  Invalid User Information...\n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n  Invalid User Information...\n")

        sys.exit(0)


# display a user’s Wishlist
def show_wishlist(_cursor, _user_id):
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))

    wishlist = _cursor.fetchall()

print(" Books currently in your wishlist : ")
for book in wishlist
    print(" book title: {}\n book author: {}\n book details: {}\n".format(book[0], book[1], book[2]))


#whatabook location
def show_locations(_cursor):
    cursor.execute("SELECT store_id, location from store;")

    location = _cursor.fetchall()

    print("Store location")
    print("location: {}\n " .format(location[0] location[1], location[2]))


# what does whatabook have in stock
def show_books(_cursor):
    cursor.execute("SELECT book_id, book_name, author, details from book;")

    books = _cursor.fetchall()

    print("\n book name: {}\n book title: {}\n book author: {}\n  book details: {}\n".format(book[0], book[1], book[2]))


# view the list of books not in the user's wishlist
def show_books_to_add(_cursor, _user_id):   
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    print("Books available for addition to your wishlist:")
    print("\n book name: {}\n book title: {}\n book author: {}\n  book details: {}\n".format(book[0], book[1], book[2]))


# add a book to the user's wishlist
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    cursor.execute("INSERT INTO wishlist(user_id, book_id)) VALUES({}, {})".format(_user_id, _book_id))

# connect to whatabook database 
try:

    db = mysql.connector.connect(**config) 

    cursor = db.cursor()

    print(" Hello Welcome to WhatABook!  Where we know all the best stories")

except mysql.connector.Error as err:   #handle issues and close the DB

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied user ID or password are invalid")

    else:
        print(" Unknown Error, Sorry Your Experiancing Difficulties")
finally:
    db.close()
