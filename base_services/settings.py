class Development:
    pc_setting = {
        "customerUserAccount": "天天果园",
        "password": "Sk123456",
    }
    h5_settings = {
        "loginAccount": "m002",
        "password": "sk123456",
        "openId": "",
        "openUserId": "woNNqDBwAA9wG54Vw04Y95_AckBqwW3A",
        "customerId": 15681
    }


class Production:
    pc_setting = {
        "customerUserAccount": "天天果园",
        "password": "Sk123456",
    }
    h5_settings = {
        "loginAccount": "m002",
        "password": "sk123456",
        "openId": "",
        "openUserId": "woNNqDBwAA9wG54Vw04Y95_AckBqwW3A",
        "customerId": 15681
    }


config = {
    "test_config": Development,
    "online_config": Production
}
