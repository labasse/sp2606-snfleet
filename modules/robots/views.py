"""Robots module views."""
from typing import override

from PySide6.QtCore import QAbstractTableModel, QItemSelection, QModelIndex, Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget

import modules.events

from .models import Robot
from .services import RobotListService, SelectionService
from .ui.ui_DetailView import Ui_DetailView
from .ui.ui_FilterView import Ui_FilterView
from .ui.ui_RobotListView import Ui_RobotListView

HEADERS = ["ID", "Display Name", "Model", "Site",
           "Status", "Last Event", "Criticity"]
HEADER_ROBOT_ATTRIBUTES = ["robot_id", "display_name", "model", "site_id"]
HEADER_STATUS = 0
HEADER_STATUS_LAST_EVENT = 1
HEADER_STATUS_CRITICITY = 2

CRITICITY_COLORS = {
    "green" : QColor(0, 200, 0),
    "orange": QColor(255, 165, 0),
    "red"   : QColor(255, 0, 0),
    "gray"  : QColor(128, 128, 128),
}

class RobotsTableModel(QAbstractTableModel):
    """Table model for the fleet overview."""

    def __init__(self,
                 list_service: RobotListService,
                 events_facade: modules.events.IEventsFacade) -> None:
        """Initialize with empty robot list."""
        super().__init__()
        self.list_service = list_service
        self.events_facade = events_facade
        self._robots = self.list_service.get_robots()

    def refresh(self) -> None:
        """Replace the current robot list and refresh view."""
        self.beginResetModel()
        self._robots = self.list_service.get_robots()
        self.endResetModel()

    def get_id_at(self, index: QModelIndex) -> str | None:
        """Get robot ID for a given index."""
        return self._robots[index.row()].robot_id \
            if index.isValid() and 0 <= index.row() < len(self._robots) \
                else None

    @override
    def rowCount(self, parent: QModelIndex|None = None) -> int:
        """Get number of rows equals number of robots."""
        return len(self._robots)

    @override
    def columnCount(self, parent: QModelIndex|None = None) -> int:
        """Get number of columns is fixed by the Columns definition."""
        return len(HEADERS)

    @override
    def data(self, index: QModelIndex,
             role: Qt.ItemDataRole=Qt.ItemDataRole.DisplayRole) -> object:
        """Provide data for each cell based on the Robot object."""
        if not index.isValid() or index.row() >= len(self._robots):
            return None
        robot = self._robots[index.row()]
        col = index.column()
        if col < len(HEADER_ROBOT_ATTRIBUTES):
            return getattr(robot, HEADER_ROBOT_ATTRIBUTES[col]) \
                   if role == Qt.DisplayRole else None
        return self.get_status_data(robot, col - len(HEADER_ROBOT_ATTRIBUTES), role)

    def get_status_data(self, robot: Robot, col: int, role: Qt.ItemDataRole) -> object:
        """Provide status-related data for a given robot and column."""
        status = self.events_facade.get_status(robot.robot_id)
        if role == Qt.DisplayRole:
            if col == HEADER_STATUS:
                return status.status
            if col == HEADER_STATUS_LAST_EVENT:
                return status.last_event_time.isoformat() \
                    if status.last_event_time else None
            if col == HEADER_STATUS_CRITICITY:
                return status.criticity
        elif role == Qt.BackgroundRole and col == HEADER_STATUS_CRITICITY:
            return CRITICITY_COLORS.get(status.criticity, QColor(128, 128, 128))
        return None

    @override
    def headerData(self, section: int, orientation: Qt.Orientation,
                   role: int=Qt.DisplayRole) -> str | None:
        """Provide column headers based on the Columns definition."""
        return HEADERS[section] if orientation == Qt.Horizontal \
                                   and role == Qt.DisplayRole else None

    def get_robot(self, row: int) -> Robot | None:
        """Get the Robot object for a given row index."""
        return self._robots[row]


class FilterView(QWidget, Ui_FilterView):
    """A simple filter view class."""

    def __init__(self, parent: QWidget = None) -> None:
        """Initialize the filter view."""
        super().__init__(parent)
        self.setupUi(self)


class RobotListView(QWidget, Ui_RobotListView):
    """A simple robots list view class."""

    def __init__(self,
                 robot_list_service: RobotListService,
                 selection_service: SelectionService,
                 events_facade: modules.events.IEventsFacade,
                 parent: QWidget = None) -> None:
        """Initialize the robots list view."""
        super().__init__(parent)
        self.setupUi(self)
        self.selection_service = selection_service
        self.model = RobotsTableModel(robot_list_service, events_facade)
        self.tableView.setModel(self.model)
        self.tableView.selectionModel().selectionChanged.connect(
            self.on_selection_changed,
        )

    def on_selection_changed(self, selected: QItemSelection) -> None:
        """Handle selection changes in the table view."""
        selection = robot if (indexes := selected.indexes()) and (
            robot := self.tableView.model().get_robot(indexes[0].row())
        ) else None
        self.selection_service.set_selection(selection)

class DetailView(QWidget, Ui_DetailView):
    """A simple robot details view class."""

    def __init__(self,
                 selection_service: SelectionService,
                 events_facade: modules.events.IEventsFacade,
                 parent: QWidget = None) -> None:
        """Initialize the robot details view."""
        super().__init__(parent)
        self.setupUi(self)
        self.selection_service = selection_service
        self.events_facade = events_facade
        self.selection_service.selection_changed.connect(self.update_details)

    def update_details(self, robot: Robot | None) -> None:
        """Update the details view based on the selected robot."""
        if robot is None:
            self.robotIDLabel.setText("No robot selected")
            self.displayNameLabel.setText("")
            self.modelLabel.setText("")
            self.siteIDLabel.setText("")
            self.statusLabel.setText("")
            self.lastEventTimeLabel.setText("")
        else:
            self.robotIDLabel.setText(robot.robot_id)
            self.displayNameLabel.setText(robot.display_name)
            self.modelLabel.setText(robot.model)
            self.siteIDLabel.setText(robot.site_id)
            status = self.events_facade.get_status(robot.robot_id)
            self.statusLabel.setText(status.status)
            self.lastEventTimeLabel.setText(
                status.last_event_time.isoformat() if status.last_event_time
                else "Never",
            )
