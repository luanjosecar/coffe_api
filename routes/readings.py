from fastapi import APIRouter, Depends, HTTPException
from fastapi import File, UploadFile, Form
from typing import List
import json
import shortuuid

from .aux.dependencies import verify_token
from .aux.postgres_reader import *


router = APIRouter(
    prefix="/readings",
    tags=["readings"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_user_readings(user=Depends(verify_token), tags=["readings"]):
    return {"verifyed": "token_OK","user":user}

@router.post("/register")
async def register_reading(file: List[UploadFile], cnn_id:str = Form(), long:str = Form(), lat:str = Form() , user=Depends(verify_token)):
    pass

@router.get("/results/{reading_id}")
async def get_results(reading_id:str , user=Depends(verify_token)):
    pass