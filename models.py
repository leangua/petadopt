from sqlalchemy import Column, Integer, String
from database import Base


class Tutor(Base):
    __tablename__ = "tutores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(String)
    cidade = Column(String)
    sobre = Column(String)
