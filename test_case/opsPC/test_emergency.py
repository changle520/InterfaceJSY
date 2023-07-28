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
@pytest.fixture(scope='function',autouse=False)
def get_elevator_call_recordId_setup(login_start):
        '''获取一键呼救记录ID'''
        Authorization = login_start
        method = data["elevator_call_record_list"][0]["Method"]
        apiurl = data["elevator_call_record_list"][0]["ApiUrl"]
        params = data["elevator_call_record_list"][0]["Params"]
        headers = data["elevator_call_record_list"][0]["Headers"]
        headers.update(Authorization)
        response = send_requests(method, apiurl, headers=headers, params=params)
        id=response['data']['content'][0]['recordId']
        return id
@pytest.fixture(scope='function',autouse=False)
def get_elevatorId_setup(login_start):
        '''获取电梯的id'''
        Authorization = login_start
        method = data["device_error_trapped_list"][0]["Method"]
        apiurl = data["device_error_trapped_list"][0]["ApiUrl"]
        params = data["device_error_trapped_list"][0]["Params"]
        headers = data["device_error_trapped_list"][0]["Headers"]
        headers.update(Authorization)
        response = send_requests(method, apiurl, headers=headers, params=params)
        elevatorId=response['data']['content'][0]['elevatorId']
        id=response['data']['content'][0]['id']
        return {"id":id,"elevatorId":elevatorId}




#   //以下是测试用例//
@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("一键呼救列表")
@allure.description("")
def test_elevator_call_record_list_001(login_start):
        Authorization =login_start
        method=data["elevator_call_record_list"][0]["Method"]
        apiurl=data["elevator_call_record_list"][0]["ApiUrl"]
        params=data["elevator_call_record_list"][0]["Params"]
        headers=data["elevator_call_record_list"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("一键呼救列表-通话结束")
@allure.description("")
def test_elevator_call_record_list_002(login_start):
        Authorization =login_start
        method=data["elevator_call_record_list"][1]["Method"]
        apiurl=data["elevator_call_record_list"][1]["ApiUrl"]
        params=data["elevator_call_record_list"][1]["Params"]
        headers=data["elevator_call_record_list"][1]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("一键呼救列表-平台未接听")
@allure.description("")
def test_elevator_call_record_list_003(login_start):
        Authorization =login_start
        method=data["elevator_call_record_list"][2]["Method"]
        apiurl=data["elevator_call_record_list"][2]["ApiUrl"]
        params=data["elevator_call_record_list"][2]["Params"]
        headers=data["elevator_call_record_list"][2]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("一键呼救列表-不传参数")
@allure.description("")
def test_elevator_call_record_list_004(login_start):
        Authorization =login_start
        method=data["elevator_call_record_list"][3]["Method"]
        apiurl=data["elevator_call_record_list"][3]["ApiUrl"]
        headers=data["elevator_call_record_list"][3]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("一键呼救列表导出")
@allure.description("")
def test_elevator_call_record_export_001(login_start):
        Authorization =login_start
        method=data["elevator_call_record_export"][0]["Method"]
        apiurl=data["elevator_call_record_export"][0]["ApiUrl"]
        params=data["elevator_call_record_export"][0]["Params"]
        headers=data["elevator_call_record_export"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("一键呼救通话记录获取")
@allure.description("")
def test_elevator_call_record_info_001(login_start,get_elevator_call_recordId_setup):
        Authorization =login_start
        method=data["elevator_call_record_info"][0]["Method"]
        apiurl=data["elevator_call_record_info"][0]["ApiUrl"]
        headers=data["elevator_call_record_info"][0]["Headers"]

        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        recordid=get_elevator_call_recordId_setup
        response=send_requests(method,apiurl,headers=headers,appendurl=recordid)
        #断言
        assert response['code']==0
        assert response['msg']=="success"
        assert response['data']['recordId']== recordid

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("困人处置列表")
@allure.description("")
def test_device_error_trapped_list_001(login_start):
        Authorization =login_start
        method=data["device_error_trapped_list"][0]["Method"]
        apiurl=data["device_error_trapped_list"][0]["ApiUrl"]
        headers=data["device_error_trapped_list"][0]["Headers"]
        params=data["device_error_trapped_list"][0]["Params"]

        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        recordid=get_elevator_call_recordId_setup
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("困人处置列表-待处理")
@allure.description("")
def test_device_error_trapped_list_002(login_start):
        Authorization =login_start
        method=data["device_error_trapped_list"][1]["Method"]
        apiurl=data["device_error_trapped_list"][1]["ApiUrl"]
        headers=data["device_error_trapped_list"][1]["Headers"]
        params=data["device_error_trapped_list"][1]["Params"]

        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        recordid=get_elevator_call_recordId_setup
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"
        assert response['data']['content'][0]['dealRemark'] == ""

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("困人处置列表-真实")
@allure.description("")
def test_device_error_trapped_list_003(login_start):
        Authorization =login_start
        method=data["device_error_trapped_list"][2]["Method"]
        apiurl=data["device_error_trapped_list"][2]["ApiUrl"]
        headers=data["device_error_trapped_list"][2]["Headers"]
        params=data["device_error_trapped_list"][2]["Params"]

        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        recordid=get_elevator_call_recordId_setup
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"
        assert response['data']['content'][0]['dealRemark'] == "真实"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("困人处置列表-误报")
@allure.description("")
def test_device_error_trapped_list_004(login_start):
        Authorization =login_start
        method=data["device_error_trapped_list"][3]["Method"]
        apiurl=data["device_error_trapped_list"][3]["ApiUrl"]
        headers=data["device_error_trapped_list"][3]["Headers"]
        params=data["device_error_trapped_list"][3]["Params"]

        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        recordid=get_elevator_call_recordId_setup
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"
        assert response['data']['content'][0]['dealRemark'] == "误报"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("困人处置列表-平层区域外困人")
@allure.description("")
def test_device_error_trapped_list_005(login_start):
        Authorization =login_start
        method=data["device_error_trapped_list"][4]["Method"]
        apiurl=data["device_error_trapped_list"][4]["ApiUrl"]
        headers=data["device_error_trapped_list"][4]["Headers"]
        params=data["device_error_trapped_list"][4]["Params"]

        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        recordid=get_elevator_call_recordId_setup
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"
        assert response['data']['content'][0]['lockEventTypeLabel'] == "平层外区域困人"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("困人处置列表-平层区域内困人")
@allure.description("")
def test_device_error_trapped_list_006(login_start):
        Authorization =login_start
        method=data["device_error_trapped_list"][5]["Method"]
        apiurl=data["device_error_trapped_list"][5]["ApiUrl"]
        headers=data["device_error_trapped_list"][5]["Headers"]
        params=data["device_error_trapped_list"][5]["Params"]

        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        recordid=get_elevator_call_recordId_setup
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"
        assert response['data']['content'][0]['lockEventTypeLabel'] == "平层内区域困人"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("困人处置列表-区域外困人")
@allure.description("")
def test_device_error_trapped_list_007(login_start):
        Authorization =login_start
        method=data["device_error_trapped_list"][6]["Method"]
        apiurl=data["device_error_trapped_list"][6]["ApiUrl"]
        headers=data["device_error_trapped_list"][6]["Headers"]
        params=data["device_error_trapped_list"][6]["Params"]

        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        recordid=get_elevator_call_recordId_setup
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"
        assert response['data']['content'][0]['lockEventTypeLabel'] == "区域外困人"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("困人处置列表-未知")
@allure.description("")
def test_device_error_trapped_list_008(login_start):
        Authorization =login_start
        method=data["device_error_trapped_list"][7]["Method"]
        apiurl=data["device_error_trapped_list"][7]["ApiUrl"]
        headers=data["device_error_trapped_list"][7]["Headers"]
        params=data["device_error_trapped_list"][7]["Params"]

        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        recordid=get_elevator_call_recordId_setup
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"
        assert response['data']['content'][0]['lockEventTypeLabel'] == "未知"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("困人处置列表导出")
@allure.description("")
def test_device_error_trapped_export_001(login_start):
        Authorization =login_start
        method=data["device_error_trapped_export"][0]["Method"]
        apiurl=data["device_error_trapped_export"][0]["ApiUrl"]
        headers=data["device_error_trapped_export"][0]["Headers"]
        params=data["device_error_trapped_export"][0]["Params"]

        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        recordid=get_elevator_call_recordId_setup
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("困人事件标记真实")
@allure.description("")
def test_update_deal_status_send_sms_001(login_start,get_elevatorId_setup):
        Authorization =login_start
        method=data["update_deal_status_send_sms"][0]["Method"]
        apiurl=data["update_deal_status_send_sms"][0]["ApiUrl"]
        headers=data["update_deal_status_send_sms"][0]["Headers"]
        params=data["update_deal_status_send_sms"][0]["Params"]
        params['id']=get_elevatorId_setup['id']
        params['elevatorId']=get_elevatorId_setup['elevatorId']

        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        recordid=get_elevator_call_recordId_setup
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("困人事件标记误报")
@allure.description("")
def test_update_deal_status_false_alarm_001(login_start,get_elevatorId_setup):
        Authorization =login_start
        method=data["update_deal_status_false_alarm"][0]["Method"]
        apiurl=data["update_deal_status_false_alarm"][0]["ApiUrl"]
        headers=data["update_deal_status_false_alarm"][0]["Headers"]
        params=data["update_deal_status_false_alarm"][0]["Params"]
        params['ids']=get_elevatorId_setup['id']
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        recordid=get_elevator_call_recordId_setup
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("困人事件回放")
@allure.description("")
def test_device_error_trapped_video_replay_001(login_start,get_elevatorId_setup):
        Authorization =login_start
        method=data["device_error_trapped_video_replay"][0]["Method"]
        apiurl=data["device_error_trapped_video_replay"][0]["ApiUrl"]
        headers=data["device_error_trapped_video_replay"][0]["Headers"]
        params=data["device_error_trapped_video_replay"][0]["Params"]
        params['id']=get_elevatorId_setup['id']
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        recordid=get_elevator_call_recordId_setup
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"
        assert response['data']['cloudUrl'] !=''

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("应急值班人员列表")
@allure.description("")
def test_watch_stander_person_list_001(login_start):
        Authorization =login_start
        method=data["watch_stander_person_list"][0]["Method"]
        apiurl=data["watch_stander_person_list"][0]["ApiUrl"]
        headers=data["watch_stander_person_list"][0]["Headers"]

        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        recordid=get_elevator_call_recordId_setup
        response=send_requests(method,apiurl,headers=headers)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("周一到周日对应的应急值班人员")
@allure.description("")
def test_watch_stander_info_001(login_start):
        Authorization =login_start
        method=data["watch_stander_info"][0]["Method"]
        apiurl=data["watch_stander_info"][0]["ApiUrl"]
        headers=data["watch_stander_info"][0]["Headers"]
        params = data["watch_stander_info"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        recordid=get_elevator_call_recordId_setup
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("应急处置")
@allure.title("新增或编辑应急值班人员")
@allure.description("")
def test_watch_stander_save_001(login_start):
        Authorization =login_start
        method=data["watch_stander_save"][0]["Method"]
        apiurl=data["watch_stander_save"][0]["ApiUrl"]
        headers=data["watch_stander_save"][0]["Headers"]
        params = data["watch_stander_save"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        recordid=get_elevator_call_recordId_setup
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

if __name__ == "__main__":
    pytest.main(["-s","-v","test_emergency.py"])
