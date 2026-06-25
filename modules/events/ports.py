"""Ports module for events."""
from abc import ABC, abstractmethod

from .models import Event


class IEventRepository(ABC):
    """Abstract base class for event repository ports."""

    @abstractmethod
    def get_events_by_robot_id(self, robot_id: str) -> list[Event]:
        """Retrieve events for a specific robot."""
