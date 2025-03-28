from pydantic import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str('7711829510:AAFYv-kDRleiVoRu1RvNsGv53XdY5-osk24')
    BOT_NAME: str('Бот англичанин')

    class Config:
        env_file = '../.env'


config = Settings()
