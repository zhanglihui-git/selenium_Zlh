import pprint

import requests

from test_wework.api.wework import Wework
from test_wework.utils.Utils import Utils


class BaseApi:
    printer = pprint.PrettyPrinter(indent=2)
    json_data = None

    @classmethod
    def verbose(cls, json_object=json_data):
        print(Utils.format(json_object))
        cls.printer.pprint(json_object)

    @classmethod
    def jsonpath(cls, expr):
        return Utils.jsonpath(cls.json_data, expr)

    def request(self, method, url, params: dict, json, data):
        requests.request(method, url=url, params=params.update({"access_token": Wework.get_app_token()}))
        self.verbose(self.json_data)
        return self.json_data

    def test_run_single_yaml(self):
        single_json =