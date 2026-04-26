import mysql.connector
import os

def get_connection(db_name):
    return mysql.connector.connect ( 
        host = "localhost",
        user = "root",
    
password=os.getenv("DB_PASSWORD"),
    database=db_name,
    charset="utf8"
)

print("Connected successfully!")