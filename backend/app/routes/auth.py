"""
Authentication routes.
"""
from app.database import get_db
from app.utils import hash_password, verify_password
from app.models.schemas import LoginRequest, LoginResponse
from app.models.db_models import User
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/login", response_model=LoginResponse)
async def login(data: LoginRequest, db: Session = Depends(get_db)) -> LoginResponse:
    """
    User login endpoint with password verification.
    
    Args:
        data: Login credentials (username and password)
        db: Database session
    
    Returns:
        LoginResponse with success status and message
    """
    # Query user from database
    user = db.query(User).filter(User.user_name == data.username).first()
    
    # Check if user exists and password is correct
    if user and verify_password(data.password, user.password):
        return LoginResponse(success=True, message="Logged in successfully")
    
    return LoginResponse(success=False, message="Invalid username or password")
