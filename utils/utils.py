# utils/utils.py
import time
import random

def random_sleep(min_sec: float = 2.0, max_sec: float = 6.0):
    """
    ينتظر عشوائيًا بين min_sec و max_sec ثواني.
    استخدم هذا بدل time.sleep() لخفض احتمالية الكشف.
    """
    if min_sec < 0 or max_sec < 0:
        raise ValueError("min_sec and max_sec must be non-negative")
    if max_sec < min_sec:
        min_sec, max_sec = max_sec, min_sec
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)
    return delay  # مفيد للتسجيل/debug إذا أردت
