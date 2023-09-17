from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    token_bot: SecretStr


    class Config:
        env_file = './data/.env'
        env_file_encoding = 'utf-8'


config = Settings()