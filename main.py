#ссылка для регистрации/использования тестового магазина
test_shop_link = "https://yookassa.ru/joinups?createTestShop=true"

from fastapi import FastAPI
import uvicorn
from database.db import engine
from sqladmin import Admin
from internal.admin import UserAdmin, SongAdmin, TestAdmin, authentication_backend
from routers import users, songs, payments

app = FastAPI()

app.include_router(users.router)
app.include_router(songs.router)
app.include_router(payments.router)

admin = Admin(app, engine, authentication_backend=authentication_backend)
admin.add_view(UserAdmin)
admin.add_view(SongAdmin)
admin.add_view(TestAdmin)

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        reload=True,
        host="0.0.0.0", 
        port=443,
        ssl_keyfile="cert/key.pem",
        ssl_certfile="cert/cert.pem"
    )
