import logging

from requests.auth import HTTPBasicAuth
from requests_futures.sessions import FuturesSession
import json
from datetime import datetime

import config.yunyizz_config


class AsyncHTTPHandler(logging.Handler):
    def __init__(self, max_workers=5):
        super().__init__()
        self.session = FuturesSession(max_workers=max_workers)

    def emit(self, record):
        try:
            data = {
                'timestamp': datetime.fromtimestamp(record.created).isoformat(),
                'level': record.levelname,
                'logger': record.name,
                'message': record.getMessage(),
                'module': record.module,
                'function': record.funcName,
                'line': record.lineno,
                'async_task': config.yunyizz_config.ASYNC_TASK_ID
            }

            # 异步发送请求
            future = self.session.post(
                url=config.yunyizz_config.BASE_URL + f"/api/log-entries/",
                headers={'content-type': 'application/json;charset=UTF-8', 'accept': "application/json"},
                json=data,
                timeout=5,
                auth=HTTPBasicAuth(config.yunyizz_config.USERNAME, config.yunyizz_config.PASSWORD)
            )

            # 可以选择性地处理响应
            future.add_done_callback(self._handle_response)

        except Exception as e:
            self.handleError(record)

    def _handle_response(self, future):
        try:
            response = future.result()
            if response.status_code >= 400:
                print(f"HTTP logging failed: {response.status_code}")
        except Exception as e:
            print(f"Response handling error: {e}")
