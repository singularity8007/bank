from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    ssn: str
    date_of_birth: date
    address: str
    password: str

class CustomerResponse(BaseModel):
    customer_id: str
    first_name: str
    last_name: str
    email: EmailStr

    class Config:
        from_attributes = True
