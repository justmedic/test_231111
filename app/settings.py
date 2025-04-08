from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    secret_key: str
    database_url: str = "postgresql+asyncpg://postgres:123@localhost/examcrm"

    # class Config:
    #     env_file = ".env"


settings = Settings()
