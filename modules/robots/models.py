"""Data models for Qt views."""

from dataclasses import dataclass
from datetime import datetime

from PySide6.QtGui import QColor


@dataclass
class Robot:
    """Represents a robot with computed status and criticity."""

    robot_id: str
    display_name: str
    model: str
    site_id: str
    created_at: datetime
    status: str
    last_event_time: datetime | None
    has_unack_critical: bool
    criticity: str  # green, orange, red, gray

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

