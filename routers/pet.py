import models
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from database import SessionLocal
from sqlalchemy.orm import Session
import sys
sys.path.append("..")

router = APIRouter(
    prefix="/pet",
    tags=["Pet"],
    responses={404: {"Description": "Not Found"}}
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Pet(BaseModel):
    nome: str
    idade: int
    temperamento: str


@router.get("/")
def retornar_pets(db: Session = Depends(get_db)):
    return db.query(models.Pet).all()


@router.get("/{pet_id}")
def retornar_pet(pet_id: int,
                 db: Session = Depends(get_db)):
    return db.query(models.Pet).filter(models.Pet.id == pet_id).first()


@router.post("/")
def criar_pet(pet: Pet,
              db: Session = Depends(get_db)):
    pet_model = models.Pet()
    pet_model.nome = pet.nome
    pet_model.idade = pet.idade
    pet_model.temperamento = pet.temperamento
