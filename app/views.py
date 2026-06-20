"""Main window module."""

from PySide6.QtWidgets import QMainWindow, QWidget

from app.ui.ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """A simple main window class."""

    def __init__(self, parent: QWidget = None) -> None:
        """Initialize the main window."""
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("SN Fleet")
