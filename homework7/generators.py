import random
from datetime import datetime, timedelta


def all_even_numbers():
    return list(num for num in range(0, 100, 2))


def random_increasing_number():
    pass


def next_day():
    today = datetime.today().date()
    return today + datetime.timedelta(days=day)
