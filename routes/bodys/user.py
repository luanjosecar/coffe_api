from pydantic import BaseModel
'''
User model
'''
class UserBody(BaseModel):
    user: str
    password: str
    new_passowrd :str = ""