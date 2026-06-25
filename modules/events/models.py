""""Data models for events."""
import datetime
from dataclasses import dataclass
from typing import Any

SEVERITIES = [ "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

@dataclass
class Event:
    """Event reported by a robot."""

    def __init__(self, pkid: int, robot_id: int, timestamp: datetime.datetime,
                 event_type: str, severity: str, message: str,
                 payload: dict[str, Any]) -> None:
        """Initialize a new BotEvent with default values."""
        self.id = pkid
        self.robot_id = robot_id
        self.timestamp = timestamp
        self.event_type = event_type
        self.severity = severity
        self.message = message
        self.payload = payload

