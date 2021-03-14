from base_services.base_token import authorization_token
from base_services.faker_datas import *

api = {
    # 登录api
    "CustomerLogin": {
        "name": "商户登录\r\n(作者：陈超斌)",
        "request": {
            "method": "post",
            "url": "/Api/Customer/CustomerLogin",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "customerUserAccount": "天天果园",
                "password": "Sk123456"
            }
        },
        "extract": {"customerId": "body.data.customerId"},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "customerId": {
                                        "type": "integer",
                                        "description": "商户Id",
                                        "format": "int64"
                                    },
                                    "customerUserAccount": {
                                        "type": "string",
                                        "description": "商户账号",
                                        "Noneable": True
                                    },
                                    "photo": {
                                        "type": "string",
                                        "description": "商户头像",
                                        "Noneable": True
                                    },
                                    "acceptToken": {
                                        "type": "string",
                                        "description": "登录成功的Token",
                                        "Noneable": True
                                    }
                                }
                            }
                        }
                    }
                ]
            }
        ]
    },
    # 省市区api
    "GetArea": {
        "name": "获取大区\r\n(作者：张海琴)",
        "request": {
            "method": "post",
            "url": "/Api/ZoneArea/GetArea",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": None
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "zoneAreaID": {
                                            "type": "integer",
                                            "description": "中国大区Id",
                                            "format": "int64"
                                        },
                                        "zoneAreaName": {
                                            "type": "string",
                                            "description": "大区名称",
                                            "Noneable": True
                                        }
                                    }
                                },
                                "description": "返回结果（单个数据实体或数据实体的集合）",
                                "Noneable": True
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetProvince": {
        "name": "获取省\r\n(作者：张海琴)",
        "request": {
            "method": "post",
            "url": "/Api/ZoneArea/GetProvince",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": None
        },
        "extract": {"provinceId": "body.data[8].provinceID"},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "provinceID": {
                                            "type": "integer",
                                            "description": "省Id",
                                            "format": "int64"
                                        },
                                        "provinceName": {
                                            "type": "string",
                                            "description": "省名称",
                                            "Noneable": True
                                        },
                                        "zoneAreaID": {
                                            "type": "integer",
                                            "description": "大区id",
                                            "format": "int64"
                                        }
                                    }
                                },
                                "description": "返回结果（单个数据实体或数据实体的集合）",
                                "Noneable": True
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetCity": {
        "name": "获取市\r\n(作者：张海琴)",
        "request": {
            "method": "post",
            "url": "/Api/ZoneArea/GetCity",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": None
        },
        "extract": {"cityId": "body.data[72].cityID"},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "cityID": {
                                            "type": "integer",
                                            "description": "城市id",
                                            "format": "int64"
                                        },
                                        "cityName": {
                                            "type": "string",
                                            "description": "城市名称",
                                            "Noneable": True
                                        },
                                        "provinceID": {
                                            "type": "integer",
                                            "description": "省Id",
                                            "format": "int64"
                                        }
                                    }
                                },
                                "description": "返回结果（单个数据实体或数据实体的集合）",
                                "Noneable": True
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetDistrict": {
        "name": "获取区\r\n(作者：张海琴)",
        "request": {
            "method": "post",
            "url": "/Api/ZoneArea/GetDistrict",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": None
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "districtID": {
                                            "type": "integer",
                                            "description": "区Id",
                                            "format": "int64"
                                        },
                                        "districtName": {
                                            "type": "string",
                                            "description": "区域名称",
                                            "Noneable": True
                                        },
                                        "cityID": {
                                            "type": "integer",
                                            "description": "城市id",
                                            "format": "int64"
                                        }
                                    }
                                },
                                "description": "返回结果（单个数据实体或数据实体的集合）",
                                "Noneable": True
                            }
                        }
                    }
                ]
            }
        ]
    },
    # 门店api
    "AddStore": {
        "name": "新增门店\r\n(作者：张海琴)",
        "request": {
            "method": "post",
            "url": "/Api/Store/AddStore",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "provinceId": "${GetProvince.extract.provinceId}",
                "cityId": "${GetCity.extract.cityId}",
                "districtId": 16295,
                "detailAddress": faker_address(),
                "street": faker_street(),
                "longitude": faker_longitude(),
                "latitude": faker_latitude(),
                "name": faker_str() + "店",
                "contactName": faker_name(),
                "contactPhone": faker_phone(),
                "storeSpace": faker_number(3),
                "storeVirtualType": 2,
                "storeNum": faker_number(),
                "storeFranchiseType": 2,
                "businessHoursStart": "08:00:00",
                "businessHoursEnd": "20:00:00"
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "boolean",
                                "description": "返回结果（单个数据实体或数据实体的集合）"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetStoreList": {
        "name": "查询门店列表\r\n(作者：张海琴)",
        "request": {
            "method": "post",
            "url": "/Api/Store/GetStoreList",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "provinceId": "${GetProvince.extract.provinceId}",
                "cityId": "${GetCity.extract.cityId}",
                "districtId": "${AddStore.request.json.districtId}",
                "name": "${AddStore.request.json.name}",
                "storeNum": "",
                "pageIndex": 1,
                "pageSize": 10
            }
        },
        "extract": {"id": "body.data.data[0].id"},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "total": {
                                        "type": "integer",
                                        "description": "总页数",
                                        "format": "int64"
                                    },
                                    "data": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "integer",
                                                    "description": "主键",
                                                    "format": "int64"
                                                },
                                                "name": {
                                                    "type": "string",
                                                    "description": "门店名称",
                                                    "Noneable": True
                                                },
                                                "contactName": {
                                                    "type": "string",
                                                    "description": "联系人",
                                                    "Noneable": True
                                                },
                                                "contactPhone": {
                                                    "type": "string",
                                                    "description": "联系电话",
                                                    "Noneable": True
                                                },
                                                "provinceId": {
                                                    "type": "integer",
                                                    "description": "省Id",
                                                    "format": "int64"
                                                },
                                                "cityId": {
                                                    "type": "integer",
                                                    "description": "市Id",
                                                    "format": "int64"
                                                },
                                                "districtId": {
                                                    "type": "integer",
                                                    "description": "区Id",
                                                    "format": "int64"
                                                },
                                                "detailAddress": {
                                                    "type": "string",
                                                    "description": "详细地址",
                                                    "Noneable": True
                                                },
                                                "street": {
                                                    "type": "string",
                                                    "description": "街道/号",
                                                    "Noneable": True
                                                },
                                                "longitude": {
                                                    "type": "number",
                                                    "description": "经纬度（经度)",
                                                    "format": "double"
                                                },
                                                "latitude": {
                                                    "type": "number",
                                                    "description": "经纬度（纬度）",
                                                    "format": "double"
                                                },
                                                "businessHoursStart": {
                                                    "type": "string",
                                                    "description": "营业开始时间",
                                                    "Noneable": True
                                                },
                                                "businessHoursEnd": {
                                                    "type": "string",
                                                    "description": "营业时间（止）",
                                                    "Noneable": True
                                                },
                                                "status": {
                                                    "type": "integer",
                                                    "description": "状态(0正常1停业)",
                                                    "format": "int32"
                                                },
                                                "isDelete": {
                                                    "type": "integer",
                                                    "description": "是否删除（False未删除True已删除）",
                                                    "format": "int32"
                                                },
                                                "customerId": {
                                                    "type": "integer",
                                                    "description": "商户Id",
                                                    "format": "int64"
                                                },
                                                "addTime": {
                                                    "type": "string",
                                                    "description": "添加时间",
                                                    "format": "date-time"
                                                },
                                                "modifyTime": {
                                                    "type": "string",
                                                    "description": "修改时间",
                                                    "format": "date-time"
                                                },
                                                "storeNum": {
                                                    "type": "string",
                                                    "description": "门店编号",
                                                    "Noneable": True
                                                },
                                                "storeVirtualType": {
                                                    "type": "integer",
                                                    "description": "",
                                                    "format": "int32"
                                                },
                                                "storeFranchiseType": {
                                                    "type": "integer",
                                                    "description": "",
                                                    "format": "int32"
                                                },
                                                "storeSpace": {
                                                    "type": "number",
                                                    "format": "double"
                                                },
                                                "employCount": {
                                                    "type": "integer",
                                                    "format": "int64"
                                                },
                                                "detailAddressInfo": {
                                                    "type": "string",
                                                    "Noneable": True
                                                },
                                                "provinceName": {
                                                    "type": "string",
                                                    "Noneable": True
                                                },
                                                "cityName": {
                                                    "type": "string",
                                                    "Noneable": True
                                                },
                                                "districtName": {
                                                    "type": "string",
                                                    "Noneable": True
                                                }
                                            },
                                            "description": "门店输出参数"
                                        },
                                        "description": "分页数据",
                                        "Noneable": True
                                    }
                                },
                                "description": "门店列表查询输出类"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetStoreDetail": {
        "name": "门店详情\r\n(作者：张海琴)",
        "request": {
            "method": "post",
            "url": "/Api/Store/GetStoreDetail",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "id": "${GetStoreList.extract.id}"
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "integer",
                                        "description": "主键",
                                        "format": "int64"
                                    },
                                    "name": {
                                        "type": "string",
                                        "description": "门店名称",
                                        "Noneable": True
                                    },
                                    "contactName": {
                                        "type": "string",
                                        "description": "联系人",
                                        "Noneable": True
                                    },
                                    "contactPhone": {
                                        "type": "string",
                                        "description": "联系电话",
                                        "Noneable": True
                                    },
                                    "provinceId": {
                                        "type": "integer",
                                        "description": "省Id",
                                        "format": "int64"
                                    },
                                    "cityId": {
                                        "type": "integer",
                                        "description": "市Id",
                                        "format": "int64"
                                    },
                                    "districtId": {
                                        "type": "integer",
                                        "description": "区Id",
                                        "format": "int64"
                                    },
                                    "detailAddress": {
                                        "type": "string",
                                        "description": "详细地址",
                                        "Noneable": True
                                    },
                                    "street": {
                                        "type": "string",
                                        "description": "街道/号",
                                        "Noneable": True
                                    },
                                    "longitude": {
                                        "type": "number",
                                        "description": "经纬度（经度)",
                                        "format": "double"
                                    },
                                    "latitude": {
                                        "type": "number",
                                        "description": "经纬度（纬度）",
                                        "format": "double"
                                    },
                                    "businessHoursStart": {
                                        "type": "string",
                                        "description": "营业开始时间",
                                        "Noneable": True
                                    },
                                    "businessHoursEnd": {
                                        "type": "string",
                                        "description": "营业时间（止）",
                                        "Noneable": True
                                    },
                                    "status": {
                                        "type": "integer",
                                        "description": "状态(0正常1停业)",
                                        "format": "int32"
                                    },
                                    "isDelete": {
                                        "type": "integer",
                                        "description": "是否删除（False未删除True已删除）",
                                        "format": "int32"
                                    },
                                    "customerId": {
                                        "type": "integer",
                                        "description": "商户Id",
                                        "format": "int64"
                                    },
                                    "addTime": {
                                        "type": "string",
                                        "description": "添加时间",
                                        "format": "date-time"
                                    },
                                    "modifyTime": {
                                        "type": "string",
                                        "description": "修改时间",
                                        "format": "date-time"
                                    },
                                    "storeNum": {
                                        "type": "string",
                                        "description": "门店编号",
                                        "Noneable": True
                                    },
                                    "storeVirtualType": {
                                        "type": "integer",
                                        "description": "",
                                        "format": "int32"
                                    },
                                    "storeFranchiseType": {
                                        "type": "integer",
                                        "description": "",
                                        "format": "int32"
                                    },
                                    "storeSpace": {
                                        "type": "string",
                                        "Noneable": True
                                    }
                                },
                                "description": "门店详情输出类"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "UpdateStore": {
        "name": "修改门店\r\n(作者：张海琴)",
        "request": {
            "method": "post",
            "url": "/Api/Store/UpdateStore",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "id": "${GetStoreList.extract.id}",
                "provinceId": "${GetProvince.extract.provinceId}",
                "cityId": "${GetCity.extract.cityId}",
                "districtId": 16295,
                "detailAddress": faker_address(),
                "street": faker_street(),
                "longitude": faker_longitude(),
                "latitude": faker_latitude(),
                "name": faker_str() + "店",
                "contactName": faker_name(),
                "contactPhone": faker_phone(),
                "storeSpace": faker_number(3),
                "storeVirtualType": 2,
                "storeNum": faker_number(),
                "storeFranchiseType": 2,
                "businessHoursStart": "08:00:00",
                "businessHoursEnd": "20:00:00"
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "boolean",
                                "description": "返回结果（单个数据实体或数据实体的集合）"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetCoustomerStore": {
        "name": "获取商家门店列表\r\n(作者：张海琴)",
        "request": {
            "method": "post",
            "url": "/Api/Store/GetCoustomerStore",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": None
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer",
                                            "description": "门店id",
                                            "format": "int64"
                                        },
                                        "name": {
                                            "type": "string",
                                            "description": "门店名称",
                                            "Noneable": True
                                        }
                                    },
                                    "description": "获取商家门店列表"
                                },
                                "description": "返回结果（单个数据实体或数据实体的集合）",
                                "Noneable": True
                            }
                        }
                    }
                ]
            }
        ]
    },
    "ExportStore": {
        "name": "导出门店\r\n(作者：张海琴)",
        "request": {
            "method": "post",
            "url": "/Api/Store/ExportStore",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "provinceId": 0,
                "cityId": 0,
                "districtId": 0,
                "name": "",
                "storeNum": "",
                "pageIndex": 1,
                "ids": [],
                "pageSize": 19}
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "string",
                                "description": "返回结果（单个数据实体或数据实体的集合）",
                                "Noneable": True
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetStoreExportModel": {
        "name": "获取门店导入模板\r\n(作者：张海琴)",
        "request": {
            "method": "post",
            "url": "/Api/Store/GetStoreExportModel",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": None
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "path": {
                                        "type": "string",
                                        "Noneable": True
                                    }
                                }
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetStoreMapList": {
        "name": "在地图中显示门店\r\n(作者：张海琴)",
        "request": {
            "method": "post",
            "url": "/Api/Store/GetStoreMapList",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": None
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "storeMapData": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "integer",
                                                    "description": "门店id",
                                                    "format": "int64"
                                                },
                                                "name": {
                                                    "type": "string",
                                                    "description": "门店名称",
                                                    "Noneable": True
                                                },
                                                "detailAddress": {
                                                    "type": "string",
                                                    "description": "地址",
                                                    "Noneable": True
                                                },
                                                "longitude": {
                                                    "type": "number",
                                                    "description": "经纬度（经度)",
                                                    "format": "double"
                                                },
                                                "latitude": {
                                                    "type": "number",
                                                    "description": "经纬度（纬度）",
                                                    "format": "double"
                                                },
                                                "contactPhone": {
                                                    "type": "string",
                                                    "description": "联系电话",
                                                    "Noneable": True
                                                }
                                            }
                                        },
                                        "Noneable": True
                                    }
                                }
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetStoreData": {
        "name": "门店统计-总数据概览",
        "request": {
            "method": "post",
            "url": "/Api/Store/GetStoreData",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": None
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "totalDistributionPrice": {
                                        "type": "number",
                                        "description": "总业绩",
                                        "format": "double"
                                    },
                                    "totalOrderCount": {
                                        "type": "integer",
                                        "description": "总订单数",
                                        "format": "int64"
                                    },
                                    "totalMumberCount": {
                                        "type": "integer",
                                        "description": "会员总数",
                                        "format": "int64"
                                    },
                                    "totalAddMumberCount": {
                                        "type": "integer",
                                        "description": "有购会员数",
                                        "format": "int64"
                                    }
                                },
                                "description": "门店统计-总数据概览"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetStoreCommissionOrMemberMap": {
        "name": "门店统计-有购会员/分销业绩",
        "request": {
            "method": "post",
            "url": "/Api/Store/GetStoreCommissionOrMemberMap",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "valueType": 1,
                "dateType": 1,
                "storeId": 0,
                "startDate": "",
                "endDate": ""
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "storeData": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "summaryDate": {
                                                    "type": "string",
                                                    "description": "汇总日期",
                                                    "Noneable": True
                                                },
                                                "summaryVaule": {
                                                    "type": "number",
                                                    "description": "汇总数字",
                                                    "format": "double"
                                                }
                                            }
                                        },
                                        "Noneable": True
                                    }
                                },
                                "description": "门店统计-有购会员/分销业绩输出类"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetStoreCommissionOrMemberDetail": {
        "name": "门店统计-门店业绩/有购会员榜",
        "request": {
            "method": "post",
            "url": "/Api/Store/GetStoreCommissionOrMemberDetail",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "valueType": 1,
                "dayType": 1,
                "pageIndex": 1,
                "pageSize": 5
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "total": {
                                        "type": "integer",
                                        "format": "int64"
                                    },
                                    "dataList": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "integer",
                                                    "description": "门店id",
                                                    "format": "int64"
                                                },
                                                "name": {
                                                    "type": "string",
                                                    "description": "门店名称",
                                                    "Noneable": True
                                                },
                                                "employeeCount": {
                                                    "type": "integer",
                                                    "description": "员工数量",
                                                    "format": "int64"
                                                },
                                                "summaryVaule": {
                                                    "type": "number",
                                                    "description": "分销业绩/有购会员",
                                                    "format": "double"
                                                }
                                            }
                                        },
                                        "Noneable": True
                                    }
                                }
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetStoreDataDetail": {
        "name": "门店统计-门店数据明细",
        "request": {
            "method": "post",
            "url": "/Api/Store/GetStoreDataDetail",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "type": 1,
                "dateType": 1,
                "startDate": "",
                "endDate": "",
                "provinceId": 0,
                "cityId": 0,
                "districtId": 0,
                "name": "",
                "storeNum": "",
                "pageIndex": 1,
                "pageSize": 10
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "total": {
                                        "type": "integer",
                                        "format": "int64"
                                    },
                                    "detailData": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "integer",
                                                    "description": "门店id",
                                                    "format": "int32"
                                                },
                                                "name": {
                                                    "type": "string",
                                                    "description": "门店名称",
                                                    "Noneable": True
                                                },
                                                "storeNum": {
                                                    "type": "string",
                                                    "description": "门店编码",
                                                    "Noneable": True
                                                },
                                                "employeeCount": {
                                                    "type": "integer",
                                                    "description": "员工数量",
                                                    "format": "int64"
                                                },
                                                "storeSpace": {
                                                    "type": "number",
                                                    "description": "门店面积",
                                                    "format": "double"
                                                },
                                                "commissionPrice": {
                                                    "type": "number",
                                                    "description": "分销业绩",
                                                    "format": "double"
                                                },
                                                "commissionCount": {
                                                    "type": "integer",
                                                    "description": "分销销售量",
                                                    "format": "int64"
                                                },
                                                "memberCount": {
                                                    "type": "integer",
                                                    "description": "有购会员数",
                                                    "format": "int64"
                                                }
                                            }
                                        },
                                        "Noneable": True
                                    }
                                }
                            }
                        }
                    }
                ]
            }
        ]
    },
    "ExportStoreDataDetail": {
        "name": "门店统计-导出门店数据明细",
        "request": {
            "method": "post",
            "url": "/Api/Store/ExportStoreDataDetail",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "type": 1,
                "dateType": 1,
                "startDate": "",
                "endDate": "",
                "provinceId": 0,
                "cityId": 0,
                "districtId": 0,
                "name": "",
                "storeNum": "",
                "pageIndex": 1,
                "pageSize": 1
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "string",
                                "description": "返回结果（单个数据实体或数据实体的集合）",
                                "Noneable": True
                            }
                        }
                    }
                ]
            }
        ]
    },

    # 员工api
    "GetEmployeesList": {
        "name": "查询员工列表（作者:李德豪）",
        "request": {
            "method": "post",
            "url": "/Api/Employee/GetEmployeesList",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "name": "",
                "storeName": "",
                "phone": "",
                "credentialNo": "",
                "employeeRole": -1,
                "status": -1,
                "serviceStatus": 1,
                "storeId": -1,
                "pageIndex": 1,
                "pageSize": 10
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "selectEmployeeList": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "integer",
                                                    "description": "员工Id",
                                                    "format": "int64"
                                                },
                                                "name": {
                                                    "type": "string",
                                                    "description": "姓名",
                                                    "Noneable": True
                                                },
                                                "phone": {
                                                    "type": "string",
                                                    "description": "手机号",
                                                    "Noneable": True
                                                },
                                                "employeeRole": {
                                                    "type": "integer",
                                                    "description": "角色(0导购1店长)",
                                                    "format": "int32"
                                                },
                                                "storeName": {
                                                    "type": "string",
                                                    "description": "所属门店名称",
                                                    "Noneable": True
                                                },
                                                "credentialNo": {
                                                    "type": "string",
                                                    "description": "员工编号",
                                                    "Noneable": True
                                                },
                                                "userInfoCount": {
                                                    "type": "integer",
                                                    "description": "会员数量",
                                                    "format": "int32"
                                                },
                                                "status": {
                                                    "type": "integer",
                                                    "description": "员工状态（0启用1禁用）",
                                                    "format": "int32"
                                                },
                                                "serviceStatus": {
                                                    "type": "integer",
                                                    "description": "在职状态（0离职1在职）",
                                                    "format": "int32"
                                                },
                                                "isDelete": {
                                                    "type": "boolean",
                                                    "description": "是否删除"
                                                }
                                            }
                                        },
                                        "Noneable": True
                                    },
                                    "total": {
                                        "type": "integer",
                                        "description": "总数",
                                        "format": "int32"
                                    }
                                }
                            }
                        }
                    }
                ]
            }
        ]
    },
    "AddEmployee": {
        "name": "新增或修改员工（作者:李德豪）",
        "request": {
            "method": "post",
            "url": "/Api/Employee/AddEmployee",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "id": 0,
                "name": faker_name(),
                "gender": 1,
                "userAccount": faker_user_name(),
                "password": "",
                "credentialNo": faker_user_name(),
                "phone": faker_phone(),
                "storeId": "${GetStoreList.extract.id}",
                "employeeRole": 0,
                "status": 0,
                "employeePhoto": faker_image_url()
            }
        },
        "extract": {"id": "body.data.id"},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "integer",
                                        "description": "插入的主键Id",
                                        "format": "int64"
                                    },
                                    "userAccount": {
                                        "type": "string",
                                        "description": "用户账号",
                                        "Noneable": True
                                    }
                                }
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetEmployeeById": {
        "name": "根据员工id查询员工详情（作者：李德豪）",
        "request": {
            "method": "post",
            "url": "/Api/Employee/GetEmployeeById",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "employeeId": "${AddEmployee.extract.id}"
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "integer",
                                        "description": "主键",
                                        "format": "int64"
                                    },
                                    "name": {
                                        "type": "string",
                                        "description": "名称",
                                        "Noneable": True
                                    },
                                    "userAccount": {
                                        "type": "string",
                                        "description": "用户账号",
                                        "Noneable": True
                                    },
                                    "credentialNo": {
                                        "type": "string",
                                        "description": "员工编号",
                                        "Noneable": True
                                    },
                                    "phone": {
                                        "type": "string",
                                        "description": "手机号",
                                        "Noneable": True
                                    },
                                    "storeId": {
                                        "type": "integer",
                                        "description": "所属门店",
                                        "format": "int32"
                                    },
                                    "addTime": {
                                        "type": "string",
                                        "description": "添加时间",
                                        "format": "date-time"
                                    },
                                    "modifyTime": {
                                        "type": "string",
                                        "description": "修改时间",
                                        "format": "date-time"
                                    },
                                    "employeeRole": {
                                        "type": "integer",
                                        "description": "员工角色（0导购1店长）",
                                        "format": "int32"
                                    },
                                    "status": {
                                        "type": "integer",
                                        "description": "员工状态（0正常1禁用）",
                                        "format": "int32"
                                    },
                                    "isDelete": {
                                        "type": "boolean",
                                        "description": "是否删除"
                                    },
                                    "customerId": {
                                        "type": "integer",
                                        "description": "店铺Id",
                                        "format": "int64"
                                    },
                                    "memberNum": {
                                        "type": "integer",
                                        "description": "会员数量",
                                        "format": "int64"
                                    },
                                    "gender": {
                                        "type": "integer",
                                        "description": "性别1男2女3未知",
                                        "format": "int32"
                                    }
                                },
                                "description": "查询员工详情输出参数类"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "BatchDeleteEmployeeByIds": {
        "name": "批量删除员工",
        "request": {
            "method": "post",
            "url": "/Api/Employee/BatchDeleteEmployeeByIds",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "ids": [
                    0
                ]
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "boolean",
                                "description": "返回结果（单个数据实体或数据实体的集合）"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "UpdateEmployeeStateById": {
        "name": "修改员工状态（禁用、启用）（作者:李德豪）",
        "request": {
            "method": "post",
            "url": "/Api/Employee/UpdateEmployeeStateById",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "id": "${AddEmployee.extract.id}",
                "status": 0
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "boolean",
                                "description": "返回结果（单个数据实体或数据实体的集合）"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "BatchDisable": {
        "name": "批量禁用",
        "request": {
            "method": "post",
            "url": "/Api/Employee/BatchDisable",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "ids": [
                    "${AddEmployee.extract.id}"
                ]
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "code": {
                                "type": "integer",
                                "description": "结果代码",
                                "format": "int32"
                            },
                            "message": {
                                "type": "string",
                                "description": "返回信息",
                                "Noneable": True
                            },
                            "successful": {
                                "type": "boolean",
                                "description": "是否成功"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "ExportEmployee": {
        "name": "导出员工",
        "request": {
            "method": "post",
            "url": "/Api/Employee/ExportEmployee",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "name": "",
                "storeName": "",
                "phone": "",
                "credentialNo": "",
                "employeeRole": -1,
                "status": -1,
                "serviceStatus": 1,
                "storeId": -1,
                "pageIndex": 1,
                "pageSize": 10,
                "ids": []
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "string",
                                "description": "返回结果（单个数据实体或数据实体的集合）",
                                "Noneable": True
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetExportModel": {
        "name": "获取导入模板",
        "request": {
            "method": "post",
            "url": "/Api/Employee/GetExportModel",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": None
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "string",
                                "description": "返回结果（单个数据实体或数据实体的集合）",
                                "Noneable": True
                            }
                        }
                    }
                ]
            }
        ]
    },
    "EmployeeIQuit": {
        "name": "员工离职保存",
        "request": {
            "method": "post",
            "url": "/Api/Employee/EmployeeIQuit",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "employeeId": "${AddEmployee.extract.id}",
                "type": 1,
                "employeeIdUserIdQuit": [],
                "batchEmployeeIdQuitQuit": []
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "code": {
                                "type": "integer",
                                "description": "结果代码",
                                "format": "int32"
                            },
                            "message": {
                                "type": "string",
                                "description": "返回信息",
                                "Noneable": True
                            },
                            "successful": {
                                "type": "boolean",
                                "description": "是否成功"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetEmployeeQuitData": {
        "name": "获取员工离职信息",
        "request": {
            "method": "post",
            "url": "/Api/Employee/GetEmployeeQuitData",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "employeeId": "${AddEmployee.extract.id}"
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "thisMonthCommission": {
                                        "type": "number",
                                        "description": "本月待结算佣金",
                                        "format": "double"
                                    },
                                    "lastMonthCommission": {
                                        "type": "number",
                                        "description": "上月待结算佣金",
                                        "format": "double"
                                    },
                                    "fansNum": {
                                        "type": "integer",
                                        "description": "粉丝数",
                                        "format": "int32"
                                    },
                                    "qywxCustomerNum": {
                                        "type": "integer",
                                        "description": "企业微信客户数量",
                                        "format": "int32"
                                    },
                                    "customerGroupNum": {
                                        "type": "integer",
                                        "description": "客户群数量",
                                        "format": "int32"
                                    },
                                    "qywxCustomerList": {
                                        "type": ["array", "null"],
                                        "items": {
                                            "type": ["object", "null"],
                                            "properties": {
                                                "niceName": {
                                                    "type": "string",
                                                    "Noneable": True
                                                },
                                                "existUserId": {
                                                    "type": "string",
                                                    "Noneable": True
                                                }
                                            }
                                        },
                                        "description": "客户信息集合",
                                        "Noneable": True
                                    }
                                }
                            }
                        }
                    }
                ]
            }
        ]
    },
    "DeleteEmployeeById": {
        "name": "根据员工Id彻底删除员工（作者:李德豪）",
        "request": {
            "method": "post",
            "url": "/Api/Employee/DeleteEmployeeById",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "id": "${AddEmployee.extract.id}"
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "boolean",
                                "description": "返回结果（单个数据实体或数据实体的集合）"
                            }
                        }
                    }
                ]
            }
        ]
    },
    # 删除门店api
    "DeleteStoreById": {
        "name": "删除门店\r\n(作者：张海琴)",
        "request": {
            "method": "post",
            "url": "/Api/Store/DeleteStoreById",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "id": "${GetStoreList.extract.id}"
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "boolean",
                                "description": "返回结果（单个数据实体或数据实体的集合）"
                            }
                        }
                    }
                ]
            }
        ]
    },

    # 会员api
    "GetEmployeeBindMemberPC": {
        "name": "查询会员列表\r\n( 作者 : 梁超 )",
        "request": {
            "method": "post",
            "url": "/Api/UserInfo/GetEmployeeBindMemberPC",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "employeeId": 0,
                "name": "",
                "phone": "",
                "employeeName": "",
                "channelSources": 0,
                "bindRelation": 0,
                "pageIndex": 1,
                "pageSize": 10,
                "nickName": ""
            }
        },
        "extract": {
            "total": "body.data.total",
            "memberId0": "body.data.memberList[0].id",
            "exterUserId0": "body.data.memberList[0].exterUserId",
            "memberId1": "body.data.memberList[1].id",
            "exterUserId1": "body.data.memberList[1].exterUserId",
        },
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "memberList": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "integer",
                                                    "description": "会员ID",
                                                    "format": "int64"
                                                },
                                                "photo": {
                                                    "type": "string",
                                                    "description": "会员头像",
                                                    "Noneable": True
                                                },
                                                "nickName": {
                                                    "type": "string",
                                                    "description": "会员昵称",
                                                    "Noneable": True
                                                },
                                                "realName": {
                                                    "type": "string",
                                                    "description": "会员姓名",
                                                    "Noneable": True
                                                },
                                                "phone": {
                                                    "type": "string",
                                                    "description": "会员手机号",
                                                    "Noneable": True
                                                },
                                                "channelSourcesStr": {
                                                    "type": "string",
                                                    "description": "渠道来源描述",
                                                    "Noneable": True,
                                                    "readOnly": True
                                                },
                                                "exterUserId": {
                                                    "type": "integer",
                                                    "description": "外部用户Id（外部请求如连锁、单商户）",
                                                    "format": "int64"
                                                },
                                                "wxEnterpriseUserId": {
                                                    "type": ["string", "null"],
                                                    "description": "企业微信客户",
                                                    "Noneable": True
                                                },
                                                "channelSources": {
                                                    "type": "integer",
                                                    "description": "渠道来源1.微信小程序2.支付宝小程序",
                                                    "format": "int32"
                                                },
                                                "distributionRelationship": {
                                                    "type": "integer",
                                                    "description": "1.分配分销关系2.变更分销关系",
                                                    "format": "int32"
                                                }
                                            },
                                            "description": "会员列表"
                                        },
                                        "Noneable": True
                                    },
                                    "total": {
                                        "type": "integer",
                                        "description": "总数",
                                        "format": "int32"
                                    }
                                },
                                "description": "查询会员列表参数输出类"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetEmployeeBindMemberPCExport": {
        "name": "导出会员列表\r\n( 作者 : 梁超 )",
        "request": {
            "method": "post",
            "url": "/Api/UserInfo/GetEmployeeBindMemberPCExport",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "employeeId": 0,
                "name": "",
                "phone": "",
                "employeeName": "",
                "channelSources": 0,
                "bindRelation": 0,
                "pageIndex": 1,
                "nickName": "",
                "pageSize": "${GetEmployeeBindMemberPC.extract.total}",
                "ids": []
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "string",
                                "description": "返回结果（单个数据实体或数据实体的集合）",
                                "Noneable": True
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetChangeFansBindEmployee": {
        "name": "查询变更粉丝关系的员工列表",
        "request": {
            "method": "post",
            "url": "/Api/UserInfo/GetChangeFansBindEmployee",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "memberId": "${GetEmployeeBindMemberPC.extract.memberId0}",
                "name": "",
                "credentialNo": "",
                "storeId": 0,
                "pageIndex": 1,
                "pageSize": 10
            }
        },
        "extract": {
            "employeeId": "body.data.employeeId",
            "nowEmployeeId": "body.data.employeeData[0].id"
        },
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "niceName": {
                                        "type": "string",
                                        "description": "会员昵称",
                                        "Noneable": True
                                    },
                                    "employeeId": {
                                        "type": "integer",
                                        "description": "所属员工id",
                                        "format": "int64"
                                    },
                                    "name": {
                                        "type": "string",
                                        "description": "所属员工姓名",
                                        "Noneable": True
                                    },
                                    "credentialNo": {
                                        "type": "string",
                                        "description": "所属员工工号",
                                        "Noneable": True
                                    },
                                    "storeName": {
                                        "type": "string",
                                        "description": "所属门店名称",
                                        "Noneable": True
                                    },
                                    "employeeData": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "integer",
                                                    "description": "员工id",
                                                    "format": "int64"
                                                },
                                                "name": {
                                                    "type": "string",
                                                    "description": "员工姓名",
                                                    "Noneable": True
                                                },
                                                "credentialNo": {
                                                    "type": "string",
                                                    "description": "员工工号",
                                                    "Noneable": True
                                                },
                                                "storeName": {
                                                    "type": "string",
                                                    "description": "门店名称",
                                                    "Noneable": True
                                                },
                                                "handleStatus": {
                                                    "type": "boolean",
                                                    "description": "操作状态False设为上级"
                                                }
                                            }
                                        },
                                        "description": "员工列表",
                                        "Noneable": True
                                    },
                                    "total": {
                                        "type": "integer",
                                        "description": "总数",
                                        "format": "int64"
                                    }
                                },
                                "description": "变更粉丝关系查询员工方法响应类"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetProgramMemberDetails": {
        "name": "查询小程序会员详情",
        "request": {
            "method": "post",
            "url": "/Api/UserInfo/GetProgramMemberDetails",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "memberId": "${GetEmployeeBindMemberPC.extract.memberId0}",
                "exterUserId": "${GetEmployeeBindMemberPC.extract.exterUserId0}"
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "integer",
                                        "description": "主键Id",
                                        "format": "int64"
                                    },
                                    "userName": {
                                        "type": ["string", "null"],
                                        "description": "用户名称",
                                        "Noneable": True
                                    },
                                    "nickName": {
                                        "type": ["string", "null"],
                                        "description": "昵称",
                                        "Noneable": True
                                    },
                                    "phone": {
                                        "type": ["string", "null"],
                                        "description": "手机号",
                                        "Noneable": True
                                    },
                                    "photo": {
                                        "type": "string",
                                        "description": "头像",
                                        "Noneable": True
                                    },
                                    "registTime": {
                                        "type": "string",
                                        "description": "注册时间",
                                        "format": "date-time",
                                        "Noneable": True
                                    },
                                    "registTimeStr": {
                                        "type": "string",
                                        "description": "注册时间文本",
                                        "Noneable": True,
                                        "readOnly": True
                                    },
                                    "usualAddress": {
                                        "type": ["string", "null"],
                                        "description": "常用地址",
                                        "Noneable": True
                                    },
                                    "address": {
                                        "type": ["string", "null"],
                                        "description": "用户地址",
                                        "Noneable": True
                                    },
                                    "email": {
                                        "type": ["string", "null"],
                                        "description": "邮箱地址",
                                        "Noneable": True
                                    },
                                    "loginTime": {
                                        "type": "string",
                                        "description": "最后登陆时间",
                                        "format": "date-time",
                                        "Noneable": True
                                    },
                                    "loginTimeStr": {
                                        "type": "string",
                                        "description": "最后登陆时间文本",
                                        "Noneable": True,
                                        "readOnly": True
                                    },
                                    "sex": {
                                        "type": "integer",
                                        "description": "性别1=男0=女2=保密",
                                        "format": "int32"
                                    },
                                    "sexStr": {
                                        "type": "string",
                                        "description": "性别文本1=男0=女2=保密",
                                        "Noneable": True,
                                        "readOnly": True
                                    },
                                    "storeName": {
                                        "type": ["string", "null"],
                                        "description": "门店名称",
                                        "Noneable": True
                                    },
                                    "remark": {
                                        "type": ["string", "null"],
                                        "description": "备注",
                                        "Noneable": True
                                    }
                                },
                                "description": "查询小程序会员详情方法响应类"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetEnterpriseWechatCustomers": {
        "name": "查询企业微信客户基本信息",
        "request": {
            "method": "post",
            "url": "/Api/UserInfo/GetEnterpriseWechatCustomers",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "memberId": "${GetEmployeeBindMemberPC.extract.memberId0}"
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "name": {
                                        "type": ["string", "null"],
                                        "description": "姓名",
                                        "Noneable": True
                                    },
                                    "employees": {
                                        "type": ["string", "null"],
                                        "description": "所属员工",
                                        "Noneable": True
                                    },
                                    "sex": {
                                        "type": "integer",
                                        "description": "性别0=未知1=男2=女",
                                        "format": "int32"
                                    },
                                    "sexStr": {
                                        "type": "string",
                                        "description": "性别文本0=未知1=男2=女",
                                        "Noneable": True,
                                        "readOnly": True
                                    },
                                    "communicationTime": {
                                        "type": "string",
                                        "description": "最近沟通时间",
                                        "format": "date-time",
                                        "Noneable": True
                                    },
                                    "communicationTimeStr": {
                                        "type": "string",
                                        "description": "最近沟通时间文本",
                                        "Noneable": True,
                                        "readOnly": True
                                    }
                                },
                                "description": "查询企业微信客户基本信息方法响应类"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetTagInformation": {
        "name": "查询标签信息",
        "request": {
            "method": "post",
            "url": "/Api/UserInfo/GetTagInformation",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "exterUserId": "${GetEmployeeBindMemberPC.extract.exterUserId0}"
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer",
                                            "description": "标签Id",
                                            "format": "int64"
                                        },
                                        "labelName": {
                                            "type": "string",
                                            "description": "标签名称",
                                            "Noneable": True
                                        }
                                    },
                                    "description": "查询标签信息方法响应类"
                                },
                                "description": "返回结果（单个数据实体或数据实体的集合）",
                                "Noneable": True
                            }
                        }
                    }
                ]
            }
        ]
    },
    "UpdateRelationShip": {
        "name": "变更粉丝关系",
        "request": {
            "method": "post",
            "url": "/Api/UserInfo/UpdateRelationShip",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "id": "${GetEmployeeBindMemberPC.extract.memberId0}",
                "employeeId": "${GetChangeFansBindEmployee.extract.employeeId}",
                "nowEmployeeId": "${GetChangeFansBindEmployee.extract.nowEmployeeId}"
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "boolean",
                                "description": "返回结果（单个数据实体或数据实体的集合）"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetMemberInfoLS": {
        "name": "获取会员自身信息(调用连锁业务系统)\r\n( 作者 : 梁超 )",
        "request": {
            "method": "post",
            "url": "/Api/UserInfo/GetMemberInfoLS",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "exterUserId": "${GetEmployeeBindMemberPC.extract.exterUserId0}"
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "integral": {
                                        "type": "integer",
                                        "description": "会员积分",
                                        "format": "int64"
                                    },
                                    "deposit": {
                                        "type": "number",
                                        "description": "会员储值",
                                        "format": "double"
                                    },
                                    "couponCount": {
                                        "type": "integer",
                                        "description": "会员优惠券",
                                        "format": "int32"
                                    },
                                    "level": {
                                        "type": "integer",
                                        "description": "会员等级",
                                        "format": "int32"
                                    },
                                    "levelStr": {
                                        "type": "string",
                                        "description": "会员等级描述",
                                        "Noneable": True
                                    },
                                    "discount": {
                                        "type": "number",
                                        "description": "会员折扣",
                                        "format": "double"
                                    },
                                    "birthday": {
                                        "type": ["string", "null"],
                                        "description": "生日",
                                        "format": "date-time",
                                        "Noneable": True
                                    },
                                    "lastConsumptionDate": {
                                        "type": "string",
                                        "description": "最后消费时间",
                                        "format": "date-time",
                                        "Noneable": True
                                    },
                                    "tags": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "integer",
                                                    "description": "Id",
                                                    "format": "int64"
                                                },
                                                "name": {
                                                    "type": "string",
                                                    "description": "标签名称",
                                                    "Noneable": True
                                                }
                                            },
                                            "description": "会员标签"
                                        },
                                        "description": "会员标签",
                                        "Noneable": True
                                    }
                                },
                                "description": "获取会员自身信息(调用连锁业务系统)"
                            }
                        }
                    }
                ]
            }
        ]
    },

    # 分销api
    "GetCommissionSummaryData": {
        "name": "佣金汇总PC\r\n(作者：张海琴)",
        "request": {
            "method": "post",
            "url": "/Api/Commission/GetCommissionSummaryData",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "type": 0,
                "startDate": "",
                "endDate": ""
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "totalCommissionAmount": {
                                        "type": "number",
                                        "description": "总佣金",
                                        "format": "double"
                                    },
                                    "pullNewCommissionAmount": {
                                        "type": "number",
                                        "description": "拉新奖",
                                        "format": "double"
                                    },
                                    "firstCommissionAmount": {
                                        "type": "number",
                                        "description": "首购奖",
                                        "format": "double"
                                    },
                                    "distributionCommissionAmount": {
                                        "type": "number",
                                        "description": "分销奖",
                                        "format": "double"
                                    }
                                },
                                "description": "分销中心:佣金汇总参数输出类"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetCommissionTypeDetailPC": {
        "name": "拉新\\首购\\分销佣金明细统计PC\r\n ( 作者 : 张海琴 )",
        "request": {
            "method": "post",
            "url": "/Api/Commission/GetCommissionTypeDetailPC",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "name": "",
                "niceName": "",
                "orderNumber": "",
                "commissionType": 1,
                "type": 0,
                "startEffectTime": "",
                "endEffectTime": "",
                "startAddTime": "",
                "endAddTime": "",
                "pageIndex": 1,
                "pageSize": 10}
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "total": {
                                        "type": "integer",
                                        "description": "总数",
                                        "format": "int32"
                                    },
                                    "data": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "distributorId": {
                                                    "type": "integer",
                                                    "description": "员工ID",
                                                    "format": "int64"
                                                },
                                                "sourceUserInfoId": {
                                                    "type": "integer",
                                                    "description": "会员id",
                                                    "format": "int64"
                                                },
                                                "name": {
                                                    "type": "string",
                                                    "description": "员工姓名",
                                                    "Noneable": True
                                                },
                                                "credentialNo": {
                                                    "type": "string",
                                                    "description": "员工编号",
                                                    "Noneable": True
                                                },
                                                "phone": {
                                                    "type": "string",
                                                    "description": "手机号",
                                                    "Noneable": True
                                                },
                                                "type": {
                                                    "type": "integer",
                                                    "description": "佣金类型",
                                                    "format": "int32"
                                                },
                                                "amount": {
                                                    "type": "number",
                                                    "description": "奖励金额/拉新奖/首购奖/分销奖",
                                                    "format": "double"
                                                },
                                                "effectTime": {
                                                    "type": "string",
                                                    "description": "生效时间",
                                                    "Noneable": True
                                                },
                                                "niceName": {
                                                    "type": ["string", "null"],
                                                    "description": "会员名",
                                                    "Noneable": True
                                                },
                                                "addTime": {
                                                    "type": "string",
                                                    "description": "订单时间/拉新时间",
                                                    "Noneable": True
                                                },
                                                "orderNumber": {
                                                    "type": "string",
                                                    "description": "订单编号",
                                                    "Noneable": True
                                                },
                                                "validOrderAmount": {
                                                    "type": "number",
                                                    "description": "商品实付金额",
                                                    "format": "double"
                                                },
                                                "typeStr": {
                                                    "type": "string",
                                                    "Noneable": True
                                                }
                                            }
                                        },
                                        "description": "佣金明细PC",
                                        "Noneable": True
                                    }
                                },
                                "description": "拉新首购分销佣金明细统计PC响应实体类"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "ExportCommissionTypeDetail": {
        "name": "佣金明细导出\r\n张海琴",
        "request": {
            "method": "post",
            "url": "/Api/Commission/ExportCommissionTypeDetail",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "name": "",
                "niceName": "",
                "orderNumber": "",
                "commissionType": 1,
                "type": 0,
                "startEffectTime": "",
                "endEffectTime": "",
                "startAddTime": "",
                "endAddTime": "",
                "pageIndex": 1,
                "pageSize": 37}
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "string",
                                "description": "返回结果（单个数据实体或数据实体的集合）",
                                "Noneable": True
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetCommissionRulesPC": {
        "name": "获取分销佣金规则\r\n ( 作者 : 梁超 )",
        "request": {
            "method": "post",
            "url": "/Api/Commission/GetCommissionRulesPC",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": None
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "lachineAmount": {
                                        "type": "number",
                                        "description": "拉新奖励金额",
                                        "format": "double"
                                    },
                                    "firstProportion": {
                                        "type": "integer",
                                        "description": "首购奖比例",
                                        "format": "int32"
                                    },
                                    "distributionProportion": {
                                        "type": "integer",
                                        "description": "分销奖比例",
                                        "format": "int32"
                                    },
                                    "conflictProportion": {
                                        "type": "integer",
                                        "description": "佣金冲突分配比例0.5为50%",
                                        "format": "int32"
                                    },
                                    "effectiveType": {
                                        "type": "integer",
                                        "description": "佣金生效时机（0订单完成1支付完成）",
                                        "format": "int32"
                                    },
                                    "effectiveDay": {
                                        "type": "integer",
                                        "description": "佣金生效时机X天后生效",
                                        "format": "int32"
                                    },
                                    "protectedPeriod": {
                                        "type": "integer",
                                        "description": "保护期（天）",
                                        "format": "int32"
                                    }
                                },
                                "description": "获取分销佣金规则PC响应类"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "AddOrUpdateCommissionRulesPC": {
        "name": "新增或修改佣金规则设置\r\n ( 作者 : 梁超 )",
        "request": {
            "method": "post",
            "url": "/Api/Commission/AddOrUpdateCommissionRulesPC",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "ruleType": 1,
                "lachineAmount": 5.5,
                "firstProportion": 80,
                "distributionProportion": 50,
                "conflictProportion": 60,
                "effectiveType": 0,
                "effectiveDay": 1,
                "protectedPeriod": 7
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "boolean",
                                "description": "返回结果（单个数据实体或数据实体的集合）"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetDistributionAchievement": {
        "name": "分销业绩概况\r\n(作者：徐武峰)",
        "request": {
            "method": "post",
            "url": "/Api/Commission/GetDistributionAchievement",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": None
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "todayDistributionPrice": {
                                        "type": "number",
                                        "description": "今日分销业绩",
                                        "format": "double"
                                    },
                                    "todayDistributionOrder": {
                                        "type": "integer",
                                        "description": "今日分销订单数",
                                        "format": "int32"
                                    },
                                    "yesterdayDistributionPrice": {
                                        "type": "number",
                                        "description": "昨日分销业绩",
                                        "format": "double"
                                    },
                                    "yesterdayDistributionOrder": {
                                        "type": "integer",
                                        "description": "昨日分销订单数",
                                        "format": "int32"
                                    },
                                    "totalDistributionPrice": {
                                        "type": "number",
                                        "description": "分销总业绩",
                                        "format": "double"
                                    },
                                    "totalDistributionOrder": {
                                        "type": "integer",
                                        "description": "分销总订单数",
                                        "format": "int32"
                                    }
                                },
                                "description": "分销业绩概况传出业务操作类"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetDistributionEmployee": {
        "name": "分销员工概况\r\n(作者：徐武峰)",
        "request": {
            "method": "post",
            "url": "/Api/Commission/GetDistributionEmployee",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": None
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "todayDistributionNewUserCount": {
                                        "type": "integer",
                                        "description": "今日分销拉新人数",
                                        "format": "int32"
                                    },
                                    "yesterdayDistributionNewUserCount": {
                                        "type": "integer",
                                        "description": "昨日分销拉新人数",
                                        "format": "int32"
                                    },
                                    "todayUserShareCount": {
                                        "type": "integer",
                                        "description": "今日员工分享次数",
                                        "format": "int32"
                                    },
                                    "yesterdayUserShareCount": {
                                        "type": "integer",
                                        "description": "昨日员工分享次数",
                                        "format": "int32"
                                    },
                                    "totalDistributionNewUserCount": {
                                        "type": "integer",
                                        "description": "分销拉新总数",
                                        "format": "int32"
                                    },
                                    "totalUserShareCount": {
                                        "type": "number",
                                        "description": "日人均分享次数",
                                        "format": "double"
                                    }
                                },
                                "description": "分销员工概况传出业务操作类"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetDistributionCommissionSurvey": {
        "name": "分销佣金概况\r\n(作者：徐武峰)",
        "request": {
            "method": "post",
            "url": "/Api/Commission/GetDistributionCommissionSurvey",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": None
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "todayTotalCommissionAmount": {
                                        "type": "number",
                                        "description": "今日总佣金",
                                        "format": "double"
                                    },
                                    "yesterdayTotalCommissionAmount": {
                                        "type": "number",
                                        "description": "昨日总佣金",
                                        "format": "double"
                                    },
                                    "todayPullNewCommissionAmount": {
                                        "type": "number",
                                        "description": "今日拉新奖",
                                        "format": "double"
                                    },
                                    "yesterdayPullNewCommissionAmount": {
                                        "type": "number",
                                        "description": "昨日拉新奖",
                                        "format": "double"
                                    },
                                    "todayFirstCommissionAmount": {
                                        "type": "number",
                                        "description": "今日首购奖",
                                        "format": "double"
                                    },
                                    "yesterdayFirstCommissionAmount": {
                                        "type": "number",
                                        "description": "昨日首购奖",
                                        "format": "double"
                                    },
                                    "todayDistributionCommissionAmount": {
                                        "type": "number",
                                        "description": "今日分销奖",
                                        "format": "double"
                                    },
                                    "yesterdayDistributionCommissionAmount": {
                                        "type": "number",
                                        "description": "昨日分销奖",
                                        "format": "double"
                                    }
                                },
                                "description": "分销佣金概况传出业务操作类"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetDistributionAchievementMapSurvey": {
        "name": "分销趋势-分销业绩（7天，30天，自定义时间）\r\n(作者：徐武峰)",
        "request": {
            "method": "post",
            "url": "/Api/Commission/GetDistributionAchievementMapSurvey",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "dateType": 2,
                "startDate": "",
                "endDate": ""
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "summaryDate": {
                                            "type": "string",
                                            "description": "时间",
                                            "Noneable": True
                                        },
                                        "amountTotal": {
                                            "type": "number",
                                            "description": "分销业绩",
                                            "format": "double"
                                        }
                                    },
                                    "description": "分销趋势-分销业绩（7天，30天）传出业务操作类"
                                },
                                "description": "返回结果（单个数据实体或数据实体的集合）",
                                "Noneable": True
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetDistributionMemberMapSurvey": {
        "name": "分销趋势-有购会员数（7天，30天，自定义时间）\r\n(作者：徐武峰)",
        "request": {
            "method": "post",
            "url": "/Api/Commission/GetDistributionMemberMapSurvey",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "dateType": 2,
                "startDate": "",
                "endDate": ""
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "summaryDate": {
                                            "type": "string",
                                            "description": "汇总日期",
                                            "Noneable": True
                                        },
                                        "summaryCount": {
                                            "type": "number",
                                            "description": "汇总数量",
                                            "format": "double"
                                        }
                                    },
                                    "description": "分销趋势-有购会员数（7天，30天）传出业务操作类"
                                },
                                "description": "返回结果（单个数据实体或数据实体的集合）",
                                "Noneable": True
                            }
                        }
                    }
                ]
            }
        ]
    },

    # 数据统计api
    "ServiceStatistics": {
        "name": "数据汇总信息",
        "request": {
            "method": "post",
            "url": "/Api/Employee/ServiceStatistics",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": None
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "qywxCustomerNum": {
                                        "type": "integer",
                                        "description": "企业微信客户数量",
                                        "format": "int32"
                                    },
                                    "qyexMemberNum": {
                                        "type": "integer",
                                        "description": "企业微信成员数量",
                                        "format": "int32"
                                    },
                                    "replyDuration": {
                                        "type": "integer",
                                        "description": "回复时长",
                                        "format": "int32"
                                    },
                                    "chatShare": {
                                        "type": "integer",
                                        "description": "聊天占比",
                                        "format": "int32"
                                    }
                                }
                            }
                        }
                    }
                ]
            }
        ]
    },
    "ServiceStatisticsEmployee": {
        "name": "数据-服务质量员工列表",
        "request": {
            "method": "post",
            "url": "/Api/Employee/ServiceStatisticsEmployee",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "name": "string",
                "credentialNo": "string",
                "storeName": "string",
                "pageIndex": 0,
                "pageSize": 0
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "employeeDatas": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "integer",
                                                    "format": "int64"
                                                },
                                                "name": {
                                                    "type": "string",
                                                    "Noneable": True
                                                },
                                                "credentialNo": {
                                                    "type": "string",
                                                    "Noneable": True
                                                },
                                                "phone": {
                                                    "type": "string",
                                                    "Noneable": True
                                                },
                                                "storeName": {
                                                    "type": "string",
                                                    "Noneable": True
                                                },
                                                "qyConsumerNum": {
                                                    "type": "integer",
                                                    "description": "企业微信客户数",
                                                    "format": "int64"
                                                },
                                                "negativeFeedbackCnt": {
                                                    "type": "integer",
                                                    "description": "删除/拉黑成员的客户数",
                                                    "format": "int32"
                                                },
                                                "avgReplyTime": {
                                                    "type": "integer",
                                                    "description": "平均首次回复时长",
                                                    "format": "int32"
                                                },
                                                "chatCnt": {
                                                    "type": "integer",
                                                    "description": "聊天总数",
                                                    "format": "int32"
                                                },
                                                "replyPercentage": {
                                                    "type": "number",
                                                    "description": "已回复聊天比例",
                                                    "format": "float"
                                                },
                                                "corporateWXUserId": {
                                                    "type": "string",
                                                    "Noneable": True
                                                }
                                            }
                                        },
                                        "Noneable": True
                                    },
                                    "total": {
                                        "type": "integer",
                                        "description": "总数",
                                        "format": "int32"
                                    }
                                }
                            }
                        }
                    }
                ]
            }
        ]
    },
    "ExportServiceStatisticsEmployee": {
        "name": "数据-服务质量导出",
        "request": {
            "method": "post",
            "url": "/Api/Employee/ExportServiceStatisticsEmployee",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "name": "",
                "credentialNo": "",
                "storeName": "",
                "pageIndex": 1,
                "pageSize": 10}
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "string",
                                "description": "返回结果（单个数据实体或数据实体的集合）",
                                "Noneable": True
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetEmployeeStatisticalSummary": {
        "name": "数据统计-员工统计汇总",
        "request": {
            "method": "post",
            "url": "/Api/Employee/GetEmployeeStatisticalSummary",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": None
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "employeeTotal": {
                                        "type": "integer",
                                        "description": "员工总数",
                                        "format": "int32"
                                    },
                                    "binMemberTotal": {
                                        "type": "integer",
                                        "description": "绑定会员数",
                                        "format": "int32"
                                    },
                                    "lachineMemberTotal": {
                                        "type": "integer",
                                        "description": "拉新会员数",
                                        "format": "int32"
                                    },
                                    "shareTotal": {
                                        "type": "number",
                                        "description": "日人均分享次数",
                                        "format": "double"
                                    }
                                },
                                "description": "数据统计-员工统计汇总参数输出类"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetEmployeeStatisticalList": {
        "name": "数据统计-员工统计列表",
        "request": {
            "method": "post",
            "url": "/Api/Employee/GetEmployeeStatisticalList",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "customerId": "${CustomerLogin.extract.customerId}",
                "orderType": 3,
                "dateType": 0,
                "startDate": "",
                "endDate": "",
                "name": "",
                "credentialNo": "",
                "storeName": "",
                "storeNum": "",
                "pageIndex": 1,
                "pageSize": 10
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "data": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "integer",
                                                    "description": "员工Id",
                                                    "format": "int64"
                                                },
                                                "name": {
                                                    "type": "string",
                                                    "description": "员工姓名",
                                                    "Noneable": True
                                                },
                                                "credentialNo": {
                                                    "type": "string",
                                                    "description": "员工工号",
                                                    "Noneable": True
                                                },
                                                "storeName": {
                                                    "type": "string",
                                                    "description": "门店名称",
                                                    "Noneable": True
                                                },
                                                "shareSum": {
                                                    "type": "integer",
                                                    "description": "分享次数",
                                                    "format": "int32"
                                                },
                                                "lachineMemberSum": {
                                                    "type": "integer",
                                                    "description": "拉新人数",
                                                    "format": "int32"
                                                },
                                                "fansSum": {
                                                    "type": "integer",
                                                    "description": "总粉丝数",
                                                    "format": "int32"
                                                },
                                                "commissionAchievement": {
                                                    "type": "number",
                                                    "description": "分销业绩（元）",
                                                    "format": "double"
                                                },
                                                "commissionMoney": {
                                                    "type": "number",
                                                    "description": "佣金（元）",
                                                    "format": "double"
                                                }
                                            },
                                            "description": "数据统计-员工列表"
                                        },
                                        "description": "数据统计-员工列表",
                                        "Noneable": True
                                    },
                                    "total": {
                                        "type": "integer",
                                        "description": "总数",
                                        "format": "int32"
                                    }
                                },
                                "description": "数据统计-员工统计列表参数输出类"
                            }
                        }
                    }
                ]
            }
        ]
    },
    "GetEmployeeStatisticalListExport": {
        "name": " 数据统计-员工统计列表导出\r\n( 作者 : 梁超 )",
        "request": {
            "method": "post",
            "url": "/Api/Employee/GetEmployeeStatisticalListExport",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "customerId": "${CustomerLogin.extract.customerId}",
                "orderType": 3,
                "dateType": 0,
                "startDate": "",
                "endDate": "",
                "name": "",
                "credentialNo": "",
                "storeName": "",
                "storeNum": "",
                "pageIndex": 1,
                "pageSize": 75
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "string",
                                "description": "返回结果（单个数据实体或数据实体的集合）",
                                "Noneable": True
                            }
                        }
                    }
                ]
            }
        ]
    },
    # 企业api
    "GetSuiteAuthLink": {
        "name": "获取企业信息",
        "request": {
            "method": "post",
            "url": "/Api/ExternalServices/GetSuiteAuthLink",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": {
                "redirectUri": "string"
            }
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "state": {
                                "type": "boolean",
                                "description": "是否授权"
                            },
                            "qyWeiXinAuthUrl": {
                                "type": "string",
                                "description": "企业微信授权链接",
                                "Noneable": True
                            },
                            "qyWeiXinRegistered": {
                                "type": "string",
                                "description": "注册企业微信跳转",
                                "Noneable": True
                            },
                            "qyWeiXinCancelAuthorization": {
                                "type": "string",
                                "description": "企业微信取消授权链接",
                                "Noneable": True
                            },
                            "authCorpInfo": {
                                "type": "object",
                                "properties": {
                                    "corpId": {
                                        "type": "string",
                                        "description": "授权方企业微信id",
                                        "Noneable": True
                                    },
                                    "corpName": {
                                        "type": "string",
                                        "description": "授权方企业微信名称",
                                        "Noneable": True
                                    },
                                    "corpType": {
                                        "type": "string",
                                        "description": "授权方企业微信类型，认证号：verified,注册号：unverified",
                                        "Noneable": True
                                    },
                                    "corpSquareLogoUrl": {
                                        "type": "string",
                                        "description": "授权方企业微信方形头像",
                                        "Noneable": True
                                    },
                                    "corpUserMax": {
                                        "type": "integer",
                                        "description": "授权方企业微信用户规模",
                                        "format": "int32"
                                    },
                                    "corpFullName": {
                                        "type": "string",
                                        "description": "所绑定的企业微信主体名称(仅认证过的企业有)",
                                        "Noneable": True
                                    },
                                    "subjectType": {
                                        "type": "integer",
                                        "description": "企业类型，1.企业;2.政府以及事业单位;3.其他组织,4.团队号",
                                        "format": "int32"
                                    },
                                    "verifiedEndTime": {
                                        "type": "integer",
                                        "description": "认证到期时间(时间戳)",
                                        "format": "int32"
                                    },
                                    "verifiedEndTimeStr": {
                                        "type": "string",
                                        "description": "认证到期时间",
                                        "Noneable": True
                                    },
                                    "corpWxqrCode": {
                                        "type": "string",
                                        "description": "授权企业在微工作台（原企业号）的二维码，可用于关注微工作台",
                                        "Noneable": True
                                    },
                                    "corpScale": {
                                        "type": "string",
                                        "description": "企业规模。当企业未设置该属性时，值为空",
                                        "Noneable": True
                                    },
                                    "corpIndustry": {
                                        "type": "string",
                                        "description": "企业所属行业。当企业未设置该属性时，值为空",
                                        "Noneable": True
                                    },
                                    "corpSubIndustry": {
                                        "type": "string",
                                        "description": "企业所属子行业。当企业未设置该属性时，值为空",
                                        "Noneable": True
                                    },
                                    "location": {
                                        "type": "string",
                                        "description": "企业所在地信息,为空时表示未知",
                                        "Noneable": True
                                    }
                                },
                                "description": "企业信息"
                            }
                        },
                        "description": "授权企业微信账户获取企业信息传出业务操作类"
                    }
                ]
            }
        ]
    },
    # 商家退出api
    "CustomerLogout": {
        "name": "商户退出登录\r\n(作者：陈超斌)",
        "request": {
            "method": "post",
            "url": "/Api/Customer/CustomerLogout",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "authorization": authorization_token('pc')
            },
            "json": None
        },
        "extract": {},
        "validator": [
            {
                "eq": [
                    "status_code",
                    200
                ]
            },
            {
                "schema": [
                    "body",
                    {
                        "type": "object",
                        "properties": {
                            "code": {
                                "type": "integer",
                                "description": "结果代码",
                                "format": "int32"
                            },
                            "message": {
                                "type": "string",
                                "description": "返回信息",
                                "Noneable": True
                            },
                            "successful": {
                                "type": "boolean",
                                "description": "是否成功"
                            }
                        }
                    }
                ]
            }
        ]
    }
}
