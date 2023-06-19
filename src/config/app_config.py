import os
from dotenv import load_dotenv

dotenv_path = ".env"
load_dotenv(dotenv_path)

class AppConfig:
    MLFLOW_TRACKING_URI = os.environ.get("MLFLOW_TRACKING_URI")
    MLFLOW_MODEL_PREFIX = "model"


if __name__ == "__main__":
    print(AppConfig.MLFLOW_TRACKING_URI)
