import pytest
import allure
from apilist.opsApi import send_requests
from common.readYaml import ReadFileData
import logging
from common.logger import Logging

Logging()


#实例化读取配置文件的类,获取配置文件
readFileData=ReadFileData()
data=readFileData.get_data('test_data/ParamYaml','ops_pc_api.yml')

#   //以下是定义的初始化、清除方法//


#   //以下是测试用例//
@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("电梯状态统计-近7日")
@allure.description("")
def test_eleStatusDateType_001(login_start):
        Authorization =login_start
        method=data["eleStatusDateType"][0]["Method"]
        apiurl=data["eleStatusDateType"][0]["ApiUrl"]
        params=data["eleStatusDateType"][0]["Params"]
        headers=data["eleStatusDateType"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"
        assert len(response['data'])==7

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("电梯状态统计-近30日")
@allure.description("")
def test_eleStatusDateType_002(login_start):
        Authorization =login_start
        method=data["eleStatusDateType"][1]["Method"]
        apiurl=data["eleStatusDateType"][1]["ApiUrl"]
        params=data["eleStatusDateType"][1]["Params"]
        headers=data["eleStatusDateType"][1]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"
        assert len(response['data']) == 30

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("电梯状态统计-不传入参数")
@allure.description("")
def test_eleStatusDateType_003(login_start):
        Authorization =login_start
        method=data["eleStatusDateType"][2]["Method"]
        apiurl=data["eleStatusDateType"][2]["ApiUrl"]
        headers=data["eleStatusDateType"][2]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("电梯状态统计-传入错误的参数值")
@allure.description("")
def test_eleStatusDateType_004(login_start):
        Authorization =login_start
        method=data["eleStatusDateType"][3]["Method"]
        apiurl=data["eleStatusDateType"][3]["ApiUrl"]
        headers=data["eleStatusDateType"][3]["Headers"]
        params = data["eleStatusDateType"][3]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']!=0
        assert response['msg']!="success"

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("电梯不同状态数量统计-传入正确的参数值")
@allure.description("")
def test_count_001(login_start):
        Authorization =login_start
        method=data["count"][0]["Method"]
        apiurl=data["count"][0]["ApiUrl"]
        params=data["count"][0]["Params"]
        headers=data["count"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("电梯不同状态数量统计-参数值为空")
@allure.description("")
def test_count_002(login_start):
        Authorization =login_start
        method=data["count"][1]["Method"]
        apiurl=data["count"][1]["ApiUrl"]
        params=data["count"][1]["Params"]
        headers=data["count"][1]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("电梯不同状态数量统计-传入不正确的参数")
@allure.description("")
def test_count_003(login_start):
        Authorization =login_start
        method=data["count"][2]["Method"]
        apiurl=data["count"][2]["ApiUrl"]
        params=data["count"][2]["Params"]
        headers=data["count"][2]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("电梯不同状态数量统计-不传入参数")
@allure.description("")
def test_count_004(login_start):
        Authorization =login_start
        method=data["count"][3]["Method"]
        apiurl=data["count"][3]["ApiUrl"]
        headers=data["count"][3]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("设备数量及在线情况-区域传入正确的值")
@allure.description("")
def test_cdevice_count_001(login_start):
        Authorization =login_start
        method=data["device_count"][0]["Method"]
        apiurl=data["device_count"][0]["ApiUrl"]
        headers=data["device_count"][0]["Headers"]
        params = data["device_count"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("设备数量及在线情况-传入的参数值不存在")
@allure.description("")
def test_cdevice_count_002(login_start):
        Authorization =login_start
        method=data["device_count"][1]["Method"]
        apiurl=data["device_count"][1]["ApiUrl"]
        headers=data["device_count"][1]["Headers"]
        params = data["device_count"][1]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"
        assert response['data']['ectOnlineCount'] == 0
        assert response['data']['ectOfflineCount'] == 0
        assert response['data']['ipcOnlineCount'] == 0
        assert response['data']['ipcOfflineCount'] == 0
        assert response['data']['istOnlineCount'] == 0
        assert response['data']['istOfflineCount'] == 0
        assert response['data']['aiOnlineCount'] == 0
        assert response['data']['aiOfflineCount'] == 0

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("设备数量及在线情况-传入的参数值为空")
@allure.description("")
def test_cdevice_count_003(login_start):
        Authorization =login_start
        method=data["device_count"][2]["Method"]
        apiurl=data["device_count"][2]["ApiUrl"]
        headers=data["device_count"][2]["Headers"]
        params = data["device_count"][2]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code'] == 0
        assert response['msg'] == "success"
        assert response['data']['ectOnlineCount'] != 0
        assert response['data']['ipcOnlineCount'] != 0
        assert response['data']['istOnlineCount'] != 0

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("设备数量及在线情况-不传入参数")
@allure.description("")
def test_cdevice_count_004(login_start):
        Authorization =login_start
        method=data["device_count"][3]["Method"]
        apiurl=data["device_count"][3]["ApiUrl"]
        headers=data["device_count"][3]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers)
        #断言
        assert response['code'] == 0
        assert response['msg'] == "success"
        assert response['data']['ectOnlineCount'] != 0
        assert response['data']['ipcOnlineCount'] != 0
        assert response['data']['istOnlineCount'] != 0

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("故障告警数量-近7日")
@allure.description("")
def test_deviceError_count_001(login_start):
        Authorization =login_start
        method=data["deviceError_count"][0]["Method"]
        apiurl=data["deviceError_count"][0]["ApiUrl"]
        headers=data["deviceError_count"][0]["Headers"]
        params = data["deviceError_count"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code'] == 0
        assert response['msg'] == "success"

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("故障告警数量-近30日")
@allure.description("")
def test_deviceError_count_002(login_start):
        Authorization =login_start
        method=data["deviceError_count"][1]["Method"]
        apiurl=data["deviceError_count"][1]["ApiUrl"]
        headers=data["deviceError_count"][1]["Headers"]
        params = data["deviceError_count"][1]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code'] == 0
        assert response['msg'] == "success"

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("故障告警数量-传入错误的参数值")
@allure.description("")
def test_deviceError_count_003(login_start):
        Authorization =login_start
        method=data["deviceError_count"][2]["Method"]
        apiurl=data["deviceError_count"][2]["ApiUrl"]
        headers=data["deviceError_count"][2]["Headers"]
        params = data["deviceError_count"][2]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code'] != 0
        assert response['msg'] == "success"

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("故障告警数量-不传参数")
@allure.description("")
def test_deviceError_count_004(login_start):
        Authorization =login_start
        method=data["deviceError_count"][3]["Method"]
        apiurl=data["deviceError_count"][3]["ApiUrl"]
        headers=data["deviceError_count"][3]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers)
        #断言
        assert response['code'] == 0
        assert response['msg'] == "success"

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("困人报警统计-近7日")
@allure.description("")
def test_lockEvent_count_001(login_start):
        Authorization =login_start
        method=data["lockEvent_count"][0]["Method"]
        apiurl=data["lockEvent_count"][0]["ApiUrl"]
        headers=data["lockEvent_count"][0]["Headers"]
        params = data["lockEvent_count"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code'] == 0
        assert response['msg'] == "success"

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("困人报警统计-近30日")
@allure.description("")
def test_lockEvent_count_002(login_start):
        Authorization =login_start
        method=data["lockEvent_count"][1]["Method"]
        apiurl=data["lockEvent_count"][1]["ApiUrl"]
        headers=data["lockEvent_count"][1]["Headers"]
        params = data["lockEvent_count"][1]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code'] == 0
        assert response['msg'] == "success"

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("困人报警统计-传入错误的参数值")
@allure.description("")
def test_lockEvent_count_003(login_start):
        Authorization =login_start
        method=data["lockEvent_count"][2]["Method"]
        apiurl=data["lockEvent_count"][2]["ApiUrl"]
        headers=data["lockEvent_count"][2]["Headers"]
        params = data["lockEvent_count"][2]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code'] == 0
        assert response['msg'] == "success"
        assert len(response['data']) == 0

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("困人报警统计-不传参数")
@allure.description("")
def test_lockEvent_count_004(login_start):
        Authorization =login_start
        method=data["lockEvent_count"][3]["Method"]
        apiurl=data["lockEvent_count"][3]["ApiUrl"]
        headers=data["lockEvent_count"][3]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers)
        #断言
        assert response['code'] == 0
        assert response['msg'] == "success"

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("一键呼救统计-近7日")
@allure.description("")
def test_callRecord_count_001(login_start):
        Authorization =login_start
        method=data["callRecord_count"][0]["Method"]
        apiurl=data["callRecord_count"][0]["ApiUrl"]
        headers=data["callRecord_count"][0]["Headers"]
        params = data["callRecord_count"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code'] == 0
        assert response['msg'] == "success"

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("一键呼救统计-近30日")
@allure.description("")
def test_callRecord_count_002(login_start):
        Authorization =login_start
        method=data["callRecord_count"][1]["Method"]
        apiurl=data["callRecord_count"][1]["ApiUrl"]
        headers=data["callRecord_count"][1]["Headers"]
        params = data["callRecord_count"][1]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code'] == 0
        assert response['msg'] == "success"

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("一键呼救统计-传入错误的参数值")
@allure.description("")
def test_callRecord_count_003(login_start):
        Authorization =login_start
        method=data["callRecord_count"][2]["Method"]
        apiurl=data["callRecord_count"][2]["ApiUrl"]
        headers=data["callRecord_count"][2]["Headers"]
        params = data["callRecord_count"][2]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code'] == 0
        assert response['msg'] == "success"
        assert len(response['data']) == 0

@allure.feature("运维管理平台")
@allure.story("首页")
@allure.title("一键呼救统计-不传参数")
@allure.description("")
def test_callRecord_count_004(login_start):
        Authorization =login_start
        method=data["callRecord_count"][3]["Method"]
        apiurl=data["callRecord_count"][3]["ApiUrl"]
        headers=data["callRecord_count"][3]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers)
        #断言
        assert response['code'] == 0
        assert response['msg'] == "success"


if __name__ == "__main__":
    pytest.main(["-s","-v","test_homePage.py"])
    # pytest.main(["-s","test_accesskey.py::test_getAccesskey_001("])
