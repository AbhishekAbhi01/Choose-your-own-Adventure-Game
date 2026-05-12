from typing import List
from pydantic import AliasChoices, Field, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = Field(validation_alias="DATABASE")
    API_PREFIX: str = "/api"
    DEBUG: bool = False

    ALLOW_ORIGINS: str = Field(
        default="",
        validation_alias=AliasChoices("ALLOW_ORIGINS", "AllOW_ORIGINS"),
    )
    OPENAI_API_KEY: str

    @field_validator("DEBUG", mode="before")
    @classmethod
    def parse_debug(cls, v: str) -> bool:
        if isinstance(v, str):
            return v.lower() in {"1", "true", "yes", "on", "debug", "development"}
        return v

    @property
    def allow_origins(self) -> List[str]:
        return [origin.strip() for origin in self.ALLOW_ORIGINS.split(",") if origin.strip()]
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        extra = "ignore"

settings = Settings()
