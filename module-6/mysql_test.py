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

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errors.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errors.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)


finally:
    """ close the connection to MySQL """

    db.close()