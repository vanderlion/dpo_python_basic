class Date:
    def __init__(self, *args):
        self.day, self.month, self.year = args

    @classmethod
    def parse_date_str(cls, str_date):
        return tuple(map(int, str_date.split('-')))

    @classmethod
    def is_date_valid(cls, str_date):
        d, m, y = cls.parse_date_str(str_date)
        return 0 < d <= 31 and 0 < m <= 12 and y > 0

    @classmethod
    def from_string(cls, str_date):
        assert cls.is_date_valid(str_date), 'Неверная дата'
        return cls(*cls.parse_date_str(str_date))

    def __str__(self):
        return 'День: %d Месяц: %d Год: %d' % (self.day, self.month, self.year)


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))