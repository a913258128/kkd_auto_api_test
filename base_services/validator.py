import json
from jsonschema import validate, ValidationError


def equal_validator(data1, data2):
    assert data1 == data2, f"相等验证失败: {data1} 不等于 {data2}"


def not_equals_validator(data1, data2):
    assert data1 != data2, f"不相等验证失败: {data1} 等于 {data2}"


def contains_validator(data1, data2):
    assert data2 in data1, f"包含验证失败: {data2} 不在 {data1} 中"


def json_schema_validator(instance, schema):
    def _json_schema():
        try:
            validate(instance, schema)
            return 1
        except ValidationError as ex:
            return ex

    assert _json_schema() == 1, f"schema 类型验证失败: \n\n{_json_schema()}"
