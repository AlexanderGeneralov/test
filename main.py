#ссылка для регистрации/использования тестового магазина
test_shop_link = "https://yookassa.ru/joinups?createTestShop=true"

from fastapi import FastAPI, Depends, HTTPException, Request, Response
from fastapi.responses import JSONResponse
import uvicorn
from schema import Song_schema, User_post_schema, User_get_schema, CreatePaymentRequest_chema
from models import Song_model, User_model
from db import get_db, engine
from sqlalchemy.orm import Session
from typing import List
from sqladmin import Admin
from admin import UserAdmin, SongAdmin, authentication_backend
from yookassa import Configuration, Payment
from yookassa.domain.notification import WebhookNotificationEventType, WebhookNotificationFactory
import uuid
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

admin = Admin(app, engine, authentication_backend=authentication_backend)
admin.add_view(UserAdmin)
admin.add_view(SongAdmin)


Configuration.account_id = os.getenv("SHOP_ACCOUNT_ID")
Configuration.secret_key = os.getenv("SHOP_SECRET_KEY")


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


@app.post("/create_payment/")
async def create_payment(req: CreatePaymentRequest_chema):
    try:
        payment = Payment.create({
            "amount": {
                "value": f"{req.amount:.2f}",
                "currency": req.currency
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://0.0.0.0:443/return_url/"
            },
            "capture": True,
            "description": req.description
        }, uuid.uuid4())
        
        # возвращаем клиенту URL для оплаты и id платежа
        return {
            "payment_id": payment.id,
            "status": payment.status,
            "confirmation_url": payment.confirmation.confirmation_url
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
@app.get("/return_url/")
async def return_after_payment():
    return {"message": "you were redirected to this page after payment"}


@app.post("/payments/webhook/")
async def yookassa_webhook(request: Request):

    try:
        # Получаем сырое тело запроса для проверки подписи
        body_bytes = await request.body()
        
        # Парсим JSON
        webhook_data = json.loads(body_bytes.decode('utf-8'))
        
        # Логируем получение вебхука
        print(f"Received webhook: {webhook_data.get('event')}")
        
        # Всегда возвращаем 200 OK ЮКассе
        return JSONResponse(
            content={"status": "received"},
            status_code=200
        )
        
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON")
    except Exception as e:
        # Логируем ошибку, но возвращаем 200 чтобы ЮКасса не повторяла запрос
        print(f"Webhook processing error: {e}")
        return JSONResponse(
            content={"status": "error", "message": str(e)},
            status_code=200  # Всегда 200 для ЮКассы!
        )


@app.get("/payment_info/{payment_id}/")
async def get_paymant_info(payment_id):
    payment_data = Payment.find_one(payment_id=payment_id)
    return {"payment status": payment_data.status}


if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        reload=True,
        host="0.0.0.0", 
        port=443,
        ssl_keyfile="cert/key.pem",
        ssl_certfile="cert/cert.pem"
    )