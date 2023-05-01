from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


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
    sobre: str = Field(min_length=1, None)


@app.post("/tutor")
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


@app.get("/tutor")
def retornar_tutores(db: Session = Depends(get_db)):
    return db.query(models.Tutor).all()


@app.get("/tutor/{tutor_id}")
def retornar_tutor(tutor_id: int,
                   db: Session = Depends(get_db)):
    return db.query(models.Tutor).filter(models.Tutor.id == tutor_id).first()


@app.delete("/tutor/{tutor_id}")
def deletar_tutor(tutor_id: int,
                  db: Session = Depends(get_db)):
    db.query(models.Tutor)\
        .filter(models.Tutor.id == tutor_id)\
        .delete()

    db.commit()
    return successful_response(200)


@app.put("/tutor/{tutor_id}")
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
