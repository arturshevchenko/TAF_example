from datetime import datetime, timedelta, UTC


class DateHandler:
    STRING_FORMAT = "%Y-%m-%dT%H:%M:%SZ%z"
    STRING_INPUT_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
    date: datetime = datetime.now(UTC)
    now: datetime = datetime.now(UTC)

    def __init__(self, date=None):
        if date is None:
            self.date = datetime.now(UTC)
        else:
            if isinstance(date, str):
                self.date = datetime.strptime(date, DateHandler.STRING_INPUT_FORMAT)
            else:
                self.date = date

    @staticmethod
    def date_str_to_date_str_only_date(date_str) -> str:
        date_obj = datetime.strptime(date_str, DateHandler.STRING_FORMAT)
        return date_obj.strftime("%d/%m/%Y")

    @staticmethod
    def hhmm_from_date(date: str) -> str:
        return ":".join(date.split("T")[1].split(":")[:2])

    @staticmethod
    def is_valid_date(date_string) -> bool:
        try:
            datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
            return True
        except ValueError:
            return False
        except TypeError:
            return False

    def as_string(self) -> str:
        return self.date.strftime(DateHandler.STRING_FORMAT)

    def as_string_no_timezone(self) -> str:
        return self.date.strftime(DateHandler.STRING_FORMAT.rstrip("%z"))

    def as_date(self):
        return self.date

    def datetime_now(self):
        self.date = datetime(
            self.now.year,
            self.now.month,
            self.now.day,
            self.now.hour,
            self.now.minute,
            self.now.second,
        )
        return self

    def start_of_today(self):
        self.date = datetime(self.now.year, self.now.month, self.now.day, 0, 0, 0)
        return self

    def end_of_today(self):
        self.date = (
            self.start_of_today().as_date() + timedelta(days=1) - timedelta(minutes=10)
        )
        return self

    def shift(self, days=0, hours=0, minutes=0, seconds=0):
        self.date = (
            self.date
            + timedelta(days=days)
            + timedelta(hours=hours)
            + timedelta(minutes=minutes)
            + timedelta(seconds=seconds)
        )
        return self

    def yesterday(self):
        self.date = self.start_of_today().shift(days=-1).as_date()
        return self

    def tomorrow(self):
        self.date = self.start_of_today().shift(days=1).as_date()
        return self

    def tomorrow_hhmm(self, hour=0, minute=0):
        self.date = (
            self.start_of_today().shift(days=1, hours=hour, minutes=minute).as_date()
        )
        return self

    def yesterday_hhmm(self, hour=0, minute=0):
        self.date = (
            self.start_of_today().shift(days=-1, hours=hour, minutes=minute).as_date()
        )
        return self

    def today_hhmm(self, hour, minute=0):
        self.date = self.start_of_today().shift(hours=hour, minutes=minute).as_date()
        return self

    def get_diff(self, date_2) -> timedelta:
        delta = self.date - date_2
        return delta
