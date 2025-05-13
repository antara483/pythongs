import mysql.connector
from dotenv import load_dotenv
import os

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        load_dotenv()  # Load .env file

        __cnx = mysql.connector.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME")
        )
    return __cnx
