import unittest

from ttrpg_bot.group import Group
from ttrpg_bot.member import Member


class GroupTests(unittest.TestCase):
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

        self.previous_players = {
            Member(7, "Previous Player 1"),
            Member(8, "Previous Player 2")
        }

        self.previous_game_masters = {
            Member(9, "Previous Game Master 1"),
            Member(10, "Previous Game Master 2")
        }

        self.test_group = Group(
            name="Test Group",
            current_players=self.current_players,
            current_game_masters=self.current_game_masters,
            previous_players=self.previous_players,
            previous_game_masters=self.previous_game_masters
        )


class PlayersTests(GroupTests):
    def test_is_concatenated_set_of_current_players_and_game_masters(self):
        # Arrange
        expected_result = self.current_players.union(self.current_game_masters)

        # Act
        result = self.test_group.players

        # Assert
        self.assertSetEqual(expected_result, result)


class SizeTests(GroupTests):
    def test_is_concatenated_set_of_current_players_and_game_masters(self):
        # Arrange
        expected_result = len(self.current_game_masters) + len(self.current_players)

        # Act
        result = self.test_group.size

        # Assert
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
