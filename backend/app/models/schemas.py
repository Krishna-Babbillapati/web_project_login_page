"""
Pydantic schemas for request/response validation.
"""
from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    """Login request schema."""
    username: str = Field(..., min_length=1, description="Username")
    password: str = Field(..., min_length=1, description="Password")

    class Config:
        schema_extra = {
            "example": {
                "username": "admin",
                "password": "secret"
            }
        }


class LoginResponse(BaseModel):
    """Login response schema."""
    success: bool
    message: str


class RegisterRequest(BaseModel):
    """Register request schema."""
    username: str = Field(..., min_length=1, description="Username")
    password: str = Field(..., min_length=1, description="Password")

    class Config:
        schema_extra = {
            "example": {
                "username": "admin",
                "password": "secret"
            }
        }


class RegisterResponse(BaseModel):
    """Register response schema."""
    success: bool
    message: str


class UpdateUserRequest(BaseModel):
    """Update user request schema."""
    username: str = Field(..., min_length=1, description="Username")
    password: str = Field(..., min_length=1, description="Password")

    class Config:
        schema_extra = {
            "example": {
                "username": "admin",
                "password": "secret"
            }
        }


class UpdateUserResponse(BaseModel):
    """Update user response schema."""
    success: bool
    message: str


class DeleteUserRequest(BaseModel):
    """Delete user request schema."""
    username: str = Field(..., min_length=1, description="Username")

    class Config:
        schema_extra = {
            "example": {
                "username": "admin"
            }
        }


class DeleteUserResponse(BaseModel):
    """Delete user response schema."""
    success: bool
    message: str
