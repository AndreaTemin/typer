import uuid
import jwt

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import datetime
from database import get_db, User
from .user_validation import is_valid_email, is_valid_name, is_valid_password
from sqlalchemy.orm import Session


router = APIRouter()

SECRET_KEY = "your-secret-key"


@router.get("/")
def root():
    # db = SessionLocal()
    # # Perform database operations using the session (db)
    # db.close()
    return {"message": "Hello, World!"}

class UserCreate(BaseModel):
    username: str
    password: str
    email: str | None

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/api/register")
def user_register(new_user: UserCreate):
    if not is_valid_email(new_user.email):
        raise HTTPException(status_code=400, detail="Invalid email address")
    if not is_valid_name(new_user.username):
        raise HTTPException(status_code=400, detail="Invalid username")
    if not is_valid_password(new_user.password):
        raise HTTPException(status_code=400, detail="Invalid password")
    
    # Create a new session
    with get_db() as db:
        existing_email = db.query(User).filter(User.email==new_user.email).first()
        if existing_email:
            raise HTTPException(status_code=400, detail="Email already exists")
        
        existing_username = db.query(User).filter(User.username==new_user.username).first()
        if existing_username:
            raise HTTPException(status_code=400, detail="Username already exists")


        now = datetime.utcnow().isoformat(sep=" ", timespec="seconds")
        user = User(
            id = str(uuid.uuid4()),
            username = new_user.username,
            email = new_user.email,
            password = new_user.password,
            created_at = now,
            updated_at = now
        )
            
        # Add the new user to the database
        db.add(user)
        db.commit()

    return {"message": "User created successfully"}

def authenticate_token(auth: HTTPAuthorizationCredentials = Depends(HTTPBearer())) -> dict:
    token = auth.credentials
    payload = decode_jwt_token(token)
    return payload

def decode_jwt_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.DecodeError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )
    
def create_jwt_token(user_id: int) -> str:
    payload = {"user_id": user_id}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

@router.post("/api/login")
def login(username: str, password: str):
    # Perform authentication logic and verify user credentials
    # If valid, generate a JWT token
    user_id = "to be defined"
    token = create_jwt_token(user_id)
    return {"token": token}

@router.get("/api/lessons")
def get_lessons():
    
    return "test"

@router.get("/api/lessons/{lesson_id}/exercises")
def get_exercises(lesson_id: int):
    # Fetch exercises for a specific lesson from the database based on the lesson_id
    # Return the exercises as a JSON response
    pass

@router.post("/api/exercises/{exercise_id}/results")
# def submit_results(
#     exercise_id: int,
#     results: ExerciseResult,
#     user_id: int = Depends(HKEY_CURRENT_USER)
# ):
def submit_results():
    # Validate input
    # Check if the exercise_id exists in the database
    # Calculate performance metrics (e.g., duration, accuracy)
    # Store the result in the database with associated user_id and exercise_id
    # Return success message or appropriate response
    pass

# Additional helper function(s)

def get_current_user():
    # Implement a function to get the current authenticated user based on the JWT token
    # This function can be used as a dependency in the submit_results endpoint
    # Return the user_id or raise an HTTPException if the user is not authenticated
    pass

@router.get("/protected", dependencies=[Depends(authenticate_token)])
def protected_route():
    return {"message": "This is a protected route."}