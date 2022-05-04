import psycopg2
from psycopg2 import Error
import os

def create_connection():
    conn = None
    
    try:
        conn = psycopg2.connect(
                host=os.getenv("POSTGRES_HOST"),
                database=os.getenv("POSTGRES_DB"),
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"))



    except Error as e:
        print('Error connection' + str(e))
    return conn
        
