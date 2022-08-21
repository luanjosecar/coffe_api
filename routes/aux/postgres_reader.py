import psycopg2
from psycopg2 import Error

def send_request(query:str):
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