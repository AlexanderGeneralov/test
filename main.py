from fastapi import FastAPI, Depends
import uvicorn
from schema import Song_schema
from models import Song_model
from db import get_db
from sqlalchemy.orm import Session

app = FastAPI()

@app.get('/songs/')
def get_songs(db: Session = Depends(get_db)):
    return db.query(Song_model).all()


@app.get('/songs/{song_id}')
def get_song(song_id: int, db: Session = Depends(get_db)):
    song = db.get(Song_model, song_id)
    return song


@app.post('/songs/', response_model=Song_schema)
def post_songs(data: Song_schema, db: Session = Depends(get_db)):
    song = Song_model(**data.model_dump())
    db.add(song)
    db.commit()
    db.refresh(song)
    return song


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
