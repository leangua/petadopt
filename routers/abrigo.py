from fastapi import APIRouter
import sys
sys.path.append("..")

router = APIRouter(
    prefix="/abrigo",
    tags=["abrigo"],
    responses={404: {"Description": "Not Found"}}
)
