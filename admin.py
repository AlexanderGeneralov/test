from sqladmin import ModelView
from models import User_model, Song_model


class UserAdmin(ModelView, model=User_model):
    column_list = [
        User_model.id, 
        User_model.username, 
        User_model.firstname, 
        User_model.lastname,
        User_model.email,
        User_model.is_admin
    ]
    

class SongAdmin(ModelView, model=Song_model):
    column_list = [
        Song_model.id,
        Song_model.title,
        Song_model.year,
        Song_model.description
    ]