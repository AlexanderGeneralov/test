from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from dependencies import get_db
from models.models import User_model
from schemas.schema import User_get_schema, User_post_schema


router = APIRouter(prefix="/users")

@router.get('/', response_model=List[User_get_schema])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User_model).all()
    return users


@router.get('/{user_id}', response_model=User_get_schema)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User_model, user_id)
    return user


@router.post('/', response_model = User_post_schema)
def post_user(data: User_post_schema, db: Session = Depends(get_db)):
    user = User_model(**data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
