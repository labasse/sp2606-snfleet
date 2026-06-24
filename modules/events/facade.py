"""Facade for event-related operations."""

import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass

from PySide6.QtWidgets import QWidget

from modules.events.services import EventFilterService
from shared.di import ServiceHost

from .views import EventsView


@dataclass
class StatusInfo:
    """Data class for robot status information."""

    status: str = "OFFLINE"
    last_event_time: datetime.datetime | None = None
    has_unack_critical: bool = False
    criticity: str = "gray"


class IEventsFacade(ABC):
    """Interface for the events facade."""

    @abstractmethod
    def get_status(self, robot_id: int) -> StatusInfo:
        """Get the status of the events facade."""

    @abstractmethod
    def filter_by_robot(self, robot_id: int) -> None:
        """Filter events based on criteria."""

    @abstractmethod
    def new_events_view(self, parent: QWidget) -> QWidget:
        """Create a new events view."""

class EventsFacade:
    """Facade for event-related operations."""

    def __init__(self, filter_service: EventFilterService) -> None:
        """Initialize the events facade."""
        self.filter_service = filter_service

    def filter_by_robot(self, robot_id: str) -> None:
        """Filter events based on the selected robot ID."""
        self.filter_service.set_robot_id(robot_id)

    def get_status(self, robot_id: str) -> StatusInfo:
        """Get the status of the events facade."""
        # Placeholder implementation; replace with actual logic
        return StatusInfo(
            status="ONLINE",
            last_event_time=datetime.datetime.now(datetime.UTC),
            has_unack_critical=False,
            criticity="green",
        ) if robot_id != "R005" else StatusInfo(
            status="OFFLINE",
            last_event_time=None,
            has_unack_critical=False,
            criticity="gray",
        )

    def new_events_view(self, parent: QWidget) -> QWidget:
        """Create a new events view."""
        return EventsView(self.filter_service, parent)


def register_services(services: ServiceHost) -> None:
    """Register event-related services."""
    services.register_singleton(EventFilterService,
                                lambda _: EventFilterService())
    services.register_singleton(IEventsFacade,
                                lambda s: EventsFacade(s.resolve(EventFilterService)))
