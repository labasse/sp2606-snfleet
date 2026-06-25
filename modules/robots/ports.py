"""Ports for robot domain."""
from abc import ABC, abstractmethod
from datetime import datetime


class IRobotStatusService(ABC):
    """Interface for a robot status service."""

    @abstractmethod
    def get_status(self, robot_id: str) -> str:
        """Get the status of a robot by its ID."""

    @abstractmethod
    def get_criticity(self, robot_id: str) -> str:
        """Get the criticity of a robot by its ID."""

    @abstractmethod
    def get_last_event_time(self, robot_id: str) -> datetime|None:
        """Get the last event time of a robot by its ID."""
