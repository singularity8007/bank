from sqlalchemy import Column, String, Numeric, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from datetime import datetime
from ..database import Base

class Account(Base):
    __tablename__ = "accounts"

    account_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(PG_UUID(as_uuid=True), nullable=False)
    account_type = Column(String(50), nullable=False)

    available_balance = Column(Numeric(10, 2), default=0.00)
    current_balance = Column(Numeric(10, 2), default=0.00)
    account_status = Column("account_status", String(50), nullable=False, default="active")
    create_time = Column("create_time", DateTime, default=datetime.utcnow)