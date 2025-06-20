from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from db import get_engine

def get_session():
    with Session(bind=get_engine()) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]