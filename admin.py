from sqladmin import ModelView
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from models import User_model, Song_model
from db import SessionLocal
import time


class AdminAuth(AuthenticationBackend):

    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]
        
        # Validate credentials here
        session = SessionLocal()
        user = session.query(User_model).filter(User_model.username == username).first()
        if user and password == user.password:
            if user.is_admin:
                request.session.update({
                    "token": "secret",
                    "expires": time.time() + 600
                })
                return True
        else:
            False

    async def logout(self, request: Request):
        request.session.clear()
    
    async def authenticate(self, request: Request):
        token = request.session.get("token")
        expires = request.session.get("expires")
        if not token:
            return False
        if time.time() > expires:
            request.session.clear()
            return False
        
        # Validate token here
        return True


authentication_backend = AdminAuth(secret_key='...')


class UserAdmin(ModelView, model=User_model):
    name = "Пользователь"
    name_plural = "Пользователи"
    category = "Пользователи"
    category_icon = "fa-solid fa-user"
    column_list = [
        User_model.id, 
        User_model.username, 
        User_model.firstname, 
        User_model.lastname,
        User_model.email,
        User_model.is_admin
        ]
    column_details_exclude_list = [
        User_model.password
        ]
    column_sortable_list = [
        User_model.id, 
        User_model.username, 
        User_model.firstname, 
        User_model.lastname,
        User_model.email,
        User_model.is_admin
        ]
    column_searchable_list = [
        User_model.id, 
        User_model.username, 
        User_model.firstname, 
        User_model.lastname,
        User_model.email,
        User_model.is_admin
        ]
    can_create = False
    can_edit = False
    can_delete = False
    
    
class SongAdmin(ModelView, model=Song_model):
    name = "Песня"
    name_plural = "Песни"
    category = "Песни"
    category_icon = "fa-solid fa-music"
    column_list = [
        Song_model.id,
        Song_model.title,
        Song_model.year,
        Song_model.description
    ]
