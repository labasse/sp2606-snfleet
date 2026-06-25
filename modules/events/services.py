"""Events module services."""

import datetime

from PySide6.QtCore import QObject, Signal

from modules.events.ports import IEventRepository

from .models import SEVERITIES, Event


class EventFilterService(QObject):
    """Service for managing event filtering."""

    filter_criteria_changed = Signal()

    def __init__(self, event_list_service: IEventRepository) -> None:
        """Initialize the event filter service."""
        super().__init__()
        self._cur_id = None
        self._event_list_service = event_list_service

    def get_robot_id(self) -> str|None:
        """Get the current robot ID."""
        return self._cur_id

    def set_robot_id(self, robot_id: str|None) -> None:
        """Set the current robot ID."""
        self._cur_id = robot_id
        self.filter_criteria_changed.emit()

    def get_filtered_events(self) -> list[Event]:
        """Get events filtered by the current robot ID."""
        return [] if self._cur_id is None else \
            self._event_list_service.get_events_by_robot_id(self._cur_id)

class EventsProcessingService:
    """Service for processing robot temperature data."""

    def __init__(self, event_list_service: IEventRepository) -> None:
        """Initialize the bot temperature processing service."""
        super().__init__()
        self._event_list_service = event_list_service

    def get_motor_temps(self, robot_id: str) -> dict[str, float]:
        """Get the average motor temperatures for a specific robot."""
        events = self._event_list_service.get_events_by_robot_id(robot_id)
        res = {}
        count = 0
        for event in events:
            if event.payload:
                for motor, temp in event.payload.items():
                    if motor not in res:
                        res[motor] = 0
                    res[motor]+= temp
            count += 1
        return {motor: round(temp/count, 1) for motor, temp in res.items()}

    def get_status(self, robot_id: str) -> tuple[str, datetime.datetime|None, str]:
        """Get the status of a specific robot."""
        events = self._event_list_service.get_events_by_robot_id(robot_id)
        last_event = max(events, key=lambda e: e.timestamp) if events else None
        severity_level = SEVERITIES.index(last_event.severity) if last_event else -1
        return (
            "ONLINE" if last_event else "OFFLINE",
            last_event.timestamp if last_event else None,
            "gray" if severity_level < 0 else (
                "green" if severity_level < 2 else (
                    "orange" if severity_level < 3 else "red")))
