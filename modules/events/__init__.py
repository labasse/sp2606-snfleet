""""Robot events module initialization."""
from .facade import IEventsFacade, StatusInfo, register_services

__all__ = ["IEventsFacade", "StatusInfo", "register_services"]
