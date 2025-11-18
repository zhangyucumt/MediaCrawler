import logging
import time

import requests
import json

from requests import HTTPError
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException

import config.yunyizz_config
from tools import utils


class YunyizzBaseRequest(object):
    base_url = config.yunyizz_config.BASE_URL
    method = 'get'
    request_params = None
    request_body = None
    path = ""
    headers = {'content-type': 'application/json;charset=UTF-8', 'accept': "application/json"}
    timeout = 10
    try_count = 3
    deprecated = False

    def send(self, raise_exception=True):
        url = self.base_url + self.path
        error_msg = ""
        for i in range(self.try_count):
            try:
                resp = requests.request(
                    self.method,
                    url,
                    params=self.request_params,
                    json=self.request_body,
                    headers=self.headers,
                    timeout=self.timeout,
                    auth=HTTPBasicAuth(config.yunyizz_config.USERNAME, config.yunyizz_config.PASSWORD)
                )
                resp.raise_for_status()
            except (RequestException, HTTPError) as e:
                utils.logger.error("rpc yunyizz request({} {} {}) request error: {}".format(
                    url, json.dumps(self.request_params, sort_keys=True), json.dumps(self.request_body, sort_keys=True), str(e)
                ))
                error_msg = str(e)
                time.sleep(5)
                continue
            else:
                try:
                    resp_json = resp.json()
                except:
                    utils.logger.info("rpc yunyizz request({} {} {}) response({} {})".format(
                        url, json.dumps(
                            self.request_params, sort_keys=True, ensure_ascii=False
                        ), json.dumps(
                            self.request_body, sort_keys=True, ensure_ascii=False
                        ), resp.status_code, resp.content.decode('utf-8')
                    ))
                    error_msg = f"请求yunyizz接口失败: {resp.content.decode('utf-8')}"
                    time.sleep(5)
                    continue
                else:
                    if self.method != 'get':
                        utils.logger.info("rpc yunyizz request({} {} {}) response({} {})".format(
                            url, json.dumps(
                                self.request_params, sort_keys=True, ensure_ascii=False
                            ), json.dumps(
                                self.request_body, sort_keys=True, ensure_ascii=False
                            ), resp.status_code, resp.content.decode('utf-8')
                        ))
                    if not resp_json["success"]:
                        utils.logger.error("rpc yunyizz request({} {} {}) response({} {})".format(
                            url, json.dumps(
                                self.request_params, sort_keys=True, ensure_ascii=False
                            ), json.dumps(
                                self.request_body, sort_keys=True, ensure_ascii=False
                            ), resp.status_code, resp.content.decode('utf-8')
                        ))
                        error_msg = f"请求yunyizz接口失败: {resp_json['message']}"
                        break
                    return self.process_resp(resp_json)
        if raise_exception:
            raise Exception(error_msg)
        return None

    def process_resp(self, resp):
        return resp["data"]
