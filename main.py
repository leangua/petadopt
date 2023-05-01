from routers import tutor
from fastapi import FastAPI
from database import engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tutor.router)
