import os
from dotenv import load_dotenv

env_path = ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    DATABASE_URL: str = os.getenv("MONGODB_URI")
    MONGO_INITDB_DATABASE: str = os.getenv("MONGO_INITDB_DATABASE")

    # MONGO_INITDB_ROOT_USERNAME: str = os.getenv("MONGO_INITDB_ROOT_USERNAME")
    # MONGO_INITDB_ROOT_PASSWORD: str = os.getenv("MONGO_INITDB_ROOT_PASSWORD")




db_config = Settings()

