""" 
    Title: pysports_queries.py
    Author: Professor Krasso
    Date: 15 July 2020
    Description: Test program for executing queries against the pysports database. 
"""

""" import statements """
import mysql.connector
from mysql.connector import errorcode


""" database config object """
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}


try:

    """ try/catch block for handling potential MySQL database errors """ 


    db = mysql.connector.connect(**config) # connect to the pysports database 


    cursor = db.cursor()
  
finally:
    """ close the connection to MySQL """
    
    db.close()
