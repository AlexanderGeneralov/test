from sqladmin import ModelView
from models import User_model, Song_model


class UserAdmin(ModelView, model=User_model):
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
    category = "Пользователи"
    category_icon = "fa-solid fa-users"
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
    column_list = [
        Song_model.id,
        Song_model.title,
        Song_model.year,
        Song_model.description
    ]
