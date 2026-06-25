"""Facade for event-related operations."""

import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass

from PySide6.QtWidgets import QWidget

from shared.di import ServiceHost

from .adapters import MemoryEventRepository
from .ports import IEventRepository
from .services import (
    EventFilterService,
    EventsProcessingService,
)
from .views import EventsView, RobotMapView


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

    def __init__(self,
                 filter_service: EventFilterService,
                 processing_service: EventsProcessingService) -> None:
        """Initialize the events facade."""
        self.filter_service = filter_service
        self.processing_service = processing_service

    def filter_by_robot(self, robot_id: str) -> None:
        """Filter events based on the selected robot ID."""
        self.filter_service.set_robot_id(robot_id)

    def get_status(self, robot_id: str) -> StatusInfo:
        """Get the status of the events facade !!! SHOULD BE IN THE BUSINESS LOGIC."""
        info = self.processing_service.get_status(robot_id)
        return StatusInfo(
            status=info[0],
            last_event_time=info[1],
            has_unack_critical=False,
            criticity=info[2],
        )

    def new_events_view(self, parent: QWidget) -> QWidget:
        """Create a new events view."""
        return EventsView(self.filter_service, parent)

    def new_botmap_view(self, parent: QWidget) -> QWidget:
        """Create a new robot map widget."""
        return RobotMapView(self.filter_service, self.processing_service, parent)

def register_services(services: ServiceHost) -> None:
    """Register event-related services."""
    services.register_singleton(IEventRepository,
                                lambda _: MemoryEventRepository())
    services.register_singleton(EventFilterService,
                                lambda s: EventFilterService(
                                    s.resolve(IEventRepository)))
    services.register_singleton(EventsProcessingService,
                                lambda s: EventsProcessingService(
                                    s.resolve(IEventRepository),
                                ))
    services.register_singleton(IEventsFacade,
                                lambda s: EventsFacade(
                                    s.resolve(EventFilterService),
                                    s.resolve(EventsProcessingService),
                                ))
