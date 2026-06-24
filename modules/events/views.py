"""Robots module views."""

from PySide6.QtWidgets import QWidget

from modules.events.services import EventFilterService

from .ui.ui_EventsView import Ui_EventsView


class EventsView(QWidget, Ui_EventsView):
    """Event list view class."""

    def __init__(self, filter_service: EventFilterService, parent: QWidget) -> None:
        """Initialize the event list view."""
        super().__init__(parent)
        self.setupUi(self)
        self.filter_service = filter_service
        self.filter_service.filter_criteria_changed.connect(self.on_robot_changed)

    def on_robot_changed(self) -> None:
        """Handle robot selection changes."""
        robot_id = self.filter_service.get_robot_id()
        self.robotIDLabel.setText(f"Selected Robot ID: {robot_id}")
