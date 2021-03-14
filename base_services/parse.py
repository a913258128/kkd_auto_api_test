from base_services.utils import gen_headers, check_contain_chinese
from base_services.utils import request_add_allure_report
from jsonpath_rw import jsonpath, parse
import json
import re


def parse_request(describe_dict):
    request_data = describe_dict.get("request")
    body = request_data.get("data") or request_data.get("json")
    if not body:
        try:
            request_data.pop("json")
        except KeyError:
            pass
    headers = request_data.get("headers", {"Content-Type": "application/json; charset=utf-8"})
    gen_headers(headers, headers.get("authorization", ""), body)
    request_data["headers"] = headers
    request_add_allure_report(request_data)
    if check_contain_chinese(str(body)):
        # body中有中文进行转码
        body_data = json.dumps(body, ensure_ascii=False).encode(encoding="utf-8")
        request_data["data"] = body_data
        try:
            request_data.pop("json")
        except KeyError:
            pass
    return request_data


def parameter_replace(json_data, a_json):
    try:
        json_data, a_json = json.dumps(json_data, ensure_ascii=False), json.dumps(a_json, ensure_ascii=False)
    except TypeError as e:
        raise TypeError("py用例文件转成json失败{}".format(e))
    pattern = re.compile(r'\${(.*?)}')
    results = pattern.findall(json_data)
    for result in results:
        json_path_expr = parse(str(result))
        try:
            json_depend_list = [match.value for match in
                                json_path_expr.find(json.loads(a_json, encoding='utf-8'))]
            json_depend = json_depend_list[0]
            if isinstance(json_depend, int):
                json_depend = str(json_depend)
                json_data = pattern.sub(json_depend, json_data, count=1).replace(f'"{json_depend}"', json_depend)
            else:
                json_data = pattern.sub(json_depend, json_data, count=1)
        except BaseException:
            raise KeyError("从用例文件中提取字段失败:${%s}" % result)
    return json.loads(json_data, encoding="utf-8")


def parse_validator(describe_dict: dict):
    assert_method = list(describe_dict.keys())[0]
    assert_value = describe_dict[assert_method]
    if assert_method in ["eq", "equal"]:
        assert_method = "equal_validator"
    elif assert_method in ["schema", "json_schema"]:
        assert_method = "json_schema_validator"
    elif assert_method in ["neq", "not_equal"]:
        assert_method = "not_equals_validator"
    elif assert_method in ["in", "contains"]:
        assert_method = "contains_validator"
    else:
        raise KeyError("验证器没有该断言方法:{}".format(assert_method))
    check_value, expected_result = assert_value
    return {"assert_method": assert_method, "check_value": check_value, "expected_result": expected_result}
