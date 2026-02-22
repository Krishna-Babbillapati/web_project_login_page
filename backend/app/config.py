"""
Application configuration.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Get the root directory of the project
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Frontend directory path (mount entire frontend folder)
FRONTEND_DIR = PROJECT_ROOT / "frontend"

# Logging
LOG_LEVEL = "info"

# Database configuration
# load_dotenv()
# DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/app.db")