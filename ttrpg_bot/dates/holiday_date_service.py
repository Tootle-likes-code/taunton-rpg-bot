from abc import ABC, abstractmethod

from ttrpg_bot.dates.bank_holiday import BankHoliday


class HolidayDateService(ABC):
    @abstractmethod
    def get_holidays(self) -> list[BankHoliday]:
        pass
