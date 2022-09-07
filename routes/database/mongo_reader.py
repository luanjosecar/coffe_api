from pymongo import MongoClient, errors
import os
from dotenv import load_dotenv
load_dotenv()


DOMAIN = os.getenv('MONGO_DOMAIN')
PORT = os.getenv('MONGO_PORT')
MONGOUSER = os.getenv('MONGO_USER')
MONGPWD = os.getenv('MONGO_PSWD')


def conect_mong():
    try:
        client = MongoClient(
            host = [ str(DOMAIN) + ":" + str(PORT) ],
            serverSelectionTimeoutMS = 3000, # 3 second timeout
            username = MONGOUSER,
            password = MONGPWD,
        )
        return client['usuarios']
    except Exception as e: 
        print("Printing Error")
        print(e)
        return None

def insert_user(usuario:str, password:str):
    try:  
        db = conect_mong()
        conector = db['users']
        usuario = {"_id": usuario,"password": password}
        conector.insert_one(usuario)
        return {"mesage" : "user Created"}
    except Exception as e: 
        print(e)
        return {"mesage" : "Erro ao Criar Usuario"}

def find_user(username:str):
    db = conect_mong()
    conector = db['users']
    usuario = conector.find_one({"_id" : username})
    return usuario


def update_user(username:str, new_value:dict):
    db = conect_mong()
    base_value = {"_id":username}
    query = {"$set" : new_value}
    db.users.replace_one(base_value, new_value)