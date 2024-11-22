import mysql.connector

def connect_db():
    conn = mysql.connector.connect( host='localhost',
                                    user='root',
                                    password='your_password',
                                    database='your_database' )
    return conn

