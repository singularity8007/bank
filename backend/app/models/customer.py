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
