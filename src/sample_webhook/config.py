from pydantic import BaseSettings

# TODO: Determine if the BaseSettings base class is needed & where it's located


# TODO: Use the configuration to identify where the indexing logic is that needs to be run?
# TODO: The github repo is not needed (I don't believe)

class Settings: #(BaseSettings):
    github_webhook_secret: str
    github_repo: str = "hammer1209/sample-webhook"
    environment: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()