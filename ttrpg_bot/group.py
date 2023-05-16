from dataclasses import dataclass, field

from ttrpg_bot.member import Member


@dataclass
class Group:
    name: str
    current_players: set[Member]
    current_game_masters: set[Member]
    previous_players: set[Member] = field(default_factory=set)
    previous_game_masters: set[Member] = field(default_factory=set)

    @property
    def players(self):
        return self.current_players.union(self.current_game_masters)

    @property
    def size(self):
        return len(self.players)
