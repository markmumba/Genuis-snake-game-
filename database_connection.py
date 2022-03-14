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
        
