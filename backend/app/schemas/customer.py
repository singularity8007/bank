from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional
from uuid import UUID

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
    customer_id: UUID
    first_name: str
    last_name: str
    email: EmailStr

    model_config = {"from_attributes": True}