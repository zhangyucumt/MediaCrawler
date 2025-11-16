from functools import wraps

from yunyizz.api import UpdateYunyizzAsyncTask


def yunyizz_decorator(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        UpdateYunyizzAsyncTask(
            body={
                "status": "running",
                "message": f"{func.__name__} is running..."
            }
        ).send()
        try:
            ret = await func(*args, **kwargs)
            UpdateYunyizzAsyncTask(
                body={
                    "status": "success",
                    "message": f"{func.__name__} completed successfully."
                }
            ).send()
            return ret
        except Exception as e:
            UpdateYunyizzAsyncTask(
                body={
                    "status": "failed",
                    "message": f"{func.__name__} failed: {e}"
                }
            ).send()
            return None
    return wrapper
