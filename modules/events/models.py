""""Data models for events."""

import datetime

from alembic.environment import Any, Optional
from sqlalchemy import JSON, DateTime, Index, Integer, String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedAsDataclass,
    mapped_column,
)


class Base(DeclarativeBase, MappedAsDataclass):
    """Base class for SQLAlchemy models with dataclass support."""

class Event(Base):
    """Event reported by a robot."""

    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    robot_id: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    timestamp: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True),
                                                         nullable=False, index=True)

    event_type: Mapped[str] = mapped_column(String, nullable=False)
    severity: Mapped[str] = mapped_column(String, nullable=False)
    message: Mapped[str] = mapped_column(String, nullable=False)

    payload: Mapped[Optional[dict[str, Any]]] = mapped_column(JSON)

    __table_args__ = (
        Index("idx_events_robot_timestamp", "robot_id", "timestamp"),
    )
