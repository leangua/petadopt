from fastapi import APIRouter, Depends
from database import SessionLocal
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
import models
import sys
sys.path.append("..")

router = APIRouter(
    prefix="/abrigo",
    tags=["abrigo"],
    responses={404: {"Description": "Not Found"}}
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Abrigo(BaseModel):
    localidade: str = Field(min_length=1)


@router.get("/")
def retornar_abrigos(db: Session = Depends(get_db)):
    return db.query(models.Abrigo).all()


@router.post("/")
def criar_abrigo(abrigo: Abrigo,
                 db: Session = Depends(get_db)):
    abrigo_model = models.Abrigo()
    abrigo_model.localidade = abrigo.localidade

    db.add(abrigo_model)
    db.commit()
    return successful_response(201)


def successful_response(status_code: int):
    return {
        'status': status_code,
        'transaction': 'Successful'
    }
