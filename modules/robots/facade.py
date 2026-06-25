"""Domain service for managing the robot information."""
from abc import ABC, abstractmethod
from collections.abc import Callable

from PySide6.QtWidgets import QWidget
from sqlalchemy.orm import sessionmaker

import modules.events
from modules.robots.adapters import RobotStatusFromEventsAdapter
from modules.robots.ports import IRobotStatusService
from shared.di import ServiceHost

from .services import RobotListService, SelectionService
from .views import DetailView, FilterView, RobotListView


class IRobotsFacade(ABC):
    """Interface for the robots facade."""

    @abstractmethod
    def connect_robot_changed(self, callback: Callable[[str], None]) -> None:
        """Connect the selection changed signal to a callback."""

    @abstractmethod
    def new_list_view(self, parent: QWidget) -> QWidget:
        """Create a new robot list view."""

    @abstractmethod
    def new_detail_view(self, parent: QWidget) -> QWidget:
        """Create a new robot detail view."""

    @abstractmethod
    def new_filter_view(self, parent: QWidget) -> QWidget:
        """Create a new robot filter view."""

class RobotsFacade(IRobotsFacade):
    """Facade class for the robots module."""

    def __init__(self,
                 status_service: IRobotStatusService,
                 list_service: RobotListService,
                 selection_service: SelectionService) -> None:
        """Initialize the robots API."""
        self.list_service = list_service
        self.selection_service = selection_service
        self.status_service = status_service

    def connect_robot_changed(self, callback: Callable[[str], None]) -> None:
        """Connect the selection changed signal to a callback."""
        self.selection_service.selection_changed.connect(
            lambda r: callback(r.robot_id if r else None))

    def new_list_view(self, parent: QWidget) -> QWidget:
        """Create a new robot list view."""
        return RobotListView(self.list_service,
                             self.selection_service,
                             self.status_service, parent)

    def new_detail_view(self, parent: QWidget) -> QWidget:
        """Create a new robot detail view."""
        return DetailView(self.selection_service, self.status_service, parent)

    def new_filter_view(self, parent: QWidget) -> QWidget:
        """Create a new robot filter view."""
        return FilterView(parent)


def register_services(services: ServiceHost) -> None:
    """Register robots domain services."""
    services.register_singleton(RobotListService,
                                lambda s: RobotListService(
                                    s.resolve(sessionmaker)))
    services.register_singleton(SelectionService,
                                lambda _: SelectionService())
    services.register_singleton(IRobotStatusService,
                                lambda s: RobotStatusFromEventsAdapter(
                                    s.resolve(modules.events.IEventsFacade)))
    services.register_singleton(IRobotsFacade,
                                lambda s: RobotsFacade(
                                    s.resolve(IRobotStatusService),
                                    s.resolve(RobotListService),
                                    s.resolve(SelectionService)))
