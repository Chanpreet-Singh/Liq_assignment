import string
import random
import secrets
import datetime

def get_unique_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(secrets.choice(characters) for x in range(length))
    return random_string

def get_random_date(start_timestamp, end_timestamp):
    random_timestamp = random.uniform(start_timestamp, end_timestamp)
    random_date = datetime.datetime.fromtimestamp(random_timestamp).date()
    return random_date

def get_random_number(range_start=-99999999, range_end=99999999):
    return random.randint(range_start, range_end)