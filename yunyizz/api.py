import config.yunyizz_config
from .base import YunyizzBaseRequest

class SetSpiderAccountOffline(YunyizzBaseRequest):
    path = f"/api/spider-accounts/{config.yunyizz_config.SPIDER_ACCOUNT_ID}/"
    method = "patch"

    def __init__(self):
        self.request_body = {
            "is_online": False
        }


class MarkTaskWaiting(YunyizzBaseRequest):
    path = f"/api/async-tasks/{config.yunyizz_config.ASYNC_TASK_ID}/"
    method = "patch"

    def __init__(self):
        self.request_body = {
            "status": "waiting"
        }



class MarkTaskRun(YunyizzBaseRequest):
    path = f"/api/async-tasks/{config.yunyizz_config.ASYNC_TASK_ID}/"
    method = "patch"

    def __init__(self):
        self.request_body = {
            "status": "running"
        }


class MarkTaskFinish(YunyizzBaseRequest):
    path = f"/api/async-tasks/{config.yunyizz_config.ASYNC_TASK_ID}/"
    method = "patch"

    def __init__(self):
        self.request_body = {
            "status": "success"
        }


class MarkTaskFail(YunyizzBaseRequest):
    path = f"/api/async-tasks/{config.yunyizz_config.ASYNC_TASK_ID}/"
    method = "patch"

    def __init__(self, error_msg: str):
        self.request_body = {
            "status": "failed",
            "result": {
                "error_msg": error_msg
            }
        }


class GetMissingAuthors(YunyizzBaseRequest):
    path = f"/api/social-users/missing/"
    method = "post"

    def __init__(self, user_ids):
        self.request_body = {
            "platform": config.yunyizz_config.PLATFORM,
            "user_ids": user_ids
        }

    def process_resp(self, resp):
        ret = super().process_resp(resp)
        return ret.get("missing_user_ids", [])



class UploadAuthor(YunyizzBaseRequest):
    path = f"/api/social-users/"
    method = "post"

    def __init__(self,
                 user_id: str,
                 *,
                 avatar: str = "",
                 nickname: str = "",
                 description: str = "",
                 follow_count: int = 0,
                 follower_count: int = 0,
                 ip_location: str = "",
                 like_count: str = "",
                 like_count_num: int = 0,
                 tags: list = None,
                 homepage_link: str = "",
                 redbook_id: str = "",
                 ext_info: dict = None
        ):
        self.request_body = {
          "keyword": config.KEYWORDS,
          "platform": config.yunyizz_config.PLATFORM,
          "avatar": avatar,
          "nickname": nickname,
          "description": description,
          "follow_count": follow_count,
          "follower_count": follower_count,
          "ip_location": ip_location,
          "like_count": like_count,
          "like_count_num": like_count_num,
          "user_id": user_id,
          "tags": tags or [],
          "homepage_link": homepage_link,
          "redbook_id": redbook_id,
          "ext_info": ext_info or {}
        }
