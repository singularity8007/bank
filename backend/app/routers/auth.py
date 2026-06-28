from fastapi import APIRouter, HTTPException
from app.services.customer_service import create_customer, get_customer_by_email
from app.logging_config import logger
from pydantic import BaseModel, EmailStr
from datetime import date

router = APIRouter(prefix="/auth", tags=["Authentication"])


class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    ssn: str
    date_of_birth: date
    address: str
    password: str


@router.post("/signup")
def signup(customer: CustomerCreate):
    logger.info(f"Signup attempt for email: {customer.email}")

    # Check if email already exists
    existing = get_customer_by_email(customer.email)
    if existing:
        logger.warning(f"Signup failed - email already exists: {customer.email}")
        raise HTTPException(status_code=400, detail="Email already registered")

    try:
        new_customer = create_customer(customer)
        logger.info(f"Customer created successfully: {new_customer['email']}")
        return new_customer
    except Exception as e:
        logger.error(f"Error creating customer: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
