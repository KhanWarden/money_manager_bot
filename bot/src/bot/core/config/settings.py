from pathlib import Path

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

from bot.core.config.database import DatabaseConfig
from bot.core.config.logging import LoggingConfig
from bot.core.config.app import AppConfig

CONFIG_DIR = Path(__file__).resolve().parent
ENVS_DIR = CONFIG_DIR / "envs"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_prefix="MONEY_MANAGER__",
        env_nested_delimiter="__",
        env_file=ENVS_DIR / ".env",
    )
    app: AppConfig
    db: DatabaseConfig
    logging: LoggingConfig = LoggingConfig()


settings = Settings()
