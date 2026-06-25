"""Adapters for the robots module."""

from datetime import datetime

import modules.events

from .ports import IRobotStatusService


class RobotStatusFromEventsAdapter(IRobotStatusService):
    """Adapter class to provide robot status from events."""

    def __init__(self, events_facade: modules.events.IEventsFacade) -> None:
        """Initialize the adapter."""
        self.events_facade = events_facade

    def _get_status_info(self, robot_id: str) -> modules.events.StatusInfo:
        """Get the status info of a robot by its ID."""
        return self.events_facade.get_status(robot_id)

    def get_status(self, robot_id: str) -> str:
        """Get the status of a robot by its ID."""
        return self._get_status_info(robot_id).status

    def get_criticity(self, robot_id: str) -> str:
        """Get the criticity of a robot by its ID."""
        return self._get_status_info(robot_id).criticity

    def get_last_event_time(self, robot_id: str) -> datetime|None:
        """Get the last event time of a robot by its ID."""
        return self._get_status_info(robot_id).last_event_time
