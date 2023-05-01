from routers import tutor
from fastapi import FastAPI
from database import engine
import models
from routers import tutor, pet, abrigo

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(tutor.router)
app.include_router(pet.router)
app.include_router(abrigo.router)
