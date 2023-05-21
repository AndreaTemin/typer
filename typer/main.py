from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

import jwt
SECRET_KEY = "your-secret-key"

# from .database import user_db

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}


@app.post("/api/register")
#def user_register(user: UserCreate): #TODO understand how manage API data in input 
def user_register():  
    # Validate user input
    # Check if the username or email already exists in the database
    # Create a new user record in the database
    # Return success message or appropriate response
    pass

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

@app.post("/api/login")
def login(username: str, password: str):
    # Perform authentication logic and verify user credentials
    # If valid, generate a JWT token
    user_id = "to be defined"
    token = create_jwt_token(user_id)
    return {"token": token}

@app.get("/api/lessons")
def get_lessons():
    # Fetch all typing lessons from the database
    # Return the lessons as a JSON response
    pass

@app.get("/api/lessons/{lesson_id}/exercises")
def get_exercises(lesson_id: int):
    # Fetch exercises for a specific lesson from the database based on the lesson_id
    # Return the exercises as a JSON response
    pass

@app.post("/api/exercises/{exercise_id}/results")
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

@app.get("/protected", dependencies=[Depends(authenticate_token)])
def protected_route():
    return {"message": "This is a protected route."}