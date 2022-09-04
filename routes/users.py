from fastapi import APIRouter, Depends, HTTPException, Form
from .utils.dependencies import verify_token
from .utils.user_base import *

router = APIRouter(
    prefix="/users",
    tags=["users"],
    #dependencies=[Depends(verify_token)],
    responses={404: {"description": "Not found"}},
)


@router.get('/heath')
async def root():
    return {"message": "Server OK"}

@router.post('/login')
async def user_login(username:str = Form(), password:str = Form()):
    resp = verify_user(username, password)
    return resp

@router.post('/create')
async def create_user_base(username:str = Form(), password:str = Form()):
    resp = create_user(username, password)
    return resp

@router.put('/modify')
async def modify_user(username:str = Form(), password:str = Form(), new_passowrd:str = Form()):
    resp = update_passowrd(username, password, new_passowrd)
    return resp