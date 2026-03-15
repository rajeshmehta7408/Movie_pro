import mysql.connector

def get_db():

    connection = mysql.connector.connect(
        host="localhost",
        user="Harshit",
        password="Harshit#8955",
        database="movie_prediction"
    )

    return connection