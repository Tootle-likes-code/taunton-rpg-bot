import datetime
import unittest
from unittest.mock import MagicMock

from ttrpg_base.application.dates.scheduling_service import SchedulingService
from ttrpg_base.infrastructure.exceptions.InvalidScheduleDateTimeException import InvalidScheduleDateTimeException


class SchedulingTestService(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_holiday_service = MagicMock()
        self.test_service = SchedulingService(self.mock_holiday_service)


class ScheduleSessionTests(SchedulingTestService):
    def test_cannot_schedule_session_in_past(self):
        # Assert
        with self.assertRaises(InvalidScheduleDateTimeException):
            # Act
            self.test_service.schedule_session(datetime.datetime.min)


if __name__ == '__main__':
    unittest.main()
