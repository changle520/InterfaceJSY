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

#   //以下是测试用例//
@allure.feature("运维管理平台")
@allure.story("日志管理")
@allure.title("操作日志列表")
@allure.description("")
def test_pc_log_list_001(login_start):
        Authorization =login_start
        method=data["pc_log_list"][0]["Method"]
        apiurl=data["pc_log_list"][0]["ApiUrl"]
        params=data["pc_log_list"][0]["Params"]
        headers=data["pc_log_list"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("日志管理")
@allure.title("操作日志列表-失败")
@allure.description("")
def test_pc_log_list_002(login_start):
        Authorization =login_start
        method=data["pc_log_list"][1]["Method"]
        apiurl=data["pc_log_list"][1]["ApiUrl"]
        params=data["pc_log_list"][1]["Params"]
        headers=data["pc_log_list"][1]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"
        assert response['data']['content'][0]['status']=="失败"


@allure.feature("运维管理平台")
@allure.story("日志管理")
@allure.title("操作日志列表-成功")
@allure.description("")
def test_pc_log_list_003(login_start):
        Authorization =login_start
        method=data["pc_log_list"][2]["Method"]
        apiurl=data["pc_log_list"][2]["ApiUrl"]
        params=data["pc_log_list"][2]["Params"]
        headers=data["pc_log_list"][2]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"
        assert response['data']['content'][0]['status']=="成功"


@allure.feature("运维管理平台")
@allure.story("日志管理")
@allure.title("日志菜单模块列表")
@allure.description("")
def test_pc_module_list_001(login_start):
        Authorization =login_start
        method=data["pc_module_list"][0]["Method"]
        apiurl=data["pc_module_list"][0]["ApiUrl"]
        headers=data["pc_module_list"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("日志管理")
@allure.title("指令消息日志列表")
@allure.description("")
def test_message_list_001(login_start):
        Authorization =login_start
        method=data["message_list"][0]["Method"]
        apiurl=data["message_list"][0]["ApiUrl"]
        params=data["message_list"][0]["Params"]
        headers=data["message_list"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("日志管理")
@allure.title("指令消息日志列表-操作失败")
@allure.description("")
def test_message_list_002(login_start):
        Authorization =login_start
        method=data["message_list"][1]["Method"]
        apiurl=data["message_list"][1]["ApiUrl"]
        params=data["message_list"][1]["Params"]
        headers=data["message_list"][1]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("日志管理")
@allure.title("指令消息日志列表-操作成功")
@allure.description("")
def test_message_list_003(login_start):
        Authorization =login_start
        method=data["message_list"][2]["Method"]
        apiurl=data["message_list"][2]["ApiUrl"]
        params=data["message_list"][2]["Params"]
        headers=data["message_list"][2]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("日志管理")
@allure.title("指令消息日志列表-梯联终端")
@allure.description("")
def test_message_list_004(login_start):
        Authorization =login_start
        method=data["message_list"][3]["Method"]
        apiurl=data["message_list"][3]["ApiUrl"]
        params=data["message_list"][3]["Params"]
        headers=data["message_list"][3]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("日志管理")
@allure.title("指令消息日志列表-视频监测终端")
@allure.description("")
def test_message_list_005(login_start):
        Authorization =login_start
        method=data["message_list"][4]["Method"]
        apiurl=data["message_list"][4]["ApiUrl"]
        params=data["message_list"][4]["Params"]
        headers=data["message_list"][4]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("日志管理")
@allure.title("指令消息日志列表-智能屏显终端")
@allure.description("")
def test_message_list_006(login_start):
        Authorization =login_start
        method=data["message_list"][5]["Method"]
        apiurl=data["message_list"][5]["ApiUrl"]
        params=data["message_list"][5]["Params"]
        headers=data["message_list"][5]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("日志管理")
@allure.title("设备上下线日志列表")
@allure.description("")
def test_device_offline_record_list_001(login_start):
        Authorization =login_start
        method=data["device_offline_record_list"][0]["Method"]
        apiurl=data["device_offline_record_list"][0]["ApiUrl"]
        params=data["device_offline_record_list"][0]["Params"]
        headers=data["device_offline_record_list"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("日志管理")
@allure.title("设备上下线日志列表-梯联终端")
@allure.description("")
def test_device_offline_record_list_002(login_start):
        Authorization =login_start
        method=data["device_offline_record_list"][1]["Method"]
        apiurl=data["device_offline_record_list"][1]["ApiUrl"]
        params=data["device_offline_record_list"][1]["Params"]
        headers=data["device_offline_record_list"][1]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("日志管理")
@allure.title("设备上下线日志列表-智能屏显终端")
@allure.description("")
def test_device_offline_record_list_003(login_start):
        Authorization =login_start
        method=data["device_offline_record_list"][3]["Method"]
        apiurl=data["device_offline_record_list"][3]["ApiUrl"]
        params=data["device_offline_record_list"][3]["Params"]
        headers=data["device_offline_record_list"][3]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("日志管理")
@allure.title("频繁掉线列表")
@allure.description("")
def test_frequent_offline_list_001(login_start):
        Authorization =login_start
        method=data["frequent_offline_list"][0]["Method"]
        apiurl=data["frequent_offline_list"][0]["ApiUrl"]
        params=data["frequent_offline_list"][0]["Params"]
        headers=data["frequent_offline_list"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("日志管理")
@allure.title("频繁掉线列表导出")
@allure.description("")
def test_frequent_offline_export_001(login_start):
        Authorization =login_start
        method=data["frequent_offline_export"][0]["Method"]
        apiurl=data["frequent_offline_export"][0]["ApiUrl"]
        params=data["frequent_offline_export"][0]["Params"]
        headers=data["frequent_offline_export"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("日志管理")
@allure.title("离线统计列表")
@allure.description("")
def test_offline_device_list_001(login_start):
        Authorization =login_start
        method=data["offline_device_list"][0]["Method"]
        apiurl=data["offline_device_list"][0]["ApiUrl"]
        params=data["offline_device_list"][0]["Params"]
        headers=data["offline_device_list"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("日志管理")
@allure.title("离线统计导出")
@allure.description("")
def test_offline_device_export_001(login_start):
        Authorization =login_start
        method=data["offline_device_export"][0]["Method"]
        apiurl=data["offline_device_export"][0]["ApiUrl"]
        params=data["offline_device_export"][0]["Params"]
        headers=data["offline_device_export"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

if __name__ == "__main__":
    pytest.main(["-s","-v","test_logManage.py"])