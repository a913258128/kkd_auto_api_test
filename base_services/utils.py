import importlib
import hashlib
import datetime
import json
import allure
import os
import re


def gen_sign(timestamp="", authorization="", body=None):
    if body is None:
        body = ''
    elif body:
        body = str(body)

    en_str = f"timestamp={timestamp}&body={body}&authorization={authorization}".replace("'", '"')
    m = hashlib.md5()
    m.update(en_str.encode('utf8'))
    mtr_str_word = m.hexdigest()
    return mtr_str_word.lower()


def gen_time():
    time = (datetime.datetime.now() + datetime.timedelta(seconds=30)).timestamp()
    time = int(round(time * 1000))
    return str(time)


def gen_headers(header, authorization, body=None):
    timestamp = gen_time()
    if authorization:
        authorization = "Bearer {}".format(authorization)
    header.update(
        {"sign": gen_sign(timestamp=timestamp, authorization=authorization, body=body), "timestamp": timestamp,
         "authorization": authorization})
    return header


def get_fun(o, fun_name):
    if hasattr(o, fun_name):
        return getattr(o, fun_name)
    else:
        raise ValueError("方法不存在")


def result_add_allure_report(result):
    """
    每个用例执行完添加到allure
    :return:
    """
    body = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>响应报文</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
          integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
</head>
<body>
<div class="container" style="text-align: left;margin-left: 0">
    <table style="width: 500px;" class="table table-striped table-hover table-bordered">
        <tbody>
        <tr>
            <td>status_code</td>
            <td>{result.get("status_code")}</td>
        </tr>
        <tr>
            <td>time</td>
            <td>{result.get("time")}S</td>
        </tr>
        <tr>
            <td>cookies</td>
            <td>{result.get("cookies")}</td>
        </tr>
        <tr>
            <td>headers</td>
            <td><pre>{result.get("headers")}</pre></td>
        </tr>
        <tr>
            <td>body</td>
            <td><pre>{json.dumps(result.get("body"), ensure_ascii=False, indent=4)}</pre></td>
        </tr>
        </tbody>
    </table>
</div>
</body>
</html>
"""
    allure.attach(body, '响应报文', allure.attachment_type.HTML)


def request_add_allure_report(result):
    """
    每个用例执行完添加到allure
    :return:
    """
    body = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>请求报文</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
          integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
</head>
<body>
<div class="container" style="text-align: left;margin-left: 0">
    <table style="width: 500px;" class="table table-striped table-hover table-bordered">
        <tbody>
        <tr>
            <td>method</td>
            <td>{result.get("method")}</td>
        </tr>
        <tr>
            <td>url</td>
            <td>{result.get("url")}</td>
        </tr>
        <tr>
            <td>headers</td>
            <td><pre>{json.dumps(result.get("headers"), ensure_ascii=False, indent=4)}</pre></td>
        </tr>
        <tr>
            <td>body</td>
            <td><pre>{json.dumps(result.get("json") or result.get("data"), ensure_ascii=False, indent=4)}</pre></td>
        </tr>
        </tbody>
    </table>
</div>
</body>
</html>
"""
    allure.attach(body, '请求报文', allure.attachment_type.HTML)


def validator_add_allure_report(result: list):
    """
    每个用例执行完添加到allure
    :return:
    """
    body = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>验证器</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
          integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
</head>
<body>
<div class="container" style="text-align: left;margin-left: 0">
    <table style="width: 500px;" class="table table-striped table-hover table-bordered">
        <tbody>
        <tr>
            <td>验证方式</td>
            <td>比对值</td>
            <td>预期结果</td>
            <td>实际结果</td>
            <td>状态</td>
        </tr>
            {}
        </tbody>
    </table>
</div>
</body>
</html>
"""
    tr_str_list = []
    for i in result:
        str_f = """<tr>
<td>{}</td>
<td>{}</td>
<td><pre>{}</pre></td>
<td><pre>{}</pre></td>
<td {}>{}</td>
</tr>"""
        expect_value = i.get("expect_value")
        actual_value = i.get("actual_value")
        try:
            expect_value = json.dumps(expect_value, ensure_ascii=False, indent=4)
            actual_value = json.dumps(actual_value, ensure_ascii=False, indent=4)
        except TypeError:
            pass
        if i.get("status") == "ok":
            status_style = 'style="background: green"'
        else:
            status_style = 'style="background: red"'
        str_f = str_f.format(i.get("assert_method"), i.get("textfield"), expect_value,
                             actual_value, status_style, i.get("status"))

        tr_str_list.append(str_f)
    all_validator_tr = "\n".join(tr_str_list)
    body = body.format(all_validator_tr)
    allure.attach(body, '验证断言', allure.attachment_type.HTML)


def check_contain_chinese(check_str):
    for ch in check_str:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    else:
        return False


def dynamic_import(package=""):
    modules = []
    package_path = os.path.dirname(os.path.abspath('.')) + os.sep + package
    files = os.listdir(package_path)
    for file in files:
        if not file.startswith("__") and not file.startswith("."):
            name, suffix = os.path.splitext(file)
            modules.append("." + name)
    for module in modules:
        importlib.import_module(module, package)
