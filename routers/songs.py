from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from models.models import Song_model
from schemas.schema import Song_schema


router = APIRouter(prefix="/songs")


@router.get('/')
def get_songs(db: Session = Depends(get_db)):
    return db.query(Song_model).all()


@router.get('/{song_id}')
def get_song(song_id: int, db: Session = Depends(get_db)):
    song = db.get(Song_model, song_id)
    return song


@router.post('/', response_model = Song_schema)
def post_songs(data: Song_schema, db: Session = Depends(get_db)):
    song = Song_model(**data.model_dump())
    db.add(song)
    db.commit()
    db.refresh(song)
    return song
