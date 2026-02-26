from sqlalchemy import Column, String, Integer, Boolean

from database.db import Base



class Song_model(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(Integer, index=True)
    description = Column(String, index=True)


class Artist_model(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class User_model(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    is_admin = Column(Boolean)
    hashed_password = Column(String)
    disabled = Column(Boolean, default=False)
