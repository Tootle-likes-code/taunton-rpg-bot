from datetime import datetime

from ttrpg_bot.dates.holiday_date_service import HolidayDateService
from ttrpg_bot.exceptions.InvalidScheduleDateTimeException import InvalidScheduleDateTimeException


class SchedulingService:
    def __init__(self, holiday_date_service: HolidayDateService):
        self._holiday_date_service = holiday_date_service

    def schedule_session(self, date: datetime):
        if date < datetime.now():
            raise InvalidScheduleDateTimeException(date)
