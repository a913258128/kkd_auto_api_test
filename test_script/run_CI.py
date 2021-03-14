import importlib
import pytest
import allure
import shutil
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(".")))
from base_services.base_request import HttpRequest, Response
from base_services.parse import parameter_replace

# 动态导入测试py文件
test_py = importlib.import_module("test_script.{}".format(os.getenv("runpy")), "test_script.test_apis.h5_api")

case_dict = test_py.api
case_list = [{k: v} for k, v in case_dict.items()]


@pytest.mark.parametrize("case", case_list)
def test_case_api(case):
    key = list(case.keys())[0]
    case = case.get(key)
    allure.dynamic.title(case.get("name"))
    case = parameter_replace(case, case_dict)
    result = HttpRequest(case).response
    response = Response(result)
    extract_dict = response.extract_response_json(case.get("extract"))
    case_dict[key]["extract"] = extract_dict
    response.assertions(case.get("validator"))


if __name__ == '__main__':
    ROOT_PATH = os.path.dirname(os.path.abspath("."))
    shutil.rmtree(fr'{ROOT_PATH}/report/xml', True)
    pytest.main(['-s', '-q', 'test_all.py', '--alluredir', f'{ROOT_PATH}/report/xml'])
