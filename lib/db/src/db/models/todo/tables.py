import datetime as dt

from sqlalchemy import Integer, String, DateTime, Identity
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Items(Base):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(Integer, Identity(always=False), primary_key=True)
    task: Mapped[str] = mapped_column(String, nullable=False)
    completed_at: Mapped[dt.datetime] = mapped_column(DateTime, nullable=True)
    completed_by: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(DateTime, nullable=False)
    created_by: Mapped[str] = mapped_column(String, nullable=False)
    updated_at: Mapped[dt.datetime] = mapped_column(DateTime, nullable=False)
    updated_by: Mapped[str] = mapped_column(String, nullable=False)
