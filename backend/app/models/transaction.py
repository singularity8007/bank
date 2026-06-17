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
