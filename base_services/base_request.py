from requests import request
from jsonpath import jsonpath
from dotenv import find_dotenv, load_dotenv
from base_services.utils import result_add_allure_report, get_fun, request_add_allure_report, \
    validator_add_allure_report
from base_services.settings import config
from base_services import validator
from base_services.parse import parse_request, parse_validator
import os

load_dotenv(find_dotenv())


class HttpRequest:
    def __init__(self, request_dict):
        self.request_dict = parse_request(request_dict)
        self.response = self.__http_request()

    def __http_request(self):
        host = os.getenv("runurl")
        config_set = config.get(os.environ.get("runenv"), "test_config")
        if not host:
            host = config_set.host
        url = f"{host}{self.request_dict.get('url')}"
        self.request_dict["url"] = url
        r_obj = request(**self.request_dict)
        return r_obj


class Response:
    def __init__(self, response):
        self.response = response
        try:
            body = response.json()
        except ValueError:
            body = response.text
        self.result = dict(status_code=response.status_code,
                           cookies=dict(response.cookies),
                           headers=response.headers,
                           body=body,
                           time=response.elapsed.total_seconds())
        result_add_allure_report(self.result)

    def extract_response_json(self, extract):
        if extract:
            extract_dict = {}
            for extract_key, extract_value in extract.items():
                extract_data = jsonpath(self.result, extract_value)
                if extract_data:
                    value = extract_data[0]
                else:
                    raise ValueError("extract 在响应报文中通过{}提取字段失败请检查是否正确".format(extract_value))
                extract_dict[extract_key] = value
            return extract_dict

    def assertions(self, validations):
        validator_result_list = []
        for validation_allure in validations:
            validation_allure = parse_validator(validation_allure)
            assert_method = validation_allure.get("assert_method")
            assert_method = get_fun(validator, assert_method)
            request_actual_result_json_path = validation_allure.get("check_value")
            request_actual_result = jsonpath(self.result, request_actual_result_json_path)
            if request_actual_result:
                request_actual_result = jsonpath(self.result, request_actual_result_json_path)[0]
            else:
                raise ValueError("验证器{}未能通过{}提取到值进行断言".format(validation_allure, request_actual_result_json_path))

            try:
                assert_method(request_actual_result, validation_allure.get("expected_result"))
                status = "ok"
            except AssertionError:
                status = "fail"
            validator_result_list.append(
                {"assert_method": validation_allure.get("assert_method"),
                 "textfield": request_actual_result_json_path,
                 "expect_value": validation_allure.get("expected_result"),
                 "actual_value": request_actual_result,
                 "status": status
                 }
            )
        validator_add_allure_report(validator_result_list)
        for validation in validations:
            validation = parse_validator(validation)
            assert_method = validation.get("assert_method")
            assert_method = get_fun(validator, assert_method)
            request_actual_result_json_path = validation.get("check_value")
            request_actual_result = jsonpath(self.result, request_actual_result_json_path)[0]
            assert_method(request_actual_result, validation.get("expected_result"))
