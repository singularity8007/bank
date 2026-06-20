from pydantic import BaseModel, Field
from uuid import UUID
from decimal import Decimal


class AccountCreate(BaseModel):
    customer_id: UUID
    account_type: str


class AccountResponse(BaseModel):
    account_id: UUID
    customer_id: UUID
    account_type: str
    available_balance: Decimal
    current_balance: Decimal
    account_status: str = Field(..., alias="account_status")

    model_config = {"from_attributes": True}