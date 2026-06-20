"""Data models for Qt views."""

from datetime import datetime

from PySide6.QtGui import QColor
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

    status: str = "OFFLINE"
    last_event_time: datetime | None = None
    has_unack_critical: bool = False
    criticity: str = "gray"

    @property
    def criticity_color(self) -> QColor:
        """Return a QColor based on the criticity level."""
        colors = {
            "green" : QColor(0, 200, 0),
            "orange": QColor(255, 165, 0),
            "red"   : QColor(255, 0, 0),
            "gray"  : QColor(128, 128, 128),
        }
        return colors.get(self.criticity, QColor(128, 128, 128))

