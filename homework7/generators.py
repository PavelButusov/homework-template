import random
from datetime import datetime, timedelta


def all_even_numbers():
    for i in range(0,100,2):
        yield i


def random_increasing_number(start_from = 0):
    last_num = start_from
    next_num = random.randint(last_num, last_num + 150)
    while True:
        next_num = random.randint(next_num, next_num+150)
        yield next_num


def next_day():
    today = datetime.today().date()
    for i in range(100):
        yield today
        today += timedelta(days=1)

gen = next_day()
