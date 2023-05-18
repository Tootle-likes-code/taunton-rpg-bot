from datetime import datetime

from ttrpg_bot.exceptions.ttrpg_bot_exception import TtrpgBotException


class InvalidScheduleDateTimeException(TtrpgBotException):
    def __init__(self, date_time: datetime):
        self.date_time: datetime = date_time

    def __str__(self):
        return f"Cannot schedule a session in the past.  " \
               f"Tried to schedule a session for {self.date_time.isoformat()}."
