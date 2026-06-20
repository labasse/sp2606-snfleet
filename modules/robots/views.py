"""Robots module views."""
from PySide6.QtWidgets import QWidget

from .ui.ui_DetailView import Ui_DetailView
from .ui.ui_FilterView import Ui_FilterView
from .ui.ui_RobotListView import Ui_RobotListView


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

class DetailView(QWidget, Ui_DetailView):
    """A simple robot details view class."""

    def __init__(self, parent: QWidget = None) -> None:
        """Initialize the robot details view."""
        super().__init__(parent)
        self.setupUi(self)
