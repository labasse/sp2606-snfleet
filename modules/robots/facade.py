"""Facade class for the robots module."""
from PySide6.QtWidgets import QMainWindow

from modules.robots.services import RobotListService, SelectionService


class RobotsFacade:
    """Facade class for the robots module."""

    def __init__(self, main_window: QMainWindow) -> None:
        """Initialize the facade with a robot list service."""
        self.list_service = RobotListService()
        self.list_service.dummy_data()  # Populate with dummy data for testing
        self.selection_service = SelectionService()

        main_window.robot_list_service = self.list_service
        main_window.robot_selection_service = self.selection_service
