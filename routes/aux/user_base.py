import jwt
from ..database.mongo_reader import * 

def verify_user(username:str, password:str):
    user = find_user(username)
    if(user):
        if(user['password'] == password):
            encoded_jwt = jwt.encode({"user_id": username}, "secret", algorithm="HS256")
            return {"Message": "User Found", "Token": "Bearer "+str(encoded_jwt)}
        else:
            return {"Message": "Wrong Password"}
    else:
        return {"Message": "User not Found"}

def create_user(username:str, passowrd:str):
    resp = insert_user(usuario=username,password=passowrd)
    return resp

def update_passowrd(username:str,password:str, new_passowrd:str):
    db = Mongo_User()
    user = find_user(username)
    if(new_passowrd==""):
        return {"Message": "Invalid Passowrd"}
    if(user and user['password'] == password):
        aux = {"password": new_passowrd}
        update_user(username,aux)
        return {"Message": "Password Changed"}
    return {"Message": "None"}