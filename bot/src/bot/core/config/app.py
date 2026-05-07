from pydantic import BaseModel


class AppConfig(BaseModel):
    token: str
