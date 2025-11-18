from functools import wraps

from yunyizz.api import MarkTaskFail, MarkTaskRun


def yunyizz_decorator(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        MarkTaskRun().send()
        try:
            ret = await func(*args, **kwargs)
            return ret
        except Exception as e:
            MarkTaskFail(str(e))
            return None
    return wrapper
