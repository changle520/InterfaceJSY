import json
import logging
from common.logger import Logging
from common.request import Request
from conf.jishiyu import url
from apilist.login import login
from common.dateEncoder import DateEncoder


Logging()
rq=Request()


def send_requests(method,api,data=None,params=None,headers=None,files=None,appendurl=None):
    '''
    发送接口请求，通用方法
    :param api:接口api
    :param method:请求方法
    :param headers:请求头
    :param params:请求参数
    :param kwargs:请求参数
    :return:返回接口的响应结果
    '''
    if appendurl: #有些api中有参数的拼接
        url_api = "{}/{}/{}".format(url, api,appendurl)
    else:
        url_api = "{}/{}".format(url,api)
    if data:
        data=json.dumps(data)  #把post请求的data参数值转换成字符串
        #data=json.dumps(data,cls=DateEncoder)  data中如果有日期格式的可以用这个方法
        data=data.replace("[null]","[]")  #把字符串中[null]替换成[],yaml文件中列表为空时读取后的值为[null]
    response = rq.request(method,url_api,data=data, params=params,headers=headers,files=files).json()
    return response


if __name__ == '__main__':
    api = "jsy-api-ops-pc/ops/pc/customer/wy/admin/update"
    params = {"groupName": "test", "initPassword": "123456", "mobile": "18888888888", "name": "xiaowang", "username": "xiaowang", "isLoginPc": 1, "isLoginApp": 0, "villageIdList": [189], "pcMenuList": [110, 111, 112, 113, 114], "appMenuList": [], "id": 496}
#     params={
#   "groupName": "test",
#   "initPassword": "123456",
#   "mobile": "18888888888",
#   "name": "postman",
#   "username": "postman",
#   "isLoginPc": 1,
#   "isLoginApp": 0,
#   "villageIdList": [
#     189
#   ],
#   "pcMenuList": [
#     110,
#     128,
#     129,
#     130,
#     131,
#     140,
#     162,
#     168,
#     243,
#     404,
#     411,
#     442,
#     111,
#     132,
#     396,
#     141,
#     145,
#     156,
#     415,
#     416,
#     135,
#     163,
#     164,
#     169,
#     325,
#     405,
#     406,
#     407,
#     408,
#     409,
#     410,
#     412,
#     443,
#     444,
#     112,
#     113,
#     114
#   ],
#   "appMenuList": [],
#   "id": 496
# }
    Authorization=login()[1]["Authorization"]
    headers={"Authorization": Authorization,"Content-Type": "application/json"}
    send_requests('POST',api,headers=headers,data=params)















