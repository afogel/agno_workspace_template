from os import getenv
from typing import Optional

from pydantic_settings import BaseSettings


class DbSettings(BaseSettings):
    """Database settings that can be set using environment variables.

    Reference: https://docs.pydantic.dev/latest/usage/pydantic_settings/
    """
    
    model_config = {"env_file": ".env", "extra": "ignore"}

    # Database configuration - set via environment variables
    db_host: str
    db_port: int = 5432
    db_user: str
    db_pass: str = ""
    db_database: str
    db_driver: str = "postgresql+psycopg"
    # Create/Upgrade database on startup using alembic
    migrate_db: bool = True

    def get_db_url(self) -> str:
        db_url = "{}://{}{}@{}:{}/{}".format(
            self.db_driver,
            self.db_user,
            f":{self.db_pass}" if self.db_pass else "",
            self.db_host,
            self.db_port,
            self.db_database,
        )
        return db_url


# Create DbSettings object
db_settings = DbSettings()
