from sqlalchemy import Column, Integer, String
from database import Base


class Tutor(Base):
    __tablename__ = "tutores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(String)
    cidade = Column(String)
    sobre = Column(String)


class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    idade = Column(Integer)
    temperamento = Column(String)


class abrigo(Base):
    __tablename__ = "abrigos"

    id = Column(Integer, primary_key=True, index=True)
    localidade = Column(String)
