from fastapi import APIRouter, Depends, HTTPException
from fastapi import File, UploadFile, Form, Body
from typing import List
import json
import shortuuid

from pydantic import BaseModel
from .utils.dependencies import verify_token
from .utils.readings import *

router = APIRouter(
    prefix="/readings",
    tags=["readings"],
    responses={404: {"description": "Not found"}},
)

class Image_location(BaseModel):
    paths: List[dict] = None

class Location():
    x_max :str = None
    x_min :str =None
    y_max :str = None
    y_min : str = None

@router.get("/")
async def get_user_readings(token=Depends(verify_token), tags=["readings"]):
    '''
    ** Retorna todas as leituras com base no usuário que está lendo o sistema
    '''
    user_id = token.get('user_id')
    reads = get_readings(user_id)


    return {"message": "Sucess", "data" : reads}

@router.post("/register")
async def register_reading(file: List[UploadFile], imp_name:str = Form(), long:str = Form(), lat:str = Form() , 
                        token=Depends(verify_token)):

    read_id = shortuuid.uuid()
    user_id = token.get('user_id')
    

    for index, imgs in enumerate(file):
        contents = await imgs.read()
        img_path = upload_img(contents,read_id,index,imp_name)
        insert_imgs(read_id, img_path)
    insert_reading(read_id,user_id=user_id,cnn_id=imp_name)
    if long and lat:
        insert_reading_location(reading_id=read_id,longitude=long,latitude=lat)
    return {"Message": "Sucess", "Reading": read_id}


@router.post("register_paths/{reading_id}")
async def register_image_paths(paths :Image_location = Body(
    examples = {
        "normal":{
            "value":{"paths":[{"x_max":"0.23", "x_min":"0.12", "y_max":"0.53", "y_min":"0.11" }]}
            }
        }),token=Depends(verify_token)):
    pass

@router.get("/results/{reading_id}")
async def get_results(reading_id:str , token=Depends(verify_token)):
    imgs_result = return_imgs_results(reading_id)
    return {"Message": "Sucess" , "Reading" : reading_id, "Data":imgs_result}


@router.get("/images/{reading_id}")
async def get_images(reading_id:str , token=Depends(verify_token)):
    imgs = return_imgs(reading_id)
    return {"Message": "Sucess" , "Imgs" : imgs}