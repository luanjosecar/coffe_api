import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
import os
load_dotenv()

PSQL_USER = os.getenv('PSQL_USER') 
PSQL_PSWD = os.getenv('PSQL_PSWD')
PSQL_PORT = os.getenv('PSQL_PORT')
PSQL_DATABASE = os.getenv('PSQL_DATABASE')
PSQL_HOST = os.getenv('PSQL_HOST')


def create_databases():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user=PSQL_USER,
                                    password=PSQL_PSWD,
                                    host=PSQL_HOST,
                                    port=PSQL_PORT,
                                    database=PSQL_DATABASE)

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Executing a SQL query
        cursor.execute(open("initializer/tables.sql", "r").read())
        connection.commit()


    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL :", error)
    finally:
        if (connection):
            print("POSTGRES - Tables Created")
            cursor.close()
            connection.close()
            print("POSTGRES - Connection closed")