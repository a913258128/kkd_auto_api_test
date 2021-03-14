import os
from base_services.base_request import HttpRequest, Response
from base_services.settings import config

run_config = config[os.getenv("runenv", "test_config")]


def authorization_token(login_type="PC"):
    if login_type in ["pc", "PC"]:
        login_api = {
            "name": "登录",
            "request": {
                "method": "POST",
                "url": "/Api/Customer/CustomerLogin",
                "json": run_config.pc_setting,
            },
            "extract": {
                "token": "body.data.acceptToken"
            },
            "validator": [
                {"eq": ["status_code", 200]}

            ]

        }
    elif login_type in ["h5", "H5"]:
        login_api = {
            "name": "登录",
            "request": {
                "method": "POST",
                "url": "/Api/Employee/EmployeeLogin",
                "json": run_config.h5_settings,
            },
            "extract": {
                "token": "body.data.acceptToken"
            },
            "validator": [
                {"eq": ["status_code", 200]}

            ]

        }
    else:
        login_api = {}
    rs = Response(HttpRequest(login_api).response)
    rs.assertions(login_api.get("validator"))
    authorization = rs.extract_response_json(login_api.get("extract"))["token"]
    return authorization


if __name__ == '__main__':
    print(authorization_token('h5'))
