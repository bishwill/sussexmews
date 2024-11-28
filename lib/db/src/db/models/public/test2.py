from sqlalchemy import Column, Integer, String

from .base import Base


class Test2(Base):
    __tablename__ = "test2"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
