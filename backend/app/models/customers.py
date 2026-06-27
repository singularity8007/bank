from sqlalchemy import Column, String, Date
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
import uuid
from ..database import Base

class Customers(Base):
    __tablename__ = "customers"

    customerid = Column("customerid", PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    firstname = Column("firstname", String(50), nullable=False)
    lastname = Column("lastname", String(50), nullable=False)
    email = Column("email", String(100), unique=True, nullable=False, index=True)
    phonenumber = Column("phonenumber", String(20), unique=True, nullable=False)
    ssn = Column("socialsecuritynumber", String(11), unique=True, nullable=False)   # ← Important
    dateofbirth = Column("dateofbirth", Date, nullable=False)
    cust_address = Column("cust_address", String(255), nullable=False)
    password_hash = Column("password_hash", String(255), nullable=False)