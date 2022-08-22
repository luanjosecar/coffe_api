from fastapi import APIRouter, Depends, HTTPException
from fastapi import File, UploadFile, Form
from typing import List
import json
import shortuuid

from .aux.dependencies import verify_token
from .aux.readings import *

router = APIRouter(
    prefix="/readings",
    tags=["readings"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_user_readings(token=Depends(verify_token), tags=["readings"]):
    '''
    ** Retorna todas as leituras com base no usuário que está lendo o sistema
    '''
    user_id = token.get('user_id')
    reads = get_readings(user_id)


    return {"message": "Sucess", "data" : reads}

@router.post("/register")
async def register_reading(file: List[UploadFile], cnn_id:str = Form(), long:str = Form(), lat:str = Form() , token=Depends(verify_token)):
    pass

@router.get("/results/{reading_id}")
async def get_results(reading_id:str , token=Depends(verify_token)):
    imgs_result = return_imgs_results(reading_id)
    return {"Message": "Sucess" , "Reading" : reading_id, "Data":imgs_result}


@router.get("/images/{reading_id}")
async def get_images(reading_id:str , token=Depends(verify_token)):
    imgs = return_imgs(reading_id)
    return {"Message": "Sucess" , "Imgs" : imgs}