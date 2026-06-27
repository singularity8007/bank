from sqlalchemy.orm import Session
from ..models.customers import Customers
from ..schemas.customers import CustomerCreate
from argon2 import PasswordHasher
import uuid

ph = PasswordHasher()

def create_customer(db: Session, customers: CustomerCreate):
    """Create a new customer with hashed password."""
    hashed_password = ph.hash(customers.password)
    
    db_customer = Customers(
        customerid=uuid.uuid4(),           # ← lowercase
        firstname=customers.first_name,
        lastname=customers.last_name,
        email=customers.email,
        phonenumber=customers.phone_number,
        ssn=customers.ssn,
        dateofbirth=customers.date_of_birth,
        cust_address=customers.address,
        password_hash=hashed_password,
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_customer_by_email(db: Session, email: str):
    # Use the correct attribute name from the model
    return db.query(Customers).filter(Customers.email == email).first()