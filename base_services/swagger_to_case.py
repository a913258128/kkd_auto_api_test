import os
import re
import json
import requests
from tkinter import *
import tkinter.messagebox

LOG_LINE_NUM = 0

PATH = os.path.abspath('tools')


class SwaggerToCase:
    def __init__(self, url):
        self.url = url
        self.api = {}
        try:
            self.r_obj = requests.get(self.url).json()
        except BaseException as e:
            raise BaseException("请求swagger接口json错误: {}".format(e))

    def to_parse_case(self):
        # 转成测试py文件
        for k, v in self.r_obj.get("paths").items():
            method_key = list(v.keys())[0]
            k_name = str(k).split("/")[-1]
            name = v.get(method_key).get("summary")
            if not name:
                name = k_name
            request_headers = {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": "authorization_token()"
            }
            #  解析请求body字段
            request_body_key = v.get(method_key).get("requestBody")
            if not request_body_key:
                request_body_key = None
            elif request_body_key:
                application_json = request_body_key.get("content").get("application/json")
                if application_json:
                    request_body_key = application_json.get("schema").get("$ref")
                    if request_body_key:
                        request_body_key = str(request_body_key).split("/")[-1]
                    else:
                        request_body_key = None
                else:
                    request_body_key = None
            body_json = self.swagger_body_extract(request_body_key)
            # 解析响应body字段
            response_body_key = v.get(method_key).get("responses")
            status_code = None
            response_body = {}
            if response_body_key:
                status_code = list(response_body_key.keys())[0]
                # 获取swagger—responses下的content字段
                response_content = response_body_key.get(status_code).get("content")
                if response_content:
                    response_application_json_schema = response_content.get("application/json").get("schema")
                    if response_application_json_schema:
                        response_application_json_schema_ref = response_application_json_schema.get("$ref")
                        if response_application_json_schema_ref:
                            components_schemas_key = str(response_application_json_schema_ref).split("/")[-1]
                            schemas_dict = self.r_obj.get("components").get("schemas").get(components_schemas_key)
                            response_body = schemas_dict
                            while True:
                                if "$ref" in str(schemas_dict):
                                    json_schemas = json.dumps(schemas_dict, ensure_ascii=False)
                                    # print(json_schemas)
                                    re_compile = re.compile(
                                        r'{"\$ref": "#/components/schemas/(\w+)"}')
                                    re_components_schemas_key = \
                                        re.findall(re_compile, json_schemas)[0]
                                    schemas_data = self.r_obj.get("components").get("schemas").get(
                                        re_components_schemas_key)
                                    json_schemas_data = json.dumps(schemas_data, ensure_ascii=False)
                                    schemas_on = re_compile.sub(json_schemas_data, json_schemas)
                                    response_body_no_space = re.sub(r'[\s+]', '', schemas_on).replace("\\", "")
                                    response_body = json.loads(response_body_no_space, encoding="utf-8")
                                    schemas_dict = response_body
                                elif "$ref" not in str(schemas_dict):
                                    break

                        else:
                            response_application_json_schema_ref = response_application_json_schema.get("items").get(
                                "$ref")
                            components_schemas_key = str(response_application_json_schema_ref).split("/")[-1]

                            response_body = self.r_obj.get("components").get("schemas").get(components_schemas_key)

            self.api.update({k_name: {"name": name,
                                      "request": {"method": method_key, "url": k, "headers": request_headers,
                                                  "json": body_json},
                                      "extract": {},
                                      "validator": [{'eq': ['status_code', int(status_code)]},
                                                    {'schema': ['body', response_body]}]
                                      },
                             })

    def swagger_body_extract(self, key):
        # 从swagger的components字段数据下提取请求的数据
        if key:
            body = {}
            swagger_schema = self.r_obj.get("components").get("schemas").get(key)
            properties = swagger_schema.get("properties")
            for k, v in properties.items():
                body_arg_type = v.get("type")
                if body_arg_type:
                    if "int" in body_arg_type:
                        body_arg = 0
                    elif "bool" in body_arg_type:
                        body_arg = True
                    elif "str" in body_arg_type:
                        body_arg = "string"
                    elif "array" in body_arg_type:
                        body_arg = []
                        array_arg_type = v.get("items").get("type")
                        if array_arg_type:
                            if "int" in array_arg_type:
                                body_arg.append(0)
                            elif "str" in array_arg_type:
                                body_arg.append("string")
                        elif not array_arg_type:
                            array_arg_type = v.get("items").get("$ref")
                            if array_arg_type:
                                ref_key = str(array_arg_type).split("/")[-1]
                                ref_dict = self.r_obj.get("components").get("schemas").get(ref_key)
                                list_value_dict = {}
                                for ref_k, ref_v in ref_dict.get("properties").items():
                                    ref_v_arg_type = ref_v.get("type")
                                    if "int" in ref_v_arg_type:
                                        ref_v_value = 0
                                    elif "str" in ref_v_arg_type:
                                        ref_v_value = "string"
                                    else:
                                        ref_v_value = ""
                                    list_value_dict.update({ref_k: ref_v_value})
                                body_arg.append(list_value_dict)
                    else:
                        body_arg = ""
                else:
                    body_arg = ""
                body.update({k: body_arg})
            return body
        else:
            return


def main(url, filename, token_type=""):
    content = """from base_services.base_token import authorization_token
from base_services.faker_datas import *

# faker_datas 模块下的方法用于快速造数据
# authorization_token 用于生成token可以自定义扩展

api = {}

"""
    if token_type:
        token_fun = "authorization_token('{}')".format(token_type)
    else:
        token_fun = '""'

    swagger_obj = SwaggerToCase(url)
    swagger_obj.to_parse_case()
    test_obj_json = json.dumps(swagger_obj.api, ensure_ascii=False, indent=4)
    content = content.format(
        test_obj_json.replace('null', "None").replace('"authorization_token()"', token_fun).replace('true',
                                                                                                    "True").replace(
            'false', "False"))
    with open(f"{PATH}/{filename}.py", "w", encoding="utf-8") as f:
        f.write(content)


class MyGUI:
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    # 设置窗口
    def set_init_window(self):
        self.init_window_name.title("Swagger用例转换器")  # 窗口名
        scn_w, scn_h = self.init_window_name.maxsize()
        cen_x = (scn_w - 500) / 2
        cen_y = (scn_h - 240) / 2
        size_xy = '%dx%d+%d+%d' % (500, 240, cen_x, cen_y)
        self.init_window_name.geometry(size_xy)

        # 标签
        self.url_label = Label(self.init_window_name, text="URL地址:")
        self.url_label.grid(row=2, column=0)
        self.filename_label = Label(self.init_window_name, text="文  件 名:")
        self.filename_label.grid(row=9, column=0)
        self.token_label = Label(self.init_window_name, text="请求头token:")
        self.token_label.grid(row=12, column=0)
        self.pass_lable = Label(self.init_window_name, text="")
        self.pass_lable.grid(row=20, column=0)

        # 文本框
        self.url_text = Text(self.init_window_name, width=56, height=2)
        self.url_text.grid(row=2, column=1, rowspan=1, columnspan=1)
        self.file_text = Text(self.init_window_name, width=56, height=2)
        self.file_text.grid(row=9, column=1, rowspan=3, columnspan=3)
        self.token_text = Text(self.init_window_name, width=56, height=2)
        self.token_text.grid(row=12, column=1, rowspan=3, columnspan=3)

        # 按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="生成用例", bg="lightblue", width=10,
                                              command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=30, column=1, rowspan=5, columnspan=5)

        # # 警告框
        # self.alert = tkinter.messagebox.showinfo(title='信息提示！', message='内容：您的女朋友收到一只不明来历的口红！')

    # 功能函数
    def str_trans_to_md5(self):
        url = self.url_text.get("0.0", "end").replace(" ", "").split("\n")[0]
        file = self.file_text.get("0.0", "end").replace(" ", "").split("\n")[0]
        token_type = self.token_text.get("0.0", "end").replace(" ", "").split("\n")[0]
        try:
            main(url, file, token_type)
            tkinter.messagebox.showinfo(title='信息提示！', message='生成用例成功,文件名为{}.py'.format(file))
        except BaseException as e:
            tkinter.messagebox.showinfo(title='信息提示！', message=e)


def gui_start():
    init_window = Tk()  # 实例化出一个父窗口
    ZMJ_PORTAL = MyGUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()
    init_window.resizable(False, False)

    init_window.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


if __name__ == '__main__':
    gui_start()
