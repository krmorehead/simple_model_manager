import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    Configuration class that loads environment variables, supporting .env files for environment-specific settings.
    """
    MODEL_TYPE: str = os.getenv('MODEL_TYPE', 'nllb-600m')
    MODEL_PATH: str = os.getenv('MODEL_PATH', '/models/nllb-600m')
    FLASK_ENV: str = os.getenv('FLASK_ENV', 'development')
    LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO') 