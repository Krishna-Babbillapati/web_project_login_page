"""
FastAPI application factory and main entry point.
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from app.config import FRONTEND_DIR
from app.routes import auth_router, admin_router


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="Login API",
        description="A simple login API with static frontend serving",
        version="1.0.0"
    )

    # Include public authentication routes
    app.include_router(auth_router, tags=["auth"])
    
    # Include backend-only admin routes
    app.include_router(admin_router, tags=["admin"])

    # Serve frontend static files at the root
    # Mount AFTER routes so API routes take precedence
    app.mount(
        "/",
        StaticFiles(directory=str(FRONTEND_DIR), html=True),
        name="static"
    )

    return app


app = create_app()