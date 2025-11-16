import config.yunyizz_config
from .base import YunyizzBaseRequest


class UpdateYunyizzAsyncTask(YunyizzBaseRequest):
    path = f"/async-task/{config.yunyizz_config.ASYNC_TASK_ID}"
    method = "patch"

    def __init__(self, body: dict):
        self.request_body = body



