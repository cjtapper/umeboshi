"""
Umeboshi provides two locking mechanisms. If using a cache with its own
`lock()` method (such as [python redis lock][prs]), it will make use of that.
Otherwise it provides its own simple locking implementation.

[prs]: https://pypi.python.org/pypi/python-redis-lock
"""
import contextlib
import time

from django.core.cache import cache

__all__ = ("lock",)

lock_key = "umeboshi-event-{}"


@contextlib.contextmanager
def simple_lock(lock_key, timeout=5000, redis_timeout_sec=5):
    """
    A simple context manager that raises the passed exception
    if a lock can't be acquired.
    """

    def acquire_lock():
        return cache.add(lock_key, 1, redis_timeout_sec)

    def release_lock():
        cache.delete(lock_key)

    waited, hops = 0, 10
    while not acquire_lock():
        time.sleep(float(hops) / 1000.0)
        waited += hops
        if waited > timeout:
            raise RuntimeError(f"Lock could not be acquired after {waited}ms")

    try:
        yield
    finally:
        release_lock()


if hasattr(cache, "lock"):

    def lock(id):
        return cache.lock(lock_key.format(id), expire=15)

else:

    def lock(id):
        return simple_lock(lock_key.format(id))
