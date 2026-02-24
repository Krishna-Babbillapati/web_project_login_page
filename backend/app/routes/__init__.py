"""
Route handlers for the application.
"""
from .auth import router as auth_router
from .admin import router as admin_router

__all__ = ["auth_router", "admin_router"]
