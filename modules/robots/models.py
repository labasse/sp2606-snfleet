"""Data models for Qt views."""

from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedAsDataclass,
    mapped_column,
)


class Base(DeclarativeBase, MappedAsDataclass):
    """Base class for SQLAlchemy models with dataclass support."""

class Robot(Base):
    """Represents a robot with computed status and criticity."""

    __tablename__ = "robots"

    robot_id: Mapped[str] = mapped_column(String, primary_key=True)
    display_name: Mapped[str] = mapped_column(String, nullable=False)
    model: Mapped[str] = mapped_column(String, nullable=False)
    site_id: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                 nullable=False)
