"""Events module services."""

from PySide6.QtCore import QObject, Signal


class EventFilterService(QObject):
    """Service for managing event filtering."""

    filter_criteria_changed = Signal()

    def __init__(self) -> None:
        """Initialize the event filter service."""
        super().__init__()
        self._current_id = None

    def get_robot_id(self) -> str|None:
        """Get the current robot ID."""
        return self._current_id

    def set_robot_id(self, robot_id: str|None) -> None:
        """Set the current robot ID."""
        self._current_id = robot_id
        self.filter_criteria_changed.emit()
