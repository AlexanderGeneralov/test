import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SHOP_ACCOUNT_ID = os.getenv("SHOP_ACCOUNT_ID")
SHOP_SECRET_KEY = os.getenv("SHOP_SECRET_KEY")