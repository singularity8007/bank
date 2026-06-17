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
