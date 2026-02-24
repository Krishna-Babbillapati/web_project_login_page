from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path
from app.models.db_models import Base, insert_sample_user
from app.models.db_models import User

# Get the database file path
DB_DIR = Path(__file__).resolve().parent.parent / "data"
DB_DIR.mkdir(exist_ok=True)
DATABASE_URL = f"sqlite:///{DB_DIR}/app.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables
Base.metadata.create_all(bind=engine)

# Insert sample user if no users exist
def init_db():
    """Initialize database with sample data if empty."""
    db = SessionLocal()
    try:
        user_count = db.query(User).count()
        if user_count == 0:
            insert_sample_user(db)
    finally:
        db.close()

# Initialize database on startup
init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
