from dataclasses import dataclass, field

from ttrpg_base.model.group import Group


@dataclass
class Game:
    name: str
    group: Group
    max_spaces: int
    continuing: bool = field(default=False)

    @property
    def spaces_available(self) -> int:
        return self.max_spaces - len(self.group.current_players)

    @property
    def are_spaces_available(self) -> bool:
        return self.spaces_available > 0
