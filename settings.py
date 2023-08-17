from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "mongodb://localhost:27017/instagram_clone"
    secret_key: str = "secret_key_here"  # Change this for production

settings = Settings()
