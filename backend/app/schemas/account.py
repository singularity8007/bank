from pydantic import BaseModel
from decimal import Decimal
from typing import Literal

class AccountCreate(BaseModel):
    account_type: Literal["checking", "savings"]

class AccountResponse(BaseModel):
    account_id: int
    customer_id: str
    account_type: str
    available_balance: Decimal
    current_balance: Decimal
    status: str

    class Config:
        from_attributes = True
