from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configurações Gerais Usadas na Aplicação.
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'sqlite+aiosqlite:///./teste.db/'
    # DB_URL: str = 'postgresql+asyncpg://postgres:1234@localhost:5432/srs'
    DBBaseModel: DeclarativeMeta = declarative_base()

    class config:
        case_sensitive = True




settings = Settings()
