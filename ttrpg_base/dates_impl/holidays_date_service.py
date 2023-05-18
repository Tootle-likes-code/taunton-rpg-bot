from datetime import datetime

import holidays
from holidays import HolidayBase

from ttrpg_base.dates.bank_holiday import BankHoliday
from ttrpg_base.dates.holiday_date_service import HolidayDateService


class HolidaysHolidayDateService(HolidayDateService):

    def __init__(self, country: str = "GB", province: str | None = None):
        self._bank_holidays: list[BankHoliday] = []
        self._initialise(country, province)

    def _initialise(self, country: str, province: str | None):
        current_year: int = datetime.today().year
        if province:
            country_holidays: HolidayBase = holidays.country_holidays(country, years=current_year, subdiv=province)
        else:
            country_holidays: HolidayBase = holidays.country_holidays(country, years=current_year)

        self._convert(country_holidays)

    def _convert(self, country_holidays: HolidayBase):
        for date in country_holidays:
            name = country_holidays.get(date)
            bank_holiday = BankHoliday(date, name)
            self._bank_holidays.append(bank_holiday)

    def get_holidays(self) -> list[BankHoliday]:
        return self._bank_holidays
