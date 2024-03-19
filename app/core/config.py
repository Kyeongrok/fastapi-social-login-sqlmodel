from typing import Any

from pydantic import PostgresDsn, field_validator
from pydantic_core.core_schema import FieldValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_ENV: str = ""
    SECRET_KEY: str = ""
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    DB_HOST: str = ""
    DB_USERNAME: str = ""
    DB_PASSWORD: str = ""
    DB_PORT: int = 5432
    DB_NAME: str = ""
    ASYNC_DATABASE_URI: PostgresDsn | str = ""

    @field_validator("ASYNC_DATABASE_URI", mode="after")
    def assemble_db_connection(cls, v: str | None, info: FieldValidationInfo) -> Any:
        if isinstance(v, str):
            if v == "":
                return PostgresDsn.build(
                    scheme="postgresql+psycopg2",
                    username=info.data["DB_USERNAME"],
                    password=info.data["DB_PASSWORD"],
                    host=info.data["DB_HOST"],
                    port=info.data["DB_PORT"],
                    path=info.data["DB_NAME"]
                )
        return v


    model_config = SettingsConfigDict(
        case_sensitive=True, env_file=".env"
    )


settings = Settings()
