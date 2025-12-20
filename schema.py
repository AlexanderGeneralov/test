from pydantic import BaseModel

class Song_schema(BaseModel):
    title: str
    year: int
    description: str

