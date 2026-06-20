"""Main entry point for the application."""

import sys

from PySide6.QtWidgets import QApplication

from app.views import MainWindow


def main() -> None:
    """Run the main application."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
