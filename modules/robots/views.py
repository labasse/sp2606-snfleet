"""Robots module views."""
from collections.abc import Sequence
from typing import override

from PySide6.QtCore import QAbstractTableModel, QItemSelection, QModelIndex, Qt, Slot
from PySide6.QtGui import QShowEvent
from PySide6.QtWidgets import QWidget

from .models import Robot
from .services import RobotListService, SelectionService
from .ui.ui_DetailView import Ui_DetailView
from .ui.ui_FilterView import Ui_FilterView
from .ui.ui_RobotListView import Ui_RobotListView

FIELD_INDEX_ROBOT_ID = 0
FIELD_INDEX_DISPLAY_NAME = 1
FIELD_INDEX_MODEL = 2
FIELD_INDEX_SITE_ID = 3
FIELD_INDEX_STATUS = 4
FIELD_INDEX_LAST_EVENT_TIME = 5
FIELD_INDEX_CRITICITY = 6

class RobotsTableModel(QAbstractTableModel):
    """Table model for the fleet overview."""

    Columns : Sequence[str] = ["ID", "Display Name", "Model", "Site",
                               "Status", "Last Event", "Criticity"]

    def __init__(self, list_service: RobotListService) -> None:
        """Initialize with empty robot list."""
        super().__init__()
        self._robots: list[Robot] = list_service.get_robots()

    def update_robots(self, robots: list[Robot]) -> None:
        """Replace the current robot list and refresh view."""
        self.beginResetModel()
        self._robots = robots
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
        return len(self.Columns)

    @override
    def data(self, index: QModelIndex,
             role: Qt.ItemDataRole=Qt.ItemDataRole.DisplayRole) -> object:
        """Provide data for each cell based on the Robot object."""
        if not index.isValid() or index.row() >= len(self._robots):
            return None
        robot = self._robots[index.row()]
        col = index.column()
        if role == Qt.BackgroundRole and col == FIELD_INDEX_CRITICITY:
            return robot.criticity_color
        if role != Qt.DisplayRole:
            return None
        if(col == FIELD_INDEX_ROBOT_ID):
            return robot.robot_id
        if(col == FIELD_INDEX_DISPLAY_NAME):
            return robot.display_name
        if(col == FIELD_INDEX_MODEL):
            return robot.model
        if(col == FIELD_INDEX_SITE_ID):
            return robot.site_id
        if(col == FIELD_INDEX_STATUS):
            return robot.status
        if(col == FIELD_INDEX_LAST_EVENT_TIME):
            return robot.last_event_time.isoformat() if robot.last_event_time \
                else "Never"
        if(col == FIELD_INDEX_CRITICITY):
            return robot.criticity
        return None

    @override
    def headerData(self, section: int, orientation: Qt.Orientation,
                   role: int=Qt.DisplayRole) -> str | None:
        """Provide column headers based on the Columns definition."""
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.Columns[section]
        return None

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

    def __init__(self, parent: QWidget = None) -> None:
        """Initialize the robots list view."""
        super().__init__(parent)
        self.setupUi(self)
        self.model = RobotsTableModel(self.window().robot_list_service)
        self.tableView.setModel(self.model)
        self.tableView.selectionModel().selectionChanged.connect(
            self.on_selection_changed,
        )

    def on_selection_changed(self, selected: QItemSelection) -> None:
        """Handle selection changes in the table view."""
        selection = robot if (indexes := selected.indexes()) and (
            robot := self.tableView.model().get_robot(indexes[0].row())
        ) else None
        self.window().robot_selection_service.set_selection(selection)

class DetailView(QWidget, Ui_DetailView):
    """A simple robot details view class."""

    selection_service: SelectionService = None

    def __init__(self, parent: QWidget = None) -> None:
        """Initialize the robot details view."""
        super().__init__(parent)
        self.setupUi(self)

    @override
    def showEvent(self, event: QShowEvent) -> None:
        """Connect to selection service when the view is shown."""
        super().showEvent(event)
        if self.selection_service is None:
            self.selection_service = self.window().robot_selection_service
            self.selection_service.selection_changed.connect(self.update_details)

    @Slot(Robot)
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
            self.statusLabel.setText(robot.status)
            self.lastEventTimeLabel.setText(
                robot.last_event_time.isoformat() if robot.last_event_time else "Never",
            )