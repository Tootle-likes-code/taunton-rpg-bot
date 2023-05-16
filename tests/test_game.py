import unittest
from unittest.mock import MagicMock, PropertyMock

from ttrpg_bot.game import Game
from ttrpg_bot.member import Member


class GameTests(unittest.TestCase):
    def setUp(self) -> None:
        self.current_players = {
            Member(1, "Test Player 1"),
            Member(2, "Test Player 2"),
            Member(3, "Test Player 3"),
            Member(4, "Test Player 4")
        }

        self.current_game_masters = {
            Member(5, "Test Game Master 1"),
            Member(6, "Test Game Master 2")
        }

        self.mock_group = MagicMock()
        self.mock_group.current_players = self.current_players
        self.mock_group.current_game_masters = self.current_game_masters
        self.mock_group.size = PropertyMock(return_value=6)

        self.test_game = Game("Test Game", self.mock_group, 6)


class SpacesAvailableTests(GameTests):
    def test_returns_difference_between_group_size_and_max_spaces(self):
        # Arrange
        expected_result = 2
        
        # Act
        result = self.test_game.spaces_available
        
        # Assert
        self.assertEquals(expected_result, result)


class AreSpacesAvailableTests(GameTests):
    def test_returns_true_when_available_spaces_greater_than_zero(self):
        # Act
        result = self.test_game.are_spaces_available

        # Assert
        self.assertTrue(result)

    def test_returns_false_when_available_spaces_zero(self):
        # Arrange
        self.test_game.max_spaces = 4

        # Act
        result = self.test_game.are_spaces_available

        # Assert
        self.assertIsNotNone(result)
        self.assertFalse(result)

    def test_returns_false_when_available_spaces_is_negative(self):
        # Arrange
        self.test_game.max_spaces = 3

        # Act
        result = self.test_game.are_spaces_available

        # Assert
        self.assertIsNotNone(result)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
