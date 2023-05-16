from dataclasses import dataclass, field
from datetime import datetime, timedelta

from ttrpg_bot.game import Game
from ttrpg_bot.location import Location


@dataclass
class Session:
    start_date_time: datetime
    end_date_time: datetime
    game: Game
    location: Location
    hard_finish_time: bool = field(default=False)

    @property
    def expected_duration(self) -> timedelta:
        return self.end_date_time - self.start_date_time
