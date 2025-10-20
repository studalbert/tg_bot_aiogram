from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
    )

    bot_token: str
    admin_ids: frozenset[int] = frozenset({42,5446529831})
    # BOT_TOKEN = os.getenv("BOT_TOKEN")

settings = Settings()
