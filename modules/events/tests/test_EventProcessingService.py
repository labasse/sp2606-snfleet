"""Test cases for EventProcessingService."""
import unittest
from unittest.mock import patch

from modules.events.services import IEventRepository, EventsProcessingService


class TestEventProcessingService(unittest.TestCase):
    """Test cases for EventProcessingService."""

    # Test case for init
    def test_init_with_invalid_event_list_service_raises_error(self):
        pass

    # Test cases for get_status method
    def test_status_with_regular_heartbeat_returns_online(self):
        pass

    def test_status_with_start_task_returns_mission(self):
        pass

    # ... ans so on ...

    @patch("modules.events.services.IEventRepository")
    def test_motor_temps_with_multiple_events_returns_average(
        self,
        event_list: IEventRepository) -> None:

        event_list.get_events_by_robot_id.return_value = [
            # Event with payload
            type("Event", (), {"payload": {"motor1": 50, "motor2": 60}})(),
            # Event with payload
            type("Event", (), {"payload": {"motor1": 70, "motor2": 80}})(),
        ]
        test = EventsProcessingService(event_list)

        result = test.get_motor_temps("robot1")

        self.assertEqual(result, {"motor1": 60.0, "motor2": 70.0})
        # Assert on getters for mutators

    # Extreme case
    def test_motor_temps_with_no_payload_event_returns_emptydict(self):
        pass

    # Error case
    def test_motor_temps_with_invalid_robot_id_raise_error(self):
        pass

