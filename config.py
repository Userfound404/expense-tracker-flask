import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key')
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'sqlite:///data.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Default budget for summary cards
    DEFAULT_BUDGET = float(os.getenv('DEFAULT_BUDGET', 80000))