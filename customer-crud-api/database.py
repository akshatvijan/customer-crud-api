import os

from dotenv import load_dotenv
import psycopg

load_dotenv()


def get_connection():
    return psycopg.connect(
        host="localhost",
        dbname="customer_management",
        user="postgres",
        password=os.getenv("PASSWORD"),
        port=5432
    )