"""
Backend-only admin routes (not exposed to frontend).
Only accessible via API/Swagger UI or curl commands.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.utils import hash_password
from app.models.schemas import RegisterRequest, RegisterResponse
from app.models.db_models import User

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/register", response_model=RegisterResponse)
async def register(data: RegisterRequest, db: Session = Depends(get_db)) -> RegisterResponse:
    """
    User registration endpoint (BACKEND ONLY).
    
    This endpoint is only accessible via:
    - Swagger UI: http://localhost:8000/docs
    - Curl command: curl -X POST http://localhost:8000/admin/register ...
    - NOT available from frontend HTML/JavaScript
    
    Args:
        data: Registration credentials (username and password)
        db: Database session
    
    Returns:
        RegisterResponse with success status and message
    """
    # Check if username already exists
    existing_user = db.query(User).filter(User.user_name == data.username).first()
    if existing_user:
        return RegisterResponse(success=False, message="Username already exists")
    
    # Create new user with hashed password
    new_user = User(user_name=data.username, password=hash_password(data.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return RegisterResponse(success=True, message=f"User '{data.username}' registered successfully")
