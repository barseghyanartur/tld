from functools import wraps

__all__ = (
    'profile',
)


def profile(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapped
