from fastapi import APIRouter, Depends, HTTPException
from .aux.dependencies import verify_token
from .objects.user import UserBody
from .aux.user_base import *

router = APIRouter(
    prefix="/users",
    tags=["users"],
    #dependencies=[Depends(verify_token)],
    responses={404: {"description": "Not found"}},
)


@router.get('/heath')
async def root():
    return {"message": "Server OK"}

@router.post('login')
async def user_login(body: UserBody):
    resp = verify_user(body.user, body.password)
    return resp

@router.post('create')
async def create_user(body:UserBody):
    resp = create_user(body.user, body.password)
    return resp

@router.put('/modify')
async def modify_user(body:UserBody):
    resp = update_passowrd(body.user, body.password, body.new_passowrd)
    return resp