import unittest
from datetime import date
from unittest.mock import patch

from ttrpg_base.dates.bank_holiday import BankHoliday
from ttrpg_base.dates_impl.holidays_date_service import HolidaysHolidayDateService

UK_BANK_HOLS_2023 = {
    date(2023, 5, 8): 'Coronation of Charles III',
    date(2023, 1, 1): "New Year's Day",
    date(2023, 1, 2): "New Year Holiday [Scotland]; New Year's Day (Observed)",
    date(2023, 1, 3): 'New Year Holiday [Scotland] (Observed)',
    date(2023, 3, 17): "St. Patrick's Day [Northern Ireland]",
    date(2023, 7, 12): 'Battle of the Boyne [Northern Ireland]',
    date(2023, 8, 7): 'Summer Bank Holiday [Scotland]',
    date(2023, 11, 30): "St. Andrew's Day [Scotland]",
    date(2023, 12, 25): 'Christmas Day',
    date(2023, 4, 7): 'Good Friday',
    date(2023, 4, 10): 'Easter Monday [England/Wales/Northern Ireland]',
    date(2023, 5, 1): 'May Day',
    date(2023, 5, 29): 'Spring Bank Holiday',
    date(2023, 8, 28): 'Late Summer Bank Holiday [England/Wales/Northern Ireland]',
    date(2023, 12, 26): 'Boxing Day'
}


class HolidaysDateServiceTests(unittest.TestCase):
    pass


@patch("ttrpg_base.dates_impl.holidays_date_service.holidays.country_holidays")
class ConstructorTests(HolidaysDateServiceTests):
    def test_without_province_holidays_called(self, patched_country_holidays):
        # Act
        HolidaysHolidayDateService("GB")

        # Assert
        patched_country_holidays.assert_called_once()

    def test_without_province_holidays_args_are_as_expected(self, patched_country_holidays):
        # Act
        HolidaysHolidayDateService("GB")

        # Assert
        patched_country_holidays.assert_called_with("GB", years=2023)

    def test_with_province_holidays_called(self, patched_country_holidays):
        # Act
        HolidaysHolidayDateService("GB", "England")

        # Assert
        patched_country_holidays.assert_called_once()

    def test_with_province_holidays_args_are_as_expected(self, patched_country_holidays):
        # Act
        HolidaysHolidayDateService("GB", "England")

        # Assert
        patched_country_holidays.assert_called_with("GB", subdiv="England", years=2023)


@patch("ttrpg_base.dates_impl.holidays_date_service.holidays.country_holidays", return_value=UK_BANK_HOLS_2023)
class GetHolidaysTests(HolidaysDateServiceTests):
    def setUp(self) -> None:
        self.expected_result = [
            BankHoliday(date=date(2023, 5, 8), name='Coronation of Charles III'),
            BankHoliday(date=date(2023, 1, 1), name="New Year's Day"),
            BankHoliday(date=date(2023, 1, 2),
                        name="New Year Holiday [Scotland]; New Year's Day (Observed)"),
            BankHoliday(date=date(2023, 1, 3),
                        name='New Year Holiday [Scotland] (Observed)'),
            BankHoliday(date=date(2023, 3, 17),
                        name="St. Patrick's Day [Northern Ireland]"),
            BankHoliday(date=date(2023, 7, 12),
                        name='Battle of the Boyne [Northern Ireland]'),
            BankHoliday(date=date(2023, 8, 7),
                        name='Summer Bank Holiday [Scotland]'),
            BankHoliday(date=date(2023, 11, 30),
                        name="St. Andrew's Day [Scotland]"),
            BankHoliday(date=date(2023, 12, 25), name='Christmas Day'),
            BankHoliday(date=date(2023, 4, 7), name='Good Friday'),
            BankHoliday(date=date(2023, 4, 10),
                        name='Easter Monday [England/Wales/Northern Ireland]'),
            BankHoliday(date=date(2023, 5, 1), name='May Day'),
            BankHoliday(date=date(2023, 5, 29), name='Spring Bank Holiday'),
            BankHoliday(date=date(2023, 8, 28),
                        name='Late Summer Bank Holiday [England/Wales/Northern Ireland]'),
            BankHoliday(date=date(2023, 12, 26), name='Boxing Day')
        ]
        self.test_service = HolidaysHolidayDateService("GB")

    def test_returns_mapped_bank_holidays(self, _):
        # Act
        result = self.test_service.get_holidays()

        # Assert
        self.assertEqual(self.expected_result, result)


if __name__ == '__main__':
    unittest.main()
