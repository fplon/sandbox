# import secrets # TODO - uncomment this for PROD
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # MODE: str = "dev"

    # API_V1_STR: str = "/api/v1"

    # # SECRET_KEY: str = secrets.token_urlsafe(32) # TODO - uncomment this for PROD
    # SECRET_KEY: str = "temp-secret-key"  # stable key for dev

    # db config
    MONGO_HOST: str = "localhost"
    MONGO_PORT: int = 27017
    MONGO_DB: str = "sample_db"
    MONGO_USER: str
    MONGO_PASSWORD: str
    MONGO_CLUSTER: str

    # ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day
    # SERVER_NAME: str = "localhost"
    # SERVER_HOST: AnyHttpUrl = AnyHttpUrl("http://localhost")
    # BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    # FRONTEND_URL: str = "http://localhost"

    # PROJECT_NAME: str = "Project"

    # FIRST_SUPERUSER: EmailStr = ""
    # FIRST_SUPERUSER_PASSWORD: str = ""

    # # SSO and secrets
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    # SSO_CALLBACK_HOSTNAME: Optional[str] = None
    # SSO_LOGIN_CALLBACK_URL: Optional[str] = None
    # DOMAIN: str

    # ZOHO_SMTP_SERVER: str
    # ZOHO_SMTP_PORT: int
    # ZOHO_SMTP_USER: str
    # ZOHO_SMTP_PASSWORD: str
    # ZOHO_INFO_USER: str

    # RECAPTCHA_SECRET_KEY: str

    # API_RATE_LIMIT: str = "10/minute"

    # OPENAI_API_KEY: str

    # STRIPE_WEBHOOK_SECRET: str
    # STRIPE_SECRET_KEY: str

    # BETTERSTACK_TOKEN: str

    # configure from .env file
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()  # type: ignore
