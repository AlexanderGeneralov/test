from fastapi import FastAPI, Depends
import uvicorn
from schema import Song_schema, User_post_schema, User_get_schema
from models import Song_model, User_model
from db import get_db, engine
from sqlalchemy.orm import Session
from typing import List
from sqladmin import Admin
from admin import UserAdmin, SongAdmin


app = FastAPI()

admin = Admin(app, engine)
admin.add_view(UserAdmin)
admin.add_view(SongAdmin)


@app.get('/songs/')
def get_songs(db: Session = Depends(get_db)):
    return db.query(Song_model).all()


@app.get('/songs/{song_id}')
def get_song(song_id: int, db: Session = Depends(get_db)):
    song = db.get(Song_model, song_id)
    return song


@app.post('/songs/', response_model = Song_schema)
def post_songs(data: Song_schema, db: Session = Depends(get_db)):
    song = Song_model(**data.model_dump())
    db.add(song)
    db.commit()
    db.refresh(song)
    return song


@app.get('/users/', response_model=List[User_get_schema])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User_model).all()
    return users


@app.post('/post_user/', response_model = User_post_schema)
def post_user(data: User_post_schema, db: Session = Depends(get_db)):
    user = User_model(**data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
