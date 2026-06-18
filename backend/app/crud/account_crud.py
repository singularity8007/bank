from sqlalchemy.orm import Session
from ..models.account import Account
from decimal import Decimal
from uuid import UUID

def create_account(db: Session, customer_id: UUID, account_type: str):
    account = Account(
        customer_id=customer_id,
        account_type=account_type,
        available_balance=Decimal("0.00"),
        current_balance=Decimal("0.00"),
        account_status="active"
    )
    db.add(account)
    db.commit()
    db.refresh(account)
    return account

def get_accounts_by_customer(db: Session, customer_id: UUID):
    return db.query(Account).filter(Account.customer_id == customer_id).all()