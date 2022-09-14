from fastapi import APIRouter, Depends, HTTPException
from .utils.dependencies import verify_token
from .utils.imps import *
from .utils.imps import *

router = APIRouter(
    prefix="/implementations",
    tags=["implementations"],
    dependencies = [Depends(verify_token)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_implementations(tags=["imps"]):
    imps = get_implementations()
    return {"Message" : "Sucess" , "Data" : imps}

@router.post("/include")
async def include_implementation(user=Depends(verify_token) ):
    pass
