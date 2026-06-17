from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..schemas.customer import CustomerCreate, CustomerResponse
from ..crud.customer_crud import create_customer, get_customer_by_email
from ..database import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/signup", response_model=CustomerResponse)
def signup(customer: CustomerCreate, db: Session = Depends(get_db)):
    existing = get_customer_by_email(db, customer.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_customer = create_customer(db, customer)
    return new_customer
