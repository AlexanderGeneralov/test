from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import DATABASE_URL
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(DATABASE_URL)


Base = declarative_base()


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
