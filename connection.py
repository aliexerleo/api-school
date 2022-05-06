import psycopg2
from psycopg2 import Error
from decouple import config

def create_connection():
    conn = None
    
    try:
        conn = psycopg2.connect(
                host=config('POSTGRES_HOST'),
                database=config('POSTGRES_DB'),
                user=config('POSTGRES_USER'),
                password=config('POSTGRES_PASSWORD'))



    except Error as e:
        print('Error connection' + str(e))
    return conn
        
