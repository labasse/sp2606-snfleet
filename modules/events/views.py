"""Robots module views."""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTreeWidgetItem, QVBoxLayout, QWidget

from modules.events.services import EventFilterService, EventsProcessingService
from modules.events.widgets import BotMapWidget

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
        self.eventsTree.clear()
        for event in self.filter_service.get_filtered_events():
            item = QTreeWidgetItem(self.eventsTree)
            item.setText(0, event.timestamp.strftime("%Y-%m-%d %H:%M:%S"))
            item.setText(1, event.event_type)
            item.setText(2, event.severity)
            item.setText(3, event.message)
            item.setText(4, "no")
            item.setData(0, Qt.UserRole, event.id)


class RobotMapView(QWidget):
    """Robot map view class."""

    def __init__(self,
                 filter_service: EventFilterService,
                 process_service: EventsProcessingService,
                 parent: QWidget) -> None:
        """Initialize the robot map view."""
        super().__init__(parent)
        self.map_widget = BotMapWidget(parent)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.map_widget)
        self.filter_service = filter_service
        self.process_service = process_service
        filter_service.filter_criteria_changed.connect(self.on_robot_changed)

    def on_robot_changed(self) -> None:
        """Handle robot selection changes."""
        self.map_widget.set_temps(
            self.process_service.get_motor_temps(
                self.filter_service.get_robot_id()))
