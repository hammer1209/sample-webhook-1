""" Configuration settings for the sample webhook application. """

import dataclasses
from pydantic_settings import BaseSettings

# TODO: Use the configuration to identify where the indexing logic is that needs to be run?
# TODO: We shouldn't need to know the github repo that initiated the push

class Settings(BaseSettings):
    """
    Configuration settings for the sample webhook application.
    This class uses Pydantic to manage settings and environment variables.
    """
    github_webhook_secret: str = "sample_webhook_secret"
    github_repo: str = "hammer1209/sample-webhook"
    environment: str = "development"

    @dataclasses.dataclass
    class Config:
        """ Pydantic configuration for settings. """
        env_file = ".env"

settings = Settings()
