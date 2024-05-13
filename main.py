from psycopg2 import connect

from os import getenv
 
DB_USER = getenv('POSTGRES_USER')
DB_PASS = getenv('POSTGRES_PASSWORD')
DB_HOST = getenv('POSTGRES_HOST', 'localhost')
DB_PORT = getenv('POSTGRES_PORT', '5432')
DB_NAME = getenv('POSTGRES_NAME')

try:
    conn = connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )
    print("Database connected successfully")
except Exception as e:
    print(f"Database not connected successfully: {e}")

