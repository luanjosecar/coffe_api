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

def send_request(query:str):
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
        cursor.execute(query)
        connection.commit()
        # Fetch result
        #record = cursor.fetchone()
        #print("DB RESPONSE - ", record, "\n")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL :", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def get_request(query):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="postgres",
                                    password="example",
                                    host="0.0.0.0",
                                    port="5432",
                                    database="postgres")

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Executing a SQL query
        cursor.execute(query)
        connection.commit()
        # Fetch result
        record = cursor.fetchall()
        #print("DB RESPONSE - ", record, "\n")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL :", error)
        record = []

    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
        return record