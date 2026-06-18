from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.account import AccountCreate, AccountResponse
from ..crud.account_crud import create_account, get_accounts_by_customer
from ..database import get_db
from typing import List
from uuid import UUID

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.post("/", response_model=AccountResponse)
def create_new_account(account: AccountCreate, db: Session = Depends(get_db)):
    # Use a proper UUID
    customer_id = UUID("00000000-0000-0000-0000-000000000000")
    return create_account(db, customer_id, account.account_type)


@router.get("/", response_model=List[AccountResponse])
def list_my_accounts(db: Session = Depends(get_db)):
    customer_id = UUID("00000000-0000-0000-0000-000000000000")
    return get_accounts_by_customer(db, customer_id)