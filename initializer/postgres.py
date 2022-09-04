import psycopg2
from psycopg2 import Error


def create_databases():
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