# Login Application - FastAPI + Frontend

A modern, modular login application with a **FastAPI** backend and **HTML/CSS/JavaScript** frontend.

## Project Structure

```
web_project_login_page/
├── backend/                    # FastAPI backend
│   ├── app/
│   │   ├── __init__.py         # Package init
│   │   ├── main.py             # FastAPI app factory
│   │   ├── config.py           # Configuration
│   │   ├── routes/             # API route handlers
│   │   │   ├── __init__.py
│   │   │   └── auth.py         # Authentication endpoints
│   │   └── models/             # Pydantic models
│   │       ├── __init__.py
│   │       └── schemas.py      # Request/response schemas
│   ├── requirements.txt        # Python dependencies
│   └── run.py                  # Entry point to run server
│
├── frontend/                   # Frontend assets
│   ├── pages/                  # HTML pages
│   │   ├── index.html          # Login page
│   │   └── login.html          # Home page (post-login)
│   ├── js/                     # JavaScript files
│   │   └── script.js           # Frontend logic
│   ├── css/                    # Stylesheets
│   │   └── style.css           # Application styles
│   ├── assets/                 # Static assets
│   │   └── favicon.svg         # Site favicon
│   └── favicon.svg             # Favicon (root level for serving)
│
├── README.md                   # This file
└── .gitignore                  # Git ignore rules
```

## Setup Instructions

### Prerequisites
- **Python 3.8+** installed
- **pip** package manager

### 1. Create Virtual Environment

```bash
cd backend
python -m venv venv
```

Activate the virtual environment:

**Windows (CMD):**
```bash
venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Run the Server

From the `backend` directory:

```bash
python run.py
```

Or directly with uvicorn:

```bash
uvicorn app.main:app --reload --port 8000
```

The server will start at **http://localhost:8000/**

## Features

### Backend (FastAPI)
- ✅ RESTful API with `/login` POST endpoint
- ✅ Pydantic models for request/response validation
- ✅ Modular route structure (routes in separate files)
- ✅ Serves frontend static files (HTML, CSS, JS)
- ✅ Proper error handling and logging
- ✅ Auto-reload in development mode

### Frontend (HTML/CSS/JavaScript)
- ✅ Clean, responsive login form
- ✅ Client-side form validation
- ✅ Asynchronous API calls with `fetch()`
- ✅ User-friendly error messages
- ✅ Modern styling with CSS
- ✅ Favicon support

## API Documentation

### Login Endpoint

**URL:** `POST /login`

**Request Body:**
```json
{
    "username": "admin",
    "password": "secret"
}
```

**Response (Success):**
```json
{
    "success": true,
    "message": "Logged in successfully"
}
```

**Response (Failure):**
```json
{
    "success": false,
    "message": "Invalid credentials"
}
```

### Default Credentials
- **Username:** `admin`
- **Password:** `secret`

### Interactive API Documentation

Once the server is running, visit:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## Development Notes

### Adding New Routes

1. Create a new file in `backend/app/routes/` (e.g., `backend/app/routes/users.py`)
2. Define routes using FastAPI decorators
3. Import and include in `backend/app/main.py` using `app.include_router()`

### Example:
```python
# backend/app/routes/users.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id, "name": "John Doe"}
```

Then in `backend/app/main.py`:
```python
from app.routes import auth_router, users_router

app.include_router(auth_router, tags=["auth"])
app.include_router(users_router, tags=["users"])
```

### Environment Variables (Future Enhancement)

For production, use environment variables for configuration:
```python
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
```

## Security Best Practices (TODO)

⚠️ **Current implementation is for development only.** Before production deployment:

- [ ] Implement password hashing (bcrypt, argon2)
- [ ] Add JWT or session-based authentication
- [ ] Use HTTPS/TLS
- [ ] Implement CORS properly (restrict origins)
- [ ] Add rate limiting
- [ ] Use a real database (PostgreSQL, MySQL, etc.)
- [ ] Input validation and sanitization
- [ ] SQL injection prevention (if using ORM)
- [ ] CSRF protection
- [ ] Secure cookie handling

## Troubleshooting

### Port 8000 already in use?
```bash
uvicorn app.main:app --port 8001
```

### CORS errors?
Check that the frontend origin is allowed in `backend/app/main.py`

### Module not found errors?
Ensure you're running from the `backend` directory and the virtual environment is activated.

### Static files not loading?
Verify that the `FRONTEND_DIR` path in `backend/app/config.py` correctly points to the `frontend` folder.

## Technologies Used

| Component | Technology |
|-----------|-----------|
| Backend | FastAPI, Uvicorn, Pydantic |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Package Manager | pip |
| Virtual Environment | venv |

## Future Enhancements

- [ ] User registration endpoint
- [ ] Password reset functionality
- [ ] Email verification
- [ ] User profile management
- [ ] Database integration
- [ ] JWT token authentication
- [ ] Frontend framework (React, Vue, etc.)
- [ ] Unit tests and integration tests
- [ ] Docker containerization
- [ ] CI/CD pipeline

## License

This project is open source and available under the MIT License.

## Author

Created as a learning project for FastAPI and frontend integration.
