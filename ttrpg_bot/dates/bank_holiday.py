from dataclasses import dataclass
from datetime import datetime


@dataclass
class BankHoliday:
    date: datetime
    name: str
