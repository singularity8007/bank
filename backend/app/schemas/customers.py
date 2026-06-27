from pydantic import BaseModel, EmailStr, Field
from uuid import UUID


class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    ssn: str
    date_of_birth: str
    address: str
    password: str


class CustomerResponse(BaseModel):
    customer_id: UUID = Field(validation_alias="customerid", serialization_alias="customer_id")
    first_name: str = Field(validation_alias="firstname", serialization_alias="first_name")
    last_name: str = Field(validation_alias="lastname", serialization_alias="last_name")
    email: EmailStr

    model_config = {"from_attributes": True}