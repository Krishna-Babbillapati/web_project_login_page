"""
Authentication routes.
"""
from fastapi import APIRouter
from app.models import LoginRequest
from app.models.schemas import LoginResponse

router = APIRouter()


@router.post("/login", response_model=LoginResponse)
async def login(data: LoginRequest) -> LoginResponse:
    """
    User login endpoint.
    
    Args:
        data: Login credentials (username and password)
    
    Returns:
        LoginResponse with success status and message
    """
    # Replace with real auth logic (DB, hashing, JWT, etc.)
    if data.username == "admin" and data.password == "secret":
        return LoginResponse(success=True, message="Logged in successfully")
    return LoginResponse(success=False, message="Invalid credentials")
