from pydantic import BaseSettings

class Settings(BaseSettings):
    github_webhook_secret: str
    github_repo: str = "hammer1209/sample-webhook"
    environment: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()