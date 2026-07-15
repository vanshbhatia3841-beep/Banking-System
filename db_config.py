import mysql.connector
import os
from dotenv import load_dotenv

# Load variables once here
load_dotenv()

def get_db_connection():
    db_user = os.getenv('DB_USER')
    db_pass = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')
    db_host = os.getenv('DB_HOST')

    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_pass,
        database=db_name,
        auth_plugin='mysql_native_password'
    )