#Jason Luttrell 11/30/24  CSD310-T301 Module 7.2

def main():
    #import statements
    import mysql.connector # to connect
    #from mysql.connector import errors

    import dotenv # to use .env file
    from dotenv import dotenv_values


    #using our .env file
    secrets = dotenv_values("c:/Users/User/csd/csd-310/module-8/.env")


    #database config dictionary
    config = {
        "user": secrets["USER"],
        "password": secrets["PASSWORD"],
        "host": secrets["HOST"],
        "database": secrets["DATABASE"],
        "raise_on_warnings": True #not in .env file
    }

    db = mysql.connector.connect(**config) # connect to the movies database 

    try:  #try/catch block for handling potential MySQL database errors

        db = mysql.connector.connect(**config) # connect to the movies database 
        
        # output the connection status 
        print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

        #create Cursor Object
        cursor = db.cursor()

        # Build first title, which shows status prior to an changes
        stTitle1 = 'DISPLAYING FILMS'

        #Display the films using the show_films function
        show_films(cursor,stTitle1)

        #**********************************************************************
        # Build first Query (insert new film) and Title
        stTitle = 'DISPLAYING FILMS AFTER INSERT'
        stQry = 'INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, ' +\
                 'studio_id, genre_id) ' +\
                 'VALUES(\'Dolittle\', \'2020\', 100, \'Stephen Gaghan\', 3, 2)'
        
        #Execute Cursor
        cursor.execute(stQry)

        #Display the films using the show_films function
        show_films(cursor,stTitle)

        #**********************************************************************
        # Build Second Query (Update Alien Genre) and Title
        stTitle = 'DISPLAYING FILMS AFTER UPDATE'
        stQry = 'UPDATE film ' +\
                 'SET genre_id = 1 ' +\
                 'WHERE film_name = \'Alien\''
        
        #Execute Cursor
        cursor.execute(stQry)

        #Display the films using the show_films function
        show_films(cursor,stTitle)

        #**********************************************************************
        # Build Third Query (Delete Gladiator) and Title
        stTitle = 'DISPLAYING FILMS AFTER DELETE'
        stQry = 'DELETE FROM film ' +\
                 'WHERE film_name = \'Gladiator\''
        
        #Execute Cursor
        cursor.execute(stQry)

        #Display the films using the show_films function
        show_films(cursor,stTitle)


    except mysql.connector.Error as err:
        """ on error code """
        print(err)


    finally:  
        db.close() #close the connection to MySQL

def show_films (cursor, title):
    #method to execute an inner join on all tables,  iterate over the dataset,
    #and output the results to the terminal window.

    #Build inner join query
    stQry = 'SELECT film_name as Name, film_director as Director, ' +\
                    'genre_name as Genre, studio_name as \'Studio Name\' ' +\
            'FROM film as a ' +\
            'INNER JOIN genre as b ON a.genre_id = b.genre_id ' +\
            'INNER JOIN studio as c ON a.studio_id = c.studio_id'
    cursor.execute(stQry) #Execute Qry

    #Get results from the cursor object
    films = cursor.fetchall()

    print(f"\n  --  {title}  --") #print the Header

    #iterate over the film dataset and display the results
    for film in films:
        print(f'\nFilm Name: {film[0]}\nDirector: {film[1]}\nGenre Name: {film[2]}\nStudio Name: {film[3]}')
    

if __name__ == '__main__':
    main()
