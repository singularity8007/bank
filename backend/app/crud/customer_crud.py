from sqlalchemy.orm import Session
from ..models.customer import Customer
from ..schemas.customer import CustomerCreate
from argon2 import PasswordHasher
import uuid

ph = PasswordHasher()

def create_customer(db: Session, customer: CustomerCreate):
    """Create a new customer with hashed password."""
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
