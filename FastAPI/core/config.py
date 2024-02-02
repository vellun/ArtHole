from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_name = os.environ.get("DB_NAME")
db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
# SECRET_AUTH = os.environ.get("SECRET_AUTH")


class Setting(BaseSettings):
    db_url: str = f"postgresql+asyncpg://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    api_v1_prefix: str = "/api/v1"

settings = Setting()