from fastapi import APIRouter, HTTPException, Request
from app.services.account_service import create_account, deposit_money
from app.logging_config import logger
from decimal import Decimal
from uuid import UUID

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.post("/")
async def create_new_account(request: Request):
    data = await request.json()

    try:
        customer_id = UUID(data["customer_id"])
        account_type = data["account_type"]

        logger.info(f"Creating {account_type} account for customer {customer_id}")

        new_account = create_account(customer_id, account_type)
        return new_account

    except Exception as e:
        logger.error(f"Failed to create account: {e}")
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/deposit")
async def deposit(request: Request):
    data = await request.json()

    try:
        account_id = UUID(data["account_id"])
        amount = Decimal(str(data["amount"]))  # Convert safely to Decimal

        logger.info(f"Deposit request: {amount} to account {account_id}")

        updated_account = deposit_money(account_id, amount)
        return updated_account

    except Exception as e:
        logger.error(f"Deposit failed: {e}")
        raise HTTPException(status_code=400, detail=str(e))