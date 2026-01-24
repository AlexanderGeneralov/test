from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "test api"

    db_name: str = "test"
    db_user_name: str = "aleksandr"
    db_password: str = "dacent0000"
    db_server: str = "localhost"

    shop_accaunt_id: str = "1256377"
    shop_secret_key: str = "test_e8bvA7e9i4sqNHTrrRxCap237sf4bKcMC_mkFb48e24"


settings = Settings()