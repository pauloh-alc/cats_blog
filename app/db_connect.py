import pymysql
import os 
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


load_dotenv()

def connect():
    connection = pymysql.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_DATABASE'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        cursorclass=pymysql.cursors.DictCursor
    )

    return connection

