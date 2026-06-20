"""Domain service for managing the robot information."""

import datetime
from datetime import timedelta

from PySide6.QtCore import QObject, Signal

from .models import Robot


class RobotListService:
    """Service to manage the list of robots."""

    def __init__(self) -> None:
        """Initialize with empty robot list."""
        self._robots: list[Robot] = []

    def get_robots(self) -> list[Robot]:
         """Return the list of robots."""
         return self._robots

    def dummy_data(self) -> None:
        """Populate the service with dummy data for testing."""
        now = datetime.datetime.now(datetime.UTC)
        self._robots = [
            Robot(
                robot_id=f"R{i:03}",
                display_name=f"Robot {i}",
                model="Model X",
                site_id=f"Site {i%3}",
                created_at=now - timedelta(days=i),
                status="Active" if i % 2 == 0 else "Inactive",
                last_event_time=now - timedelta(hours=i) if i % 2 == 0 else None,
                has_unack_critical=(i % 5 == 0),
                criticity="green" if i % 3 == 0 else "orange" if i % 3 == 1 else "red",
            )
            for i in range(10)
        ]

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
