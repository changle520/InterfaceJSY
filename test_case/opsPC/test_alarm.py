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
@allure.story("应急处置")
@allure.title("事件告警类型")
@allure.description("")
def test_alarm_event_type_001(login_start):
        Authorization =login_start
        method=data["alarm_event_type"][0]["Method"]
        apiurl=data["alarm_event_type"][0]["ApiUrl"]
        params=data["alarm_event_type"][0]["Params"]
        headers=data["alarm_event_type"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"
        assert response['data'][0]['name']=="反复开关门"
        assert response['data'][1]['name']=="长时间挡门"
        assert response['data'][2]['name']=="电动车入梯"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("事件告警列表查询")
@allure.description("")
def test_alarm_event_list_001(login_start):
        Authorization =login_start
        method=data["alarm_event_list"][0]["Method"]
        apiurl=data["alarm_event_list"][0]["ApiUrl"]
        params=data["alarm_event_list"][0]["Params"]
        headers=data["alarm_event_list"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("事件告警记录导出")
@allure.description("")
def test_alarm_event_list_export_001(login_start):
        Authorization =login_start
        method=data["alarm_event_list_export"][0]["Method"]
        apiurl=data["alarm_event_list_export"][0]["ApiUrl"]
        params=data["alarm_event_list_export"][0]["Params"]
        headers=data["alarm_event_list_export"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("故障告警类型")
@allure.description("")
def test_alarm_fault_type_001(login_start):
        Authorization =login_start
        method=data["alarm_fault_type"][0]["Method"]
        apiurl=data["alarm_fault_type"][0]["ApiUrl"]
        params=data["alarm_fault_type"][0]["Params"]
        headers=data["alarm_fault_type"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("故障告警列表")
@allure.description("")
def test_alarm_fault_list_001(login_start):
        Authorization =login_start
        method=data["alarm_fault_list"][0]["Method"]
        apiurl=data["alarm_fault_list"][0]["ApiUrl"]
        params=data["alarm_fault_list"][0]["Params"]
        headers=data["alarm_fault_list"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("故障告警导出-大于5万条")
@allure.description("")
def test_alarm_fault_export_001(login_start):
        Authorization =login_start
        method=data["alarm_fault_export"][0]["Method"]
        apiurl=data["alarm_fault_export"][0]["ApiUrl"]
        params=data["alarm_fault_export"][0]["Params"]
        headers=data["alarm_fault_export"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==555
        assert response['msg']=='用户单次导出最多5万条'

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("故障告警导出-小于5万条")
@allure.description("")
def test_alarm_fault_export_002(login_start):
        Authorization =login_start
        method=data["alarm_fault_export"][1]["Method"]
        apiurl=data["alarm_fault_export"][1]["ApiUrl"]
        params=data["alarm_fault_export"][1]["Params"]
        headers=data["alarm_fault_export"][1]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=='success'


if __name__=="__main__":
        pytest.main(["-s","-v","test_alarm.py"])