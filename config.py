# config.py
from dotenv import load_dotenv
import os

load_dotenv()

CONFIG = {
    "linkedin_email": os.getenv("LINKEDIN_EMAIL"),
    "linkedin_password": os.getenv("LINKEDIN_PASSWORD"),
    "db_path": os.getenv("DB_PATH", "./db/jobs.db"),
}
