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
