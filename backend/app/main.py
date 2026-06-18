from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import the routers
from app.routers import auth, accounts

app = FastAPI(
    title="Educational Bank API",
    description="Simple bank simulation backend for learning purposes",
    version="0.1.0"
)

# Allow frontend access later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routers (this makes /auth/signup appear)
app.include_router(auth.router)
app.include_router(accounts.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Educational Bank API!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}