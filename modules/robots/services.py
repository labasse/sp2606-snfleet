"""Domain service for managing the robot information."""

import datetime
import random
from datetime import timedelta

from PySide6.QtCore import QObject, Signal
from sqlalchemy.orm import Session, sessionmaker

from .models import Robot

SITES = ["Logistics_North", "Assembly_South", "R&D_Lab"]
MODELS = ["Atlas-G2", "Helix-Pro", "Sentry-X1" ]
STATUS = ["IDLE", "ON_MISSION", "UNDER_MAINTENANCE", "FAULTY", "OFFLINE"]

class RobotListService:
    """Service to manage the list of robots."""

    def __init__(self, session_factory: sessionmaker) -> None:
        """Initialize with empty robot list."""
        self.session_factory = session_factory

    def get_robots(self) -> list[Robot]:
         """Return the list of robots."""
         with self.session_factory() as session:
            if not session.query(Robot).first():
                self._dummy_data(session)
            return session.query(Robot).all()

    def _dummy_data(self, session: Session) -> None:
        """Populate the service with dummy data for testing."""
        now = datetime.datetime.now(datetime.UTC)
        robots = [
            Robot(
                robot_id=f"R{i:03}",
                display_name=f"{model} #{i}",
                model=model,
                site_id=random.choice(SITES),
                created_at=now - timedelta(days=i),
                status=STATUS[n if (n:=random.randint(0, 15)) < len(STATUS) else 0],
                last_event_time=now - timedelta(hours=i) if i % 2 == 0 else None,
                has_unack_critical=(i % 5 == 0),
                criticity="green" if i % 3 == 0 else "orange" if i % 3 == 1 else "red",
            )
            for i, model in [(i, random.choice(MODELS)) for i in range(10)]
        ]
        session.add_all(robots)
        session.commit()

class SelectionService(QObject):
    """Service to manage the selection of a robot."""

    selection_changed = Signal(Robot)

    def __init__(self) -> None:
        """Initialize with no selected robot."""
        super().__init__()
        self._selected_robot: Robot | None = None

    def get_selection(self) -> Robot | None:
        """Return the currently selected robot."""
        return self._selected_robot

    def set_selection(self, robot: Robot | None) -> None:
        """Set the selected robot and emit a signal if it changes."""
        if self._selected_robot != robot:
            self._selected_robot = robot
            self.selection_changed.emit(robot)
