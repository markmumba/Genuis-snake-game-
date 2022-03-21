import psycopg2


#connecting the db
con = psycopg2.connect(
    host = "localhost",
    database= "snakegame",
    user = "postgres",
    password = "bobbyshmurda66"
)


#function to save the score 
def insert_scores(new_score):

    # insert a row into the table 
    sql = "INSERT INTO scores (score) VALUES (%s)"
    conn = None
    try:
        conn= con
        cursor = conn.cursor()

        cursor.execute(sql,(new_score,))

        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print (error)
    finally:
        if conn is not None:
            conn.close()

    return new_score        

#function to print the high score 
        
def get_highest_score():

    sql = "SELECT MAX(score) FROM scores"
    conn = None
    highest_score =None

    try : 
        conn = con
        cursor = conn.cursor()
        cursor.execute(sql)
        highest_score = cursor.fetchone()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print (error)

    finally:
        if conn is not None:
            conn.close()

    return highest_score

x= get_highest_score()



