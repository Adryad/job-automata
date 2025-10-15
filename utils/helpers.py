import time, random

def random_sleep(min_sec=2, max_sec=6):
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)
