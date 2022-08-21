from fastapi import APIRouter, Depends, HTTPException
from .aux.dependencies import verify_token

router = APIRouter(
    prefix="/implementations",
    tags=["implementations"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_implementations(user=Depends(verify_token),tags=["imps"]):
    pass

@router.get("/{leaf}")
async def read_implementations(leaf: str , user=Depends(verify_token)):
    pass

@router.post("/include")
async def include_implementation(user=Depends(verify_token)):
    pass

