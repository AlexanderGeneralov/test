import uuid

from sqlalchemy import Column, String, Integer, Boolean, UUID
from sqlalchemy.orm import Mapped, mapped_column
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
    description = Column(String)


class User_model(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    email = Column(String)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    is_admin = Column(Boolean)
    hashed_password = Column(String)
    disabled = Column(Boolean, default=False)

class Test_model(Base):
    __tablename__ = "tests"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
