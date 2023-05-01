from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Tutor(Base):
    __tablename__ = "tutores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(String)
    cidade = Column(String)
    sobre = Column(String)


class Pets(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    idade = Column(Integer)
    temperamento = Column(String)
    abrigo_id = Column(Integer, ForeignKey("abrigos.id"))

    abrigo = relationship("Abrigos", back_populates="pet")


class Abrigos(Base):
    __tablename__ = "abrigos"

    id = Column(Integer, primary_key=True, index=True)
    localidade = Column(String)

    pet = relationship("Pets", back_populates="abrigo")
