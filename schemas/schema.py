from pydantic import BaseModel


class Song_schema(BaseModel):
    title: str
    year: int
    description: str


class User_post_schema(BaseModel):
    email: str
    username: str
    firstname: str
    hashed_password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool


class User_get_schema(BaseModel):
    email: str
    username: str
    firstname: str
    is_active: bool
    is_superuser: bool
    is_verified: bool


class CreatePaymentRequest_chema(BaseModel):
    amount: float
    currency: str = "RUB"
    description: str
