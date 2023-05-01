import models
from pydantic import BaseModel, Field
from database import SessionLocal, Session
from fastapi import APIRouter, Depends
import sys
sys.path.append("..")


router = APIRouter(
    prefix="/tutores",
    tags=["tutores"],
    response={404: {"Description": "Not Found"}}
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Tutor(BaseModel):
    nome: str = Field(min_length=1)
    telefone: str = Field(min_length=1)
    cidade: str = Field(min_length=1)
    sobre: str = Field(min_length=1)


@router.get("/")
def retornar_tutores(db: Session = Depends(get_db)):
    return db.query(models.Tutor).all()


@router.get("/tutores/{tutor_id}")
def retornar_tutor(tutor_id: int,
                   db: Session = Depends(get_db)):
    return db.query(models.Tutor).filter(models.Tutor.id == tutor_id).first()


@router.post("/")
def criar_tutor(tutor: Tutor,
                db: Session = Depends(get_db)):

    tutor_model = models.Tutor()
    tutor_model.nome = tutor.nome
    tutor_model.telefone = tutor.telefone
    tutor_model.cidade = tutor.cidade
    tutor_model.sobre = tutor.sobre

    db.add(tutor_model)
    db.commit()
    return successful_response(201)


@router.delete("/{tutor_id}")
def deletar_tutor(tutor_id: int,
                  db: Session = Depends(get_db)):
    db.query(models.Tutor)\
        .filter(models.Tutor.id == tutor_id)\
        .delete()

    db.commit()
    return successful_response(200)


@router.put("/{tutor_id}")
def atualizar_tutor(tutor_id: int,
                    tutor: Tutor,
                    db: Session = Depends(get_db)):
    tutor_model = db.query(models.Tutor).filter(
        models.Tutor.id == tutor_id).first()

    tutor_model.nome = tutor.nome
    tutor_model.telefone = tutor.telefone
    tutor_model.cidade = tutor.cidade
    tutor_model.sobre = tutor.sobre

    db.add(tutor_model)
    db.commit()

    return successful_response(200)


def successful_response(status_code: int):
    return {
        'status': status_code,
        'transaction': 'Successful'
    }
