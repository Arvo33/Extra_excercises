# How do we get a date of Easter in given year

from datetime import datetime


def calculate_easter_date(year_input=datetime.now().year):
    year = year_input

    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    p = (h + l - 7 * m + 114) % 31
    q = (h + l - 7 * m + 114) // 31

    day = p + 1

    if q == 4:
        month = 'April'
    else:
        month = 'March'

    return f'{day} {month} {year}'


if __name__ == '__main__':
    print(calculate_easter_date(2015))
