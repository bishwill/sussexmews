from sqlalchemy.orm import Session

from .engine import get_engine

def get_session() -> Session:
    return Session(bind=get_engine())