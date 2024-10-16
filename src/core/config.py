from typing import Optional, List
from pydantic import Field, PostgresDsn, field_validator
from pydantic_core.core_schema import FieldValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )

    POSTGRES_HOST: str = Field(default=None)
    POSTGRES_PORT: int = Field(default=None)
    POSTGRES_DB: str = Field(default=None)
    POSTGRES_USER: str = Field(default=None)
    POSTGRES_PASSWORD: str = Field(default=None)
    POSTGRES_DSN: Optional[PostgresDsn] = Field(default=None)
    CORS_ORIGINS: Optional[List[str]] = Field(default=["*"])

    @field_validator('POSTGRES_DSN')
    def validate_postgres_dsn(
        cls,
        field: Optional[PostgresDsn],
        fields: FieldValidationInfo,
    ):
        if field:
            return field
        return PostgresDsn(
            f'postgresql+asyncpg://{fields.data.get("POSTGRES_USER")}:'
            f'{fields.data.get("POSTGRES_PASSWORD")}@'
            f'{fields.data.get("POSTGRES_HOST")}:'
            f'{fields.data.get("POSTGRES_PORT")}/'
            f'{fields.data.get("POSTGRES_DB")}',
        )


config = Config()


