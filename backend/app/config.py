"""
Application configuration.
"""
from pathlib import Path

# Get the root directory of the project
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Frontend directory path (mount entire frontend folder)
FRONTEND_DIR = PROJECT_ROOT / "frontend"

# Logging
LOG_LEVEL = "info"
