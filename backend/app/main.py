from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Educational Bank API",
    description="Simple bank simulation backend for learning purposes",
    version="0.1.0"
)

# Allow frontend access later (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Educational Bank API!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
