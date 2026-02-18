from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from yookassa import Configuration, Payment
from yookassa.domain.notification import WebhookNotificationEventType, WebhookNotificationFactory
from core.config import SHOP_ACCOUNT_ID, SHOP_SECRET_KEY
from schemas.schema import CreatePaymentRequest_chema

import uuid
import json


router = APIRouter(prefix="/payments")


Configuration.account_id = SHOP_ACCOUNT_ID
Configuration.secret_key = SHOP_SECRET_KEY


@router.post("/")
async def create_payment(req: CreatePaymentRequest_chema):
    try:
        payment = Payment.create({
            "amount": {
                "value": f"{req.amount:.2f}",
                "currency": req.currency
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://0.0.0.0:443/payments/return_url/"
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
        
@router.get("/return_url/")
async def return_after_payment():
    return {"message": "you were redirected to this page after payment"}


@router.post("/webhook/")
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


@router.get("/payment_info/{payment_id}/")
async def get_paymant_info(payment_id):
    payment_data = Payment.find_one(payment_id=payment_id)
    return {"payment status": payment_data.status}
