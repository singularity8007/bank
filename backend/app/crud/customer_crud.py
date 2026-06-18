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
        customerid=uuid.uuid4(),           # ← lowercase
        firstname=customer.first_name,
        lastname=customer.last_name,
        email=customer.email,
        phonenumber=customer.phone_number,
        ssn=customer.ssn,
        dateofbirth=customer.date_of_birth,
        cust_address=customer.address,
        password_hash=hashed_password,
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_customer_by_email(db: Session, email: str):
    # Use the correct attribute name from the model
    return db.query(Customer).filter(Customer.email == email).first()