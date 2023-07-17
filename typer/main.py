import uvicorn
from API.user_management.api_user import router
from fastapi import FastAPI


app = FastAPI(debug=True)

app.include_router(router)

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)