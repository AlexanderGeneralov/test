from pydantic import BaseModel


class Song_schema(BaseModel):
    title: str
    year: int
    description: str


class User_post_schema(BaseModel):
    email: str
    username: str
    firstname: str
    lastname: str
    is_admin: bool


class User_get_schema(BaseModel):
    email: str
    username: str
    firstname: str
    lastname: str
    is_admin: bool


class CreatePaymentRequest_chema(BaseModel):
    amount: float
    currency: str = "RUB"
    description: str  
    