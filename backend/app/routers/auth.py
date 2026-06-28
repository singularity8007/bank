from fastapi import APIRouter, HTTPException, Request
from app.services.customer_service import create_customer, get_customer_by_email
from app.logging_config import logger

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/signup")
async def signup(request: Request):
    data = await request.json()

    logger.info(f"Signup attempt for email: {data.get('email')}")

    # Check if email already exists
    existing = get_customer_by_email(data["email"])
    if existing:
        logger.warning(f"Signup failed - email already exists: {data['email']}")
        raise HTTPException(status_code=400, detail="Email already registered")

    try:
        new_customer = create_customer(data)
        logger.info(f"Customer created successfully: {new_customer['email']}")
        return new_customer
    except Exception as e:
        logger.error(f"Error creating customer: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")