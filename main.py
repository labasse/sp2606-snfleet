"""Main entry point for the application."""

import os
import sys

from PySide6.QtWidgets import QApplication
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import modules.events
import modules.robots
from app.views import MainWindow
from shared.di import ServiceHost


def build_sessionmaker(_: ServiceHost) -> sessionmaker:
    """Build a SQLAlchemy sessionmaker."""
    url = os.getenv("ROBOTS_DB_URL", "sqlite:///")
    return sessionmaker(create_engine(url, echo=False))

def main() -> None:
    """Run the main application."""
    services = ServiceHost()
    services.register_singleton(sessionmaker, build_sessionmaker)
    modules.robots.register_services(services)
    modules.events.register_services(services)

    app = QApplication(sys.argv)
    window = MainWindow(
        services.resolve(modules.robots.IRobotsFacade),
        services.resolve(modules.events.IEventsFacade),
    )
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
