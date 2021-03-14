from faker import Faker
import datetime

f = Faker(locale='zh_CN')


def faker_name():
    # 假姓名
    return f.name()


def faker_header():
    # 假请求头
    return f.user_agent()


def faker_user_name():
    # 假用户名
    return f.user_name() + f.numerify() + f.random_element().upper()


def faker_password():
    # 假密码
    return f.password()


def faker_phone():
    # 假手机号
    return f.phone_number()


def faker_address():
    # 假地址，不准确
    return f.address()


def faker_street():
    # 假街道，不准确
    return f.street_address()


def faker_longitude():
    # 假经度
    return str(f.longitude())


def faker_latitude():
    # 假纬度
    return str(f.latitude())


def faker_email():
    # 假邮箱
    return f.email()


def faker_str():
    # 假的4个字符串
    return f.word() + f.word()


def faker_paragraph():
    # 假的一段话
    return f.text()


def faker_image_url():
    # 假的图片地址
    return f.image_url()


def faker_number(length=5):
    # 生成假的数值 默认5位 可修改
    return int(f.random_number(length))


def faker_time(day=0, formats='day'):
    """
    :param day: 数字
    :param formats: 时间格式
    :return: 根据计算机当前日期获取+ -day的日期
    """
    time = datetime.datetime.now()
    time_now = datetime.datetime.now()
    if formats == 'day':
        time = (time_now + datetime.timedelta(days=day)).strftime('%Y-%m-%d')
    elif formats == 'minute':
        time = (time_now + datetime.timedelta(days=day)).strftime('%Y-%m-%d %H:%M')
    elif formats == 'second':
        time = (time_now + datetime.timedelta(days=day)).strftime('%Y-%m-%d %H:%M:%S')
    elif formats == 'hms':
        time = (time_now + datetime.timedelta(days=day)).strftime('%H:%M:%S')
    elif formats == 'unix':
        time = str(round((time_now + datetime.timedelta(days=day)).timestamp() * 1000))
    return time



