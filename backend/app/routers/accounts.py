from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.account import AccountCreate, AccountResponse
from ..crud.account_crud import create_account
from ..database import get_db
from typing import List
from ..models.account import Account   # needed for the list endpoint

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.post("/", response_model=AccountResponse)
def create_new_account(account: AccountCreate, db: Session = Depends(get_db)):
    return create_account(db, account.customer_id, account.account_type)


@router.get("/", response_model=List[AccountResponse])
def list_my_accounts(db: Session = Depends(get_db)):
    return db.query(Account).all()