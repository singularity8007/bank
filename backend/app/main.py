from fastapi import FastAPI
from app.logging_config import logger
from app.routers import auth, accounts

app = FastAPI(
    title="Simple Bank API",
    description="Educational bank project using raw SQL",
    version="1.0.0"
)

# Include routers
app.include_router(auth.router)
app.include_router(accounts.router)


@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {"message": "Welcome to Simple Bank API"}