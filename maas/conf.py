import os

from pydantic import BaseSettings


class Settings(BaseSettings):

    PLUS_SERVICE_ADDRESS: str = ""
    MINUS_SERVICE_ADDRESS: str = ""
    DIVIDE_SERVICE_ADDRESS: str = ""
    MULTIPLY_SERVICE_ADDRESS: str = ""
    POWER_SERVICE_ADDRESS: str = ""

    class Config:
        env_prefix = os.getenv("ENV", "MAAS") + "_"


settings = Settings()
