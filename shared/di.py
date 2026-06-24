"""Dependency Injection utilities for managing service instances."""
from abc import ABC, abstractmethod
from collections.abc import Callable


class IServiceResolver(ABC):
    """Interface providing service resolution capabilities."""

    @abstractmethod
    def resolve[T](self, interface: type[T]) -> T:
        """Resolve an instance of the given interface."""

class ServiceHost(IServiceResolver):
    """A simple dependency injection container for managing service instances."""

    def __init__(self) -> None:
        """Initialize the service host with empty registries."""
        self._factories: dict[type, Callable] = {}
        self._singletons: dict[type, object] = {}

    def register_transient[T](self, interface: type[T],
                              factory: Callable[[IServiceResolver], T]) -> None:
        """Register a transient service factory for a given interface."""
        self._factories[interface] = factory

    def register_singleton[T](self, interface: type[T],
                              factory: Callable[[IServiceResolver], T]) -> None:
        """Register a singleton service factory for a given interface."""
        self.register_transient(interface, factory)
        self._singletons[interface] = None

    def resolve[T](self, interface: type[T]) -> T:
        """Resolve an instance of the given interface."""
        is_singleton = interface in self._singletons
        if is_singleton and self._singletons[interface] is not None:
            return self._singletons[interface]
        factory = self._factories[interface]
        instance = factory(self)
        if is_singleton:
            self._singletons[interface] = instance
        return instance
