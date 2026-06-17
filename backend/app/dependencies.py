from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .database import get_db
# TODO: Add current user dependency using sessions later

def get_current_user(db: Session = Depends(get_db)):
    """
    Placeholder for getting the currently logged-in user.
    Will be implemented when we add session-based authentication.
    """
    # For now, return None or raise error
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Not implemented yet"
    )
