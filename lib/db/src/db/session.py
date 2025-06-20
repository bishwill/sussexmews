from sqlalchemy.orm import Session, sessionmaker

from .engine import get_engine

def get_session() -> Session:
    return sessionmaker(bind=get_engine())