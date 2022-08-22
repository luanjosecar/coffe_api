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
async def register_reading(file: List[UploadFile], imp_name:str = Form(), long:str = Form(), lat:str = Form() , token=Depends(verify_token)):

    read_id = shortuuid.uuid()
    user_id = token.get('user_id')
    insert_reading(read_id,user_id=user_id,cnn_id=imp_name)
    if not long:
        insert_reading_location(reading_id=read_id,longitude=long,latitude=lat)
    for index, imgs in enumerate(file):
        img_path = upload_img(imgs,read_id,index,imp_name)
        insert_imgs(read_id, img_path)
    return {"Message": "Sucess"}


@router.get("/results/{reading_id}")
async def get_results(reading_id:str , token=Depends(verify_token)):
    imgs_result = return_imgs_results(reading_id)
    return {"Message": "Sucess" , "Reading" : reading_id, "Data":imgs_result}


@router.get("/images/{reading_id}")
async def get_images(reading_id:str , token=Depends(verify_token)):
    imgs = return_imgs(reading_id)
    return {"Message": "Sucess" , "Imgs" : imgs}