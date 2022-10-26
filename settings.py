from pydantic import BaseSettings


class Settings(BaseSettings):
	TOKEN: str = "" # TELEGRAM TOKEN


settings = Settings()
