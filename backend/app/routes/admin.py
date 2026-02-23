"""
Backend-only admin routes (not exposed to frontend).
Only accessible via API/Swagger UI or curl commands.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.utils import hash_password
from app.models.schemas import RegisterRequest, RegisterResponse, UpdateUserRequest, UpdateUserResponse, DeleteUserResponse, DeleteUserRequest
from app.models.db_models import User, insert_any_user, update_user_password, delete_user as db_delete_user

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
    insert_any_user(session=db, username=data.username, password=data.password)
    
    return RegisterResponse(success=True, message=f"User '{data.username}' registered successfully")


@router.post("/update-password", response_model=UpdateUserResponse)
async def update_password(data: UpdateUserRequest, db: Session = Depends(get_db)) -> UpdateUserResponse:
    """
    Update user password endpoint (BACKEND ONLY).
    
    Args:
        data: Updated user credentials (username and new password)
        db: Database session
    
    Returns:
        UpdateUserResponse with success status and message
    """
    try:
        update_user_password(session=db, username=data.username, new_password=data.password)
        if db.query(User).filter(User.user_name == data.username).first() is None:
            return UpdateUserResponse(success=False, message=f"User '{data.username}' not found")
    except Exception as e:
        return UpdateUserResponse(success=False, message=f"Failed to update password: {str(e)}")
    
    return UpdateUserResponse(success=True, message=f"Password updated for user '{data.username}'")


@router.post("/delete-user", response_model=DeleteUserResponse)
async def delete_user(data: DeleteUserRequest, db: Session = Depends(get_db)) -> DeleteUserResponse:
    """
    Delete user endpoint (BACKEND ONLY).
    
    Args:
        data: Delete user request data (username)
        db: Database session
    
    Returns:
        DeleteUserResponse with success status and message
    """
    # call the database helper (aliased above) to avoid recursive name conflict
    try:
        db_delete_user(session=db, username=data.username)
        if db.query(User).filter(User.user_name == data.username).first() is None:
            return DeleteUserResponse(success=False, message=f'User "{data.username}" does not exist')
    except Exception as e:
        return DeleteUserResponse(success=False, message=f"Failed to delete user: {str(e)}")
    
    return DeleteUserResponse(success=True, message=f"User '{data.username}' deleted successfully")

