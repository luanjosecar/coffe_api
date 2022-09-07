from pymongo import MongoClient, errors
import os
from dotenv import load_dotenv
load_dotenv()

DOMAIN = os.getenv('MONGO_DOMAIN')
PORT = os.getenv('MONGO_PORT')
MONGOUSER = os.getenv('MONGO_USER')
MONGPWD = os.getenv('MONGO_PSWD')

def conect_mong_base():
    try:
        client = MongoClient(
            host = [ str(DOMAIN) + ":" + str(PORT) ],
            serverSelectionTimeoutMS = 3000, # 3 second timeout
            username = MONGOUSER,
            password = MONGPWD,
        )
        return client
    except Exception as e: 
        print("Printing Error")
        print(e)
        return None

def create_mongo():
    mong = conect_mong_base()
    dblist = mong.list_database_names()
    if "usuarios" in dblist:
        print("MONGO - The database exists.")
    else:
        mong["usuarios"]
        print("MONGO - database created")