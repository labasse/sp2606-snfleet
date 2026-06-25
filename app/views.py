"""Main window module."""

from PySide6.QtWidgets import QMainWindow, QStackedLayout, QWidget

import modules.events
import modules.robots
from app.ui.ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """A simple main window class."""

    def __init__(self,
                 robots_facade: modules.robots.IRobotsFacade,
                 events_facade: modules.events.IEventsFacade,
                 parent: QWidget = None) -> None:
        """Initialize the main window."""
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowTitle("SN Fleet")

        robots_facade.connect_robot_changed(events_facade.filter_by_robot)

        self._place(self.robotListView, robots_facade.new_list_view  (self))
        self._place(self.detailView   , robots_facade.new_detail_view(self))
        self._place(self.filterView   , robots_facade.new_filter_view(self))

        self._place(self.eventView    , events_facade.new_events_view(self))
        self._place(self.eventsMapView, events_facade.new_botmap_view(self))

    def _place(self, stack: QStackedLayout, view: QWidget) -> None:
        """Place a view in a stacked layout."""
        stack.setCurrentIndex(stack.addWidget(view))
