#Jason Luttrell 11/30/24  CSD310-T301 Module 7.2

""" import statements """
import mysql.connector # to connect
#from mysql.connector import errors

import dotenv # to use .env file
from dotenv import dotenv_values


#using our .env file
secrets = dotenv_values("c:/Users/User/csd/csd-310/module-6/.env")


""" database config object """
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True #not in .env file
}

db = mysql.connector.connect(**config) # connect to the movies database 

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the movies database 
    
    # output the connection status 
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    #create Cursor Object
    cursor = db.cursor()

    #***********************************************************************
    # Build first Query (studios) and Intro Message
    stQ1Intro = '-- DISPLAYING Studio RECORDS --'
    stQry1 = 'SELECT studio_id, studio_name FROM studio'

    #Execute Cursor, Fetch and print
    cursor.execute(stQry1)
    studios = cursor.fetchall()
    print(stQ1Intro)
    #Loop through the query return and print the results
    for x in studios:
        print("Studio ID: {}\n Studio Name: {}\n".format(x[0],x[1]))

    #**********************************************************************
    # Build Second Query (genres) and Intro Message
    stQ1Intro = '-- DISPLAYING Genre RECORDS --'
    stQry1 = 'SELECT genre_id, genre_name FROM genre;'
    #Execute Cursor, Fetch and print
    cursor.execute(stQry1)
    studios = cursor.fetchall()
    print(stQ1Intro)
    #Loop through the query return and print the results
    for x in studios:
        print("Genre ID: {}\n Genre Name: {}\n".format(x[0],x[1]))

    #**********************************************************************
    # Build Third Query (short films) and Intro Message
    stQ1Intro = '-- DISPLAYING Short Film RECORDS --'
    stQry1 = 'SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;'
    #Execute Cursor, Fetch and print
    cursor.execute(stQry1)
    studios = cursor.fetchall()
    print(stQ1Intro)
    #Loop through the query return and print the results
    for x in studios:
        print("Film Name: {}\n Film Runtime: {}\n".format(x[0],x[1]))


   #**********************************************************************
    # Build Third Query (short films) and Intro Message
    stQ1Intro = '-- DISPLAYING Director RECORDS in Order--'
    stQry1 = 'SELECT film_name, film_director FROM film ORDER BY film_director'
    #Execute Cursor, Fetch and print
    cursor.execute(stQry1)
    studios = cursor.fetchall()
    print(stQ1Intro)
    #Loop through the query return and print the results
    for x in studios:
        print("Film Name: {}\n Director Name: {}\n".format(x[0],x[1]))


except mysql.connector.Error as err:
    """ on error code """
    print(err)


finally:
    """ close the connection to MySQL """

    db.close()
