""""Data models for events."""

import datetime
import random
from collections.abc import Generator

from alembic.environment import Any, Optional
from sqlalchemy import JSON, DateTime, Index, Integer, String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedAsDataclass,
    mapped_column,
    sessionmaker,
)

from .models import SEVERITIES, Event
from .ports import IEventRepository


class Base(DeclarativeBase, MappedAsDataclass):
    """Base class for SQLAlchemy models with dataclass support."""

class EventORM(Base):
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

class SqlAlchemyEventRepository(IEventRepository):
    """Repository for managing events in the database."""

    def __init__(self, session_factory: sessionmaker) -> None:
        """Initialize the repository with a database session."""
        self._session_factory = session_factory

    def get_events_by_robot_id(self, robot_id: str) -> Generator[Event]:
        """Retrieve events for a specific robot."""
        with self._session_factory() as session:
            for event_orm in session.query(EventORM).filter_by(robot_id=robot_id).all():
                yield Event(
                    pkid        =event_orm.id,
                    robot_id    =event_orm.robot_id,
                    timestamp   =event_orm.timestamp,
                    event_type  =event_orm.event_type,
                    severity    =event_orm.severity,
                    message     =event_orm.message,
                    payload     =event_orm.payload,
                )


EVENT_TYPES = [
    "HEARTBEAT", "STATE_CHANGE", "SENSOR_ALERT", "TASK_START", "TASK_COMPLETE",
    "FAULT", "MAINTENANCE_START", "MAINTENANCE_END", "ALERT_TRIGGERED",
]
MOTOR_COMBOS = [
    ["neck_pitch", "shoulder_left", "shoulder_right",
     "elbow_left", "elbow_right", "torso_yaw"],
    ["hip_left", "hip_right", "knee_left", "knee_right",
     "ankle_left", "ankle_right", "arm_left", "arm_right"],
    ["shoulder_left", "shoulder_right", "knee_left", "knee_right"],
]
class MemoryEventRepository(IEventRepository):
    """Repository for managing events in memory."""

    def __init__(self) -> None:
        """Initialize the memory event repository."""
        super().__init__()
        self._data = {}

    def get_events_by_robot_id(self, robot_id: str) -> Generator[Event]:
        """Get events for a specific robot."""
        if robot_id not in self._data:
            self._data[robot_id] = self._generate_dummy_events(robot_id)
        yield from self._data[robot_id]

    def _generate_dummy_events(self, robot_id: str) -> list[Event]:
        """Generate dummy events for a specific robot."""
        seed = hash(robot_id)
        now = datetime.datetime.now(datetime.UTC)
        motor_list = MOTOR_COMBOS[seed % len(MOTOR_COMBOS)]
        return [Event(
            pkid = i,
            robot_id = robot_id,
            timestamp = now + datetime.timedelta(minutes=i),
            event_type = random.choice(EVENT_TYPES),
            severity = random.choice(SEVERITIES),
            message = f"Robot automatic report (sequence {i})",
            payload = {m: round(random.uniform(25,65), 1) for m in motor_list},
            ) for i in range(10)]

