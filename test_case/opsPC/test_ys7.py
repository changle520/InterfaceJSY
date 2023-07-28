import pytest
import allure
from apilist.ys7 import send_requests
from common.readYaml import ReadFileData
import logging
from common.logger import Logging

Logging()


#实例化读取配置文件的类,获取配置文件
readFileData=ReadFileData()
data=readFileData.get_data('test_data/ParamYaml','ops_pc_api.yml')

#   //以下是定义的初始化、清除方法//
# @pytest.fixture(scope='function',autouse=False)
@pytest.fixture(scope='module',autouse=True)
def get_Token_id_setup():
        print("在这个模块文件里只执行一次^_^")

        #获取accessToken
        method=data["get_accessToken"][0]["Method"]
        apiurl=data["get_accessToken"][0]["ApiUrl"]
        params=data["get_accessToken"][0]["Params"]
        response=send_requests(method,apiurl,params=params)
        accessToken=response['data']['accessToken']

        #获取consumerId
        method = data["get_consumerId"][0]["Method"]
        apiurl = data["get_consumerId"][0]["ApiUrl"]
        params = data["get_consumerId"][0]["Params"]
        params['accessToken'] = accessToken
        response = send_requests(method, apiurl, params=params)
        consumerId=response['data']['consumerId']
        return {'accessToken':accessToken,"consumerId":consumerId}


#   //以下是测试用例//
@allure.feature("运维管理平台")
@allure.story("萤石云接口")
@allure.title("获取accessToken")
@allure.description("")
def test_get_accessToken_001():
        method=data["get_accessToken"][0]["Method"]
        apiurl=data["get_accessToken"][0]["ApiUrl"]
        params=data["get_accessToken"][0]["Params"]

        #发送请求
        response=send_requests(method,apiurl,params=params)
        #断言
        assert response['code']=='200'
        assert response['msg']=="操作成功!"
        assert response['data']['accessToken']!=""

@allure.feature("运维管理平台")
@allure.story("萤石云接口")
@allure.title("读取consumerId")
@allure.description("")
def test_get_consumerId_001(get_Token_id_setup):
        method=data["get_consumerId"][0]["Method"]
        apiurl=data["get_consumerId"][0]["ApiUrl"]
        params=data["get_consumerId"][0]["Params"]
        params['accessToken']=get_Token_id_setup['accessToken']

        #发送请求
        response=send_requests(method,apiurl,params=params)
        #断言
        assert response['code']=='200'
        assert response['msg']=="操作成功"
        assert response['data']['consumerId']!=""

@allure.feature("运维管理平台")
@allure.story("萤石云接口")
@allure.title("订阅消息")
@allure.description("")
def test_subscribeEvent_001(get_Token_id_setup):
        method=data["subscribeEvent"][0]["Method"]
        apiurl=data["subscribeEvent"][0]["ApiUrl"]
        params=data["subscribeEvent"][0]["Params"]
        params['accessToken']=get_Token_id_setup['accessToken']

        #发送请求
        response=send_requests(method,apiurl,params=params)
        #断言
        assert response['meta']['code']==200
        assert response['meta']['message']=="操作成功"

@allure.feature("运维管理平台")
@allure.story("萤石云接口")
@allure.title("告警信息查询")
@allure.description("")
def test_consumer_messages_001(get_Token_id_setup):
        method=data["consumer_messages"][0]["Method"]
        apiurl=data["consumer_messages"][0]["ApiUrl"]
        params=data["consumer_messages"][0]["Params"]
        params['accessToken']=get_Token_id_setup['accessToken']
        params['consumerId'] = get_Token_id_setup['consumerId']

        #发送请求
        response=send_requests(method,apiurl,params=params)
        #断言
        assert response['code']=='200'
        assert response['msg']=="操作成功"

@allure.feature("运维管理平台")
@allure.story("萤石云接口")
@allure.title("录像回放")
@allure.description("")
def test_address_get_001(get_Token_id_setup):
        method=data["address_get"][0]["Method"]
        apiurl=data["address_get"][0]["ApiUrl"]
        params=data["address_get"][0]["Params"]
        params['accessToken']=get_Token_id_setup['accessToken']

        #发送请求
        response=send_requests(method,apiurl,params=params)
        #断言
        assert response['code']=='200'
        assert response['msg']=="操作成功"

@allure.feature("运维管理平台")
@allure.story("萤石云接口")
@allure.title("云录制")
@allure.description("")
def test_video_sava_001(get_Token_id_setup):
        method=data["video_sava"][0]["Method"]
        apiurl=data["video_sava"][0]["ApiUrl"]
        params=data["video_sava"][0]["Params"]
        params['accessToken']=get_Token_id_setup['accessToken']

        #发送请求
        response=send_requests(method,apiurl,params=params)
        #断言
        assert response['code']=='200'
        assert response['msg']=="操作成功"

@allure.feature("运维管理平台")
@allure.story("萤石云接口")
@allure.title("查询云录制")
@allure.description("")
def test_cloud_task_001(get_Token_id_setup):
        method=data["cloud_task"][0]["Method"]
        apiurl=data["cloud_task"][0]["ApiUrl"]
        params=data["cloud_task"][0]["Params"]
        params['accessToken']=get_Token_id_setup['accessToken']

        #发送请求
        response=send_requests(method,apiurl,params=params)
        #断言
        assert response['code']=='200'
        assert response['msg']=="操作成功"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("电梯实时监控-萤石云-capacity")
@allure.description("")
def test_device_capacity_001(get_Token_id_setup):
        method=data["device_capacity"][0]["Method"]
        apiurl=data["device_capacity"][0]["ApiUrl"]
        params=data["device_capacity"][0]["Params"]
        params['accessToken']=get_Token_id_setup['accessToken']

        #发送请求
        response=send_requests(method,apiurl,params=params)
        #断言
        assert response['code']=='200'
        assert response['msg']=="操作成功"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("电梯实时监控-萤石云-info")
@allure.description("")
def test_device_info_001(get_Token_id_setup):
        method=data["device_info"][0]["Method"]
        apiurl=data["device_info"][0]["ApiUrl"]
        params=data["device_info"][0]["Params"]
        params['accessToken']=get_Token_id_setup['accessToken']

        #发送请求
        response=send_requests(method,apiurl,params=params)
        #断言
        assert response['code']=='200'
        assert response['msg']=="操作成功"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("电梯实时监控-萤石云-ezopen")
@allure.description("")
def test_ezopen_url_001(get_Token_id_setup):
        method=data["ezopen_url"][0]["Method"]
        apiurl=data["ezopen_url"][0]["ApiUrl"]
        params=data["ezopen_url"][0]["Params"]
        params['accessToken']=get_Token_id_setup['accessToken']

        #发送请求
        response=send_requests(method,apiurl,params=params)
        #断言
        assert response['code']=='200'
        assert response['msg']=="操作成功"


if __name__=="__main__":
        pytest.main(["-s","test_ys7.py"])