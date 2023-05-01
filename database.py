from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#SQLALCHEMY_DATABASE_URL = "sqlite:///./petadopt.db"

engine = create_engine('postgresql://leangua:12345@localhost/petadopt')

"""with engine.connect() as conn:
    query = text('SELECT 1')
    result = conn.execute(query)
    print(result.fetchone())"""

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
