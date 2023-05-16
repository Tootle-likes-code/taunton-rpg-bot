from dataclasses import dataclass, field
from datetime import datetime, timedelta

from ttrpg_bot.game import Game
from ttrpg_bot.location import Location
from ttrpg_bot.session_attendance import SessionAttendance


@dataclass
class Session:
    start_date_time: datetime
    end_date_time: datetime
    game: Game
    location: Location
    hard_finish_time: bool = field(default=False)
    session_attendance: SessionAttendance = field(default=None)

    def __post_init__(self):
        if not self.session_attendance:
            self.session_attendance = SessionAttendance(self.game.group, self)

    @property
    def expected_duration(self) -> timedelta:
        return self.end_date_time - self.start_date_time
