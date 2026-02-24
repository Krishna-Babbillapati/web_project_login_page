from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from app.utils import hash_password

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    user_name = Column(String, unique=True, index=True, primary_key=True)
    password = Column(String)  # Stores bcrypt-hashed password


def insert_sample_user(session):
    """Insert a sample user into the database with hashed password."""
    # Hash the password before storing
    hashed_pwd = hash_password("secret")
    sample_user = User(user_name="admin", password=hashed_pwd)
    session.add(sample_user)
    session.commit()


def insert_any_user(session, username: str, password: str):
    """Insert a user with specified username and password (hashed)."""
    hashed_pwd = hash_password(password)
    new_user = User(user_name=username, password=hashed_pwd)
    session.add(new_user)
    session.commit()


def update_user_password(session, username: str, new_password: str):
    """Update the password for a given user."""
    user = session.query(User).filter(User.user_name == username).first()
    if user:
        user.password = hash_password(new_password)
        session.commit()


def delete_user(session, username: str):
    """Delete a user from the database."""
    user = session.query(User).filter(User.user_name == username).first()
    if user:
        session.delete(user)
        session.commit()
