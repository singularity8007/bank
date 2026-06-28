from app.database import get_connection
from app.logging_config import logger
from decimal import Decimal
import uuid
from uuid import UUID


def create_account(customer_id: UUID, account_type: str):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            account_id = uuid.uuid4()   # ← Generate UUID here

            cur.execute("""
                INSERT INTO account (
                    account_id, 
                    customer_id, 
                    account_type, 
                    available_balance, 
                    current_balance, 
                    account_status
                ) VALUES (
                    %(account_id)s,
                    %(customer_id)s,
                    %(account_type)s,
                    0.00,
                    0.00,
                    'active'
                )
                RETURNING account_id, customer_id, account_type, available_balance, current_balance, account_status
            """, {
                "account_id": account_id,
                "customer_id": customer_id,
                "account_type": account_type
            })

            result = cur.fetchone()
            conn.commit()
            logger.info(f"Account created for customer {customer_id}")
            return result

    except Exception as e:
        conn.rollback()
        logger.error(f"Error creating account: {e}")
        raise
    finally:
        conn.close()


def deposit_money(account_id: UUID, amount: Decimal):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            # Get current balances
            cur.execute("""
                SELECT available_balance, current_balance 
                FROM account 
                WHERE account_id = %(account_id)s
            """, {"account_id": account_id})

            account = cur.fetchone()
            if not account:
                raise Exception("Account not found")

            new_available = account["available_balance"] + amount
            new_current = account["current_balance"] + amount

            # Update balances
            cur.execute("""
                UPDATE account
                SET available_balance = %(new_available)s,
                    current_balance = %(new_current)s
                WHERE account_id = %(account_id)s
                RETURNING account_id, customer_id, account_type, available_balance, current_balance, account_status
            """, {
                "account_id": account_id,
                "new_available": new_available,
                "new_current": new_current
            })

            result = cur.fetchone()
            conn.commit()

            logger.info(f"Deposit of {amount} completed for account {account_id}")
            return result

    except Exception as e:
        conn.rollback()
        logger.error(f"Error during deposit: {e}")
        raise
    finally:
        conn.close()