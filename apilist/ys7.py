import json
import logging
from common.logger import Logging
from common.request import Request
from conf.jishiyu import ysy_url
from apilist.login import login


Logging()
rq=Request()


def send_requests(method,api,data=None,params=None,headers=None,files=None):
    '''
    发送接口请求，通用方法
    :param api:接口api
    :param method:请求方法
    :param headers:请求头
    :param params:请求参数
    :param kwargs:请求参数
    :return:返回接口的响应结果
    '''
    url_api = "{}/{}".format(ysy_url,api)
    if data:
        data=json.dumps(data)  #把post请求的data参数值转换成字符串

    response = rq.request(method,url_api,data=data, params=params,headers=headers,files=files).json()
    return response


if __name__ == '__main__':
    api = "jsy-api-ops-pc/ops/pc/customer/supervise/admin/list"
    params = {"page": 1, "size": 10}
    Authorization=login()["Authorization"]
    headers={"Authorization": Authorization}
    send_requests('GET',api,headers=headers,params=params)















