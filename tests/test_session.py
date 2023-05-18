import unittest
from datetime import datetime, timedelta
from unittest.mock import MagicMock

from ttrpg_model.location import Location
from ttrpg_model.session import Session


class SessionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.location = Location()

        self.mock_game = MagicMock()

        self.test_session = Session(
            datetime(2023, 5, 16, 19),
            datetime(2023, 5, 16, 22),
            self.mock_game,
            self.location
        )


class ExpectedDurationTests(SessionTests):
    def test_returns_correct_time_difference(self):
        # Arrange
        expected_result = timedelta(seconds=10_800)

        # Act
        result = self.test_session.expected_duration

        # Assert
        self.assertEqual(expected_result, result)
