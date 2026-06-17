#!/usr/bin/env python3
"""
Backend Scaffold Generator for the Educational Bank Project

This script creates the complete backend folder structure with starter files.
Run it once to bootstrap your project.

Usage:
    python generate_backend.py

It will create a 'backend/' folder in the current directory.
"""

import os
from pathlib import Path

# ============================================================
# CONFIGURATION
# ============================================================
BACKEND_DIR = Path("backend")
APP_DIR = BACKEND_DIR / "app"

# ============================================================
# HELPER FUNCTIONS
# ============================================================
def create_file(path: Path, content: str = ""):
    """Create a file with optional content. Skip if exists."""
    if path.exists():
        print(f"  [SKIP] {path} already exists")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"  [CREATED] {path}")

def create_init_file(directory: Path):
    """Create an __init__.py file in a directory."""
    init_file = directory / "__init__.py"
    create_file(init_file, '"""Package initialization."""\n')

# ============================================================
# MAIN GENERATION
# ============================================================
def generate_backend():
    print("\n🚀 Generating Educational Bank Backend Structure...\n")

    # --- Root backend files ---
    create_file(BACKEND_DIR / "README.md", """
# Bank Backend

This is the FastAPI backend for the educational bank simulation project.

## How to run

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate     # Linux/Mac
   .venv\\Scripts\\activate      # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and fill in your database credentials.

4. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

Visit http://127.0.0.1:8000/docs for the interactive API documentation.
""")

    create_file(BACKEND_DIR / "requirements.txt", """
# Educational Bank Backend - Pinned versions (June 2026)
fastapi==0.137.1
uvicorn[standard]==0.30.1
sqlalchemy==2.0.51
pydantic==2.13.4
python-dotenv==1.2.2
argon2-cffi==25.1.0
psycopg2-binary==2.9.9          # PostgreSQL driver
""")

    create_file(BACKEND_DIR / ".env.example", """
# Copy this file to .env and update values
DATABASE_URL=postgresql://bankuser:bankpassword@localhost:5432/bankdb
SECRET_KEY=change-this-to-a-very-long-random-string
""")

    # --- app/ directory ---
    create_init_file(APP_DIR)

    # main.py
    create_file(APP_DIR / "main.py", """
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Educational Bank API",
    description="Simple bank simulation backend for learning purposes",
    version="0.1.0"
)

# Allow frontend access later (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Educational Bank API!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
""")

    # database.py
    create_file(APP_DIR / "database.py", """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://bankuser:bankpassword@localhost:5432/bankdb")

engine = create_engine(DATABASE_URL, echo=True)  # echo=True shows SQL (good for learning)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    \"\"\"Dependency for FastAPI routes to get a database session.\"\"\"
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
""")

    # dependencies.py
    create_file(APP_DIR / "dependencies.py", """
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .database import get_db
# TODO: Add current user dependency using sessions later

def get_current_user(db: Session = Depends(get_db)):
    \"\"\"
    Placeholder for getting the currently logged-in user.
    Will be implemented when we add session-based authentication.
    \"\"\"
    # For now, return None or raise error
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Not implemented yet"
    )
""")

    # --- models/ ---
    models_dir = APP_DIR / "models"
    create_init_file(models_dir)

    create_file(models_dir / "customer.py", """
from sqlalchemy import Column, String, Date, UUID
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
import uuid
from ..database import Base

class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    phone_number = Column(String(20), unique=True, nullable=False)
    ssn = Column(String(11), unique=True, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    address = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)

    # TODO: Add relationship to accounts later
""")

    create_file(models_dir / "account.py", """
from sqlalchemy import Column, String, Numeric, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class Account(Base):
    __tablename__ = "accounts"

    account_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(ForeignKey("customers.customer_id"), nullable=False)
    account_type = Column(String(20), nullable=False)  # checking or savings
    available_balance = Column(Numeric(10, 2), default=0.00)
    current_balance = Column(Numeric(10, 2), default=0.00)
    status = Column(String(20), default="active")  # active, closed
    created_at = Column(DateTime, default=datetime.utcnow)

    # TODO: Add relationship to transactions
""")

    create_file(models_dir / "transaction.py", """
from sqlalchemy import Column, String, Numeric, DateTime, ForeignKey, UUID
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
import uuid
from datetime import datetime
from ..database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    source_account_id = Column(ForeignKey("accounts.account_id"))
    recipient_account_id = Column(ForeignKey("accounts.account_id"))
    amount = Column(Numeric(10, 2), nullable=False)
    transaction_type = Column(String(50), nullable=False)
    status = Column(String(20), default="PENDING")  # PENDING, SETTLED, ROLLED_BACK
    transaction_date = Column(DateTime, default=datetime.utcnow)
    notes = Column(String(512))
    direction = Column(String(10))  # INCOMING or OUTGOING
""")

    create_file(models_dir / "session.py", """
from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, Integer
from datetime import datetime, timedelta
from ..database import Base

class Session(Base):
    __tablename__ = "sessions"

    session_id = Column(String(128), primary_key=True)
    customer_id = Column(ForeignKey("customers.customer_id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_active_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(days=7))
    is_active = Column(Boolean, default=True)
    ip_address = Column(String(45))
""")

    # --- schemas/ ---
    schemas_dir = APP_DIR / "schemas"
    create_init_file(schemas_dir)

    create_file(schemas_dir / "customer.py", """
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
""")

    create_file(schemas_dir / "account.py", """
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
""")

    # --- crud/ ---
    crud_dir = APP_DIR / "crud"
    create_init_file(crud_dir)

    create_file(crud_dir / "customer_crud.py", """
from sqlalchemy.orm import Session
from ..models.customer import Customer
from ..schemas.customer import CustomerCreate
from argon2 import PasswordHasher
import uuid

ph = PasswordHasher()

def create_customer(db: Session, customer: CustomerCreate):
    \"\"\"Create a new customer with hashed password.\"\"\"
    hashed_password = ph.hash(customer.password)
    db_customer = Customer(
        customer_id=uuid.uuid4(),
        first_name=customer.first_name,
        last_name=customer.last_name,
        email=customer.email,
        phone_number=customer.phone_number,
        ssn=customer.ssn,
        date_of_birth=customer.date_of_birth,
        address=customer.address,
        password_hash=hashed_password,
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_customer_by_email(db: Session, email: str):
    return db.query(Customer).filter(Customer.email == email).first()
""")

    create_file(crud_dir / "account_crud.py", """
from sqlalchemy.orm import Session
from ..models.account import Account
from decimal import Decimal

def create_account(db: Session, customer_id: str, account_type: str):
    account = Account(
        customer_id=customer_id,
        account_type=account_type,
        available_balance=Decimal("0.00"),
        current_balance=Decimal("0.00"),
        status="active"
    )
    db.add(account)
    db.commit()
    db.refresh(account)
    return account

def get_accounts_by_customer(db: Session, customer_id: str):
    return db.query(Account).filter(Account.customer_id == customer_id).all()
""")

    # --- routers/ ---
    routers_dir = APP_DIR / "routers"
    create_init_file(routers_dir)

    create_file(routers_dir / "auth.py", """
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..schemas.customer import CustomerCreate, CustomerResponse
from ..crud.customer_crud import create_customer, get_customer_by_email
from ..database import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/signup", response_model=CustomerResponse)
def signup(customer: CustomerCreate, db: Session = Depends(get_db)):
    existing = get_customer_by_email(db, customer.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_customer = create_customer(db, customer)
    return new_customer
""")

    create_file(routers_dir / "accounts.py", """
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.account import AccountCreate, AccountResponse
from ..crud.account_crud import create_account, get_accounts_by_customer
from ..database import get_db
from typing import List

router = APIRouter(prefix="/accounts", tags=["Accounts"])

@router.post("/", response_model=AccountResponse)
def create_new_account(account: AccountCreate, db: Session = Depends(get_db)):
    # TODO: Get customer_id from current logged in user
    customer_id = "00000000-0000-0000-0000-000000000000"  # placeholder
    return create_account(db, customer_id, account.account_type)

@router.get("/", response_model=List[AccountResponse])
def list_my_accounts(db: Session = Depends(get_db)):
    # TODO: Get customer_id from session
    customer_id = "00000000-0000-0000-0000-000000000000"
    return get_accounts_by_customer(db, customer_id)
""")

    # --- utils/ ---
    utils_dir = APP_DIR / "utils"
    create_init_file(utils_dir)

    create_file(utils_dir / "security.py", """
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

def hash_password(password: str) -> str:
    return ph.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        ph.verify(hashed_password, plain_password)
        return True
    except VerifyMismatchError:
        return False
""")

    print("\n✅ Backend structure generated successfully!")
    print(f"\nNext steps:")
    print(f"  1. cd backend")
    print(f"  2. python -m venv .venv && source .venv/bin/activate")
    print(f"  3. pip install -r requirements.txt")
    print(f"  4. cp .env.example .env   # then edit .env with your DB credentials")
    print(f"  5. uvicorn app.main:app --reload")
    print(f"\nVisit http://127.0.0.1:8000/docs to see your API.\n")


if __name__ == "__main__":
    generate_backend()
