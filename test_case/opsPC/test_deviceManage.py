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
'''
模块文件的初始化、清除方法
'''
@pytest.fixture(scope="module",autouse=True)
def device_version_add_setup(login_start):
        print("执行初始化操作:新增产品型号")
        #新增一个产品型号
        Authorization =login_start
        method=data["product_model_add"][1]["Method"]
        apiurl=data["product_model_add"][1]["ApiUrl"]
        headers=data["product_model_add"][1]["Headers"]
        params=data["product_model_add"][1]["Params"]
        headers.update(Authorization)
        response=send_requests(method,apiurl,headers=headers,data=params)

        yield
        device_version_add_teardown_module(login_start)


def device_version_add_teardown_module(login_start):
        print("执行清除化操作:删除产品型号")
        Authorization = login_start
        #查看产品型号获取id
        method = data["product_model_list"][0]["Method"]
        apiurl = data["product_model_list"][0]["ApiUrl"]
        headers = data["product_model_list"][0]["Headers"]
        params = data["product_model_list"][0]["Params"]
        headers.update(Authorization)
        response = send_requests(method, apiurl, headers=headers, data=params)
        id=response['data']['content'][0]['id']

        #删除产品型号
        method=data["product_model_del"][0]["Method"]
        apiurl=data["product_model_del"][0]["ApiUrl"]
        headers=data["product_model_del"][0]["Headers"]
        headers.update(Authorization)
        response=send_requests(method,apiurl,headers=headers,appendurl=id)

'''
测试用例的相关初始化、清除方法
'''
def device_version_add_teardown(login_start):
        print("执行清除操作：删除产品的固件版本")
        Authorization = login_start
        #查看固件版本列表，获取id
        method = data["device_version_list"][0]["Method"]
        apiurl = data["device_version_list"][0]["ApiUrl"]
        headers = data["device_version_list"][0]["Headers"]
        params = data["device_version_list"][0]["Params"]
        headers.update(Authorization)
        response = send_requests(method, apiurl, headers=headers, params=params)
        id=response['data']['content'][0]['id']

        #删除固件版本
        method=data["device_version_del"][0]["Method"]
        apiurl=data["device_version_del"][0]["ApiUrl"]
        headers=data["device_version_del"][0]["Headers"]
        headers.update(Authorization)
        response=send_requests(method,apiurl,headers=headers,appendurl=id)

@pytest.fixture(scope="function",autouse=False)
def device_version_update_setup(login_start):
        print("执行初始化操作：新增一个固件版本")
        Authorization =login_start
        #新增一个产品的固件版本
        method=data["device_version_add"][0]["Method"]
        apiurl=data["device_version_add"][0]["ApiUrl"]
        headers=data["device_version_add"][0]["Headers"]
        params=data["device_version_add"][0]["Params"]
        params['productModel']=data['product_model_add'][1]['Params']['productModel']
        headers.update(Authorization)
        send_requests(method,apiurl,headers=headers,data=params)

        #查看固件版本列表，获取id、productModel
        method = data["device_version_list"][0]["Method"]
        apiurl = data["device_version_list"][0]["ApiUrl"]
        headers = data["device_version_list"][0]["Headers"]
        params = data["device_version_list"][0]["Params"]
        headers.update(Authorization)
        response = send_requests(method, apiurl, headers=headers, params=params)
        id=response['data']['content'][0]['id']
        productModel=response['data']['content'][0]['productModel']
        return {"id":id,"productModel":productModel}


@pytest.fixture(scope="function",autouse=False)
def productModel_add_setup(login_start):
        print("执行初始化操作")
        yield
        print("执行增加产品型号的清除操作：删除产品型号")
        productModel_add_teardown(login_start)
def productModel_add_teardown(login_start):
        print("执行清除操作：删除产品型号")
        Authorization = login_start
        #查看产品型号列表，获取id
        method = data["product_model_list"][0]["Method"]
        apiurl = data["product_model_list"][0]["ApiUrl"]
        headers = data["product_model_list"][0]["Headers"]
        params = data["product_model_list"][0]["Params"]
        headers.update(Authorization)
        response = send_requests(method, apiurl, headers=headers, data=params)
        id=response['data']['content'][0]['id']

        #删除产品型号
        method=data["product_model_del"][0]["Method"]
        apiurl=data["product_model_del"][0]["ApiUrl"]
        headers=data["product_model_del"][0]["Headers"]
        headers.update(Authorization)
        send_requests(method,apiurl,headers=headers,appendurl=id)

@pytest.fixture(scope="function",autouse=False)
def productModel_update_setup(login_start):
        print("执行初始化操作：新增产品型号")
        #新增一个产品型号
        Authorization =login_start
        method=data["product_model_add"][0]["Method"]
        apiurl=data["product_model_add"][0]["ApiUrl"]
        headers=data["product_model_add"][0]["Headers"]
        params=data["product_model_add"][0]["Params"]
        headers.update(Authorization)
        response=send_requests(method,apiurl,headers=headers,data=params)

        #查看产品型号获取id
        method = data["product_model_list"][0]["Method"]
        apiurl = data["product_model_list"][0]["ApiUrl"]
        headers = data["product_model_list"][0]["Headers"]
        params = data["product_model_list"][0]["Params"]
        headers.update(Authorization)
        response = send_requests(method, apiurl, headers=headers, data=params)
        id=response['data']['content'][0]['id']
        return id

#   //以下是测试用例//
@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("检修工单查询-普通工单")
@allure.description("")
def test_overhaul_work_order_001(login_start):
        Authorization =login_start
        method=data["overhaul_work_order"][0]["Method"]
        apiurl=data["overhaul_work_order"][0]["ApiUrl"]
        params=data["overhaul_work_order"][0]["Params"]
        headers=data["overhaul_work_order"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("检修工单查询-加急工单")
@allure.description("")
def test_overhaul_work_order_002(login_start):
        Authorization =login_start
        method=data["overhaul_work_order"][1]["Method"]
        apiurl=data["overhaul_work_order"][1]["ApiUrl"]
        params=data["overhaul_work_order"][1]["Params"]
        headers=data["overhaul_work_order"][1]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("检修工单查询-特急工单")
@allure.description("")
def test_overhaul_work_order_003(login_start):
        Authorization =login_start
        method=data["overhaul_work_order"][2]["Method"]
        apiurl=data["overhaul_work_order"][2]["ApiUrl"]
        params=data["overhaul_work_order"][2]["Params"]
        headers=data["overhaul_work_order"][2]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("派遣人员查询")
@allure.description("")
def test_overhaul_work_order_person_001(login_start):
        Authorization =login_start
        method=data["overhaul_work_order_person"][0]["Method"]
        apiurl=data["overhaul_work_order_person"][0]["ApiUrl"]
        params=data["overhaul_work_order_person"][0]["Params"]
        headers=data["overhaul_work_order_person"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("关闭工单")
@allure.description("")
def test_overhaul_work_order_close_001(login_start):
        Authorization =login_start
        method=data["overhaul_work_order_close"][0]["Method"]
        apiurl=data["overhaul_work_order_close"][0]["ApiUrl"]
        params=data["overhaul_work_order_close"][0]["Params"]
        headers=data["overhaul_work_order_close"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']!=0

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("查看检修工单详情")
@allure.description("")
def test_overhaul_work_order_info_001(login_start):
        Authorization =login_start
        method=data["overhaul_work_order_info"][0]["Method"]
        apiurl=data["overhaul_work_order_info"][0]["ApiUrl"]
        headers=data["overhaul_work_order_info"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers)
        #断言
        assert response['code']==0
        assert response['msg']=="success"


@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("编辑检修工单")
@allure.description("")
def test_overhaul_work_order_update_001(login_start):
        Authorization =login_start
        method=data["overhaul_work_order_update"][0]["Method"]
        apiurl=data["overhaul_work_order_update"][0]["ApiUrl"]
        params=data["overhaul_work_order_update"][0]["Params"]
        headers=data["overhaul_work_order_update"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("梯联设备升级")
@allure.description("")
def test_deviceEct_upgrade_001(login_start):
        Authorization =login_start
        method=data["deviceEct_upgrade"][0]["Method"]
        apiurl=data["deviceEct_upgrade"][0]["ApiUrl"]
        params=data["deviceEct_upgrade"][0]["Params"]
        headers=data["deviceEct_upgrade"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("梯联设备广播升级")
@allure.description("")
def test_deviceEct_broadcast_001(login_start):
        Authorization =login_start
        method=data["deviceEct_broadcast"][0]["Method"]
        apiurl=data["deviceEct_broadcast"][0]["ApiUrl"]
        params=data["deviceEct_broadcast"][0]["Params"]
        headers=data["deviceEct_broadcast"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("梯联终端列表升级")
@allure.description("")
def test_deviceEct_list_001(login_start):
        Authorization =login_start
        method=data["deviceEct_list"][0]["Method"]
        apiurl=data["deviceEct_list"][0]["ApiUrl"]
        params=data["deviceEct_list"][0]["Params"]
        headers=data["deviceEct_list"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"


@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("梯联终端设备修改")
@allure.description("")
def test_deviceEct_update_001(login_start):
        Authorization =login_start
        method=data["deviceEct_update"][0]["Method"]
        apiurl=data["deviceEct_update"][0]["ApiUrl"]
        params=data["deviceEct_update"][0]["Params"]
        headers=data["deviceEct_list"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("设备解绑")
@allure.description("")
def test_device_bind_delete_001(login_start):
        Authorization =login_start
        method=data["device_bind_delete"][0]["Method"]
        apiurl=data["device_bind_delete"][0]["ApiUrl"]
        params=data["device_bind_delete"][0]["Params"]
        headers=data["device_bind_delete"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("设备日志")
@allure.description("")
def test_device_message_001(login_start):
        Authorization =login_start
        method=data["device_message"][0]["Method"]
        apiurl=data["device_message"][0]["ApiUrl"]
        params=data["device_message"][0]["Params"]
        headers=data["device_message"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("查看设备详情")
@allure.description("")
def test_deviceEct_info_001(login_start):
        Authorization =login_start
        method=data["deviceEct_info"][0]["Method"]
        apiurl=data["deviceEct_info"][0]["ApiUrl"]
        headers=data["deviceEct_info"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("梯联设备重启")
@allure.description("")
def test_deviceEct_restart_001(login_start):
        Authorization =login_start
        method=data["deviceEct_restart"][0]["Method"]
        apiurl=data["deviceEct_restart"][0]["ApiUrl"]
        headers=data["deviceEct_restart"][0]["Headers"]
        params=data["deviceEct_restart"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("检测参数配置")
@allure.description("")
def test_deviceEct_judge_param_001(login_start):
        Authorization =login_start
        method=data["deviceEct_judge_param"][0]["Method"]
        apiurl=data["deviceEct_judge_param"][0]["ApiUrl"]
        headers=data["deviceEct_judge_param"][0]["Headers"]
        params=data["deviceEct_judge_param"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("视频监测终端列表")
@allure.description("")
def test_deviceIpc_list_001(login_start):
        Authorization =login_start
        method=data["deviceIpc_list"][0]["Method"]
        apiurl=data["deviceIpc_list"][0]["ApiUrl"]
        headers=data["deviceIpc_list"][0]["Headers"]
        params=data["deviceIpc_list"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("视频监测终端：修改布防撤防状态-布防")
@allure.description("")
def test_update_defence_001(login_start):
        Authorization =login_start
        method=data["update_defence"][0]["Method"]
        apiurl=data["update_defence"][0]["ApiUrl"]
        headers=data["update_defence"][0]["Headers"]
        params=data["update_defence"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("视频监测终端：修改布防撤防状态-撤防")
@allure.description("")
def test_update_defence_001(login_start):
        Authorization =login_start
        method=data["update_defence"][0]["Method"]
        apiurl=data["update_defence"][0]["ApiUrl"]
        headers=data["update_defence"][0]["Headers"]
        params=data["update_defence"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("视频监测终端：批量布防")
@allure.description("")
def test_batch_defence_001(login_start):
        Authorization =login_start
        method=data["batch_defence"][0]["Method"]
        apiurl=data["batch_defence"][0]["ApiUrl"]
        headers=data["batch_defence"][0]["Headers"]
        params=data["batch_defence"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("视频监测终端：批量撤防")
@allure.description("")
def test_batch_cancel_defence_001(login_start):
        Authorization =login_start
        method=data["batch_cancel_defence"][0]["Method"]
        apiurl=data["batch_cancel_defence"][0]["ApiUrl"]
        headers=data["batch_cancel_defence"][0]["Headers"]
        params=data["batch_cancel_defence"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("视频监测终端：广播升级")
@allure.description("")
def test_deviceIst_upgrade_broadcast_001(login_start):
        Authorization =login_start
        method=data["deviceIst_upgrade_broadcast"][0]["Method"]
        apiurl=data["deviceIst_upgrade_broadcast"][0]["ApiUrl"]
        headers=data["deviceIst_upgrade_broadcast"][0]["Headers"]
        params=data["deviceIst_upgrade_broadcast"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("视频监测终端：智能屏升级")
@allure.description("")
def test_deviceIst_upgrade_001(login_start):
        Authorization =login_start
        method=data["deviceIst_upgrade"][0]["Method"]
        apiurl=data["deviceIst_upgrade"][0]["ApiUrl"]
        headers=data["deviceIst_upgrade"][0]["Headers"]
        params=data["deviceIst_upgrade"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("视频监测终端：智能屏重启")
@allure.description("")
def test_deviceIst_restart_001(login_start):
        Authorization =login_start
        method=data["deviceIst_restart"][0]["Method"]
        apiurl=data["deviceIst_restart"][0]["ApiUrl"]
        headers=data["deviceIst_restart"][0]["Headers"]
        params=data["deviceIst_restart"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("视频监测终端：熄屏设置")
@allure.description("")
def test_deviceIst_sleep_001(login_start):
        Authorization =login_start
        method=data["deviceIst_sleep"][0]["Method"]
        apiurl=data["deviceIst_sleep"][0]["ApiUrl"]
        headers=data["deviceIst_sleep"][0]["Headers"]
        params=data["deviceIst_sleep"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("视频监测终端：定时音量设置")
@allure.description("")
def test_deviceIst_voice_config_001(login_start):
        Authorization =login_start
        method=data["deviceIst_voice_config"][0]["Method"]
        apiurl=data["deviceIst_voice_config"][0]["ApiUrl"]
        headers=data["deviceIst_voice_config"][0]["Headers"]
        params=data["deviceIst_voice_config"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("视频监测终端：电话设置")
@allure.description("")
def test_deviceIst_phone_config_001(login_start):
        Authorization =login_start
        method=data["deviceIst_phone_config"][0]["Method"]
        apiurl=data["deviceIst_phone_config"][0]["ApiUrl"]
        headers=data["deviceIst_phone_config"][0]["Headers"]
        params=data["deviceIst_phone_config"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("视频监测终端：设备解绑")
@allure.description("")
def test_elevator_device_bind_delete_001(login_start):
        Authorization =login_start
        method=data["elevator_device_bind_delete"][0]["Method"]
        apiurl=data["elevator_device_bind_delete"][0]["ApiUrl"]
        headers=data["elevator_device_bind_delete"][0]["Headers"]
        params=data["elevator_device_bind_delete"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("视频监测终端：智能屏列表")
@allure.description("")
def test_deviceIst_list_001(login_start):
        Authorization =login_start
        method=data["deviceIst_list"][0]["Method"]
        apiurl=data["deviceIst_list"][0]["ApiUrl"]
        headers=data["deviceIst_list"][0]["Headers"]
        params=data["deviceIst_list"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("视频监测终端：日志下载")
@allure.description("")
def test_deviceIst_log_download_001(login_start):
        Authorization =login_start
        method=data["deviceIst_log_download"][0]["Method"]
        apiurl=data["deviceIst_log_download"][0]["ApiUrl"]
        headers=data["deviceIst_log_download"][0]["Headers"]
        params=data["deviceIst_log_download"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("视频监测终端：设备日志列表")
@allure.description("")
def test_log_list_001(login_start):
        Authorization =login_start
        method=data["log_list"][0]["Method"]
        apiurl=data["log_list"][0]["ApiUrl"]
        headers=data["log_list"][0]["Headers"]
        params=data["log_list"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("直梯管理-小区树状图")
@allure.description("")
def test_region_tree_001(login_start):
        Authorization =login_start
        method=data["region_tree"][0]["Method"]
        apiurl=data["region_tree"][0]["ApiUrl"]
        headers=data["region_tree"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("直梯管理-基本信息")
@allure.description("")
def test_straight_elevator_base_001(login_start):
        Authorization =login_start
        method=data["straight_elevator_base"][0]["Method"]
        apiurl=data["straight_elevator_base"][0]["ApiUrl"]
        headers=data["straight_elevator_base"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("直梯管理-设备链路")
@allure.description("")
def test_device_linking_001(login_start):
        Authorization =login_start
        method=data["device_linking"][0]["Method"]
        apiurl=data["device_linking"][0]["ApiUrl"]
        headers=data["device_linking"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("直梯管理-设备故障")
@allure.description("")
def test_device_error_call_001(login_start):
        Authorization =login_start
        method=data["device_error_call"][0]["Method"]
        apiurl=data["device_error_call"][0]["ApiUrl"]
        headers=data["device_error_call"][0]["Headers"]
        params=data["device_error_call"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("电梯实时监控-monitor")
@allure.description("")
def test_elevator_monitor_001(login_start):
        Authorization =login_start
        method=data["elevator_monitor"][0]["Method"]
        apiurl=data["elevator_monitor"][0]["ApiUrl"]
        headers=data["elevator_monitor"][0]["Headers"]
        params=data["elevator_monitor"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("设备固件-新增固件版本")
@allure.description("")
def test_device_version_add_001(login_start,device_version_add_setup):
        Authorization =login_start
        method=data["device_version_add"][0]["Method"]
        apiurl=data["device_version_add"][0]["ApiUrl"]
        headers=data["device_version_add"][0]["Headers"]
        params=data["device_version_add"][0]["Params"]
        params['productModel']=data['product_model_add'][1]['Params']['productModel']
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

        #调用自定义的清除方法，删除固件版本
        device_version_add_teardown(login_start)


@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("设备固件-固件详情列表")
@allure.description("")
def test_device_version_list_001(login_start):
        Authorization =login_start
        method=data["device_version_list"][0]["Method"]
        apiurl=data["device_version_list"][0]["ApiUrl"]
        headers=data["device_version_list"][0]["Headers"]
        params=data["device_version_list"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("设备固件-查看固件详情")
@allure.description("")
def test_device_version_detail_001(login_start,device_version_update_setup):
        Authorization =login_start
        method=data["device_version_detail"][0]["Method"]
        apiurl=data["device_version_detail"][0]["ApiUrl"]
        headers=data["device_version_detail"][0]["Headers"]
        params=data["device_version_detail"][0]["Params"]
        params['id']=device_version_update_setup['id']
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

        #执行清除操作
        device_version_add_teardown(login_start)
@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("设备固件-编辑固件详情")
@allure.description("")
def test_device_version_update_001(login_start,device_version_update_setup):
        Authorization =login_start
        method=data["device_version_update"][0]["Method"]
        apiurl=data["device_version_update"][0]["ApiUrl"]
        headers=data["device_version_update"][0]["Headers"]
        params=data["device_version_update"][0]["Params"]
        params['id']=device_version_update_setup['id']
        params['productModel'] = device_version_update_setup['productModel']

        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

        #调用自定义清除方法
        device_version_add_teardown(login_start)

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("设备固件-删除固件版本")
@allure.description("")
def test_device_version_del_001(login_start,device_version_update_setup):
        Authorization =login_start
        method=data["device_version_del"][0]["Method"]
        apiurl=data["device_version_del"][0]["ApiUrl"]
        headers=data["device_version_del"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        id=device_version_update_setup['id']
        response=send_requests(method,apiurl,headers=headers,appendurl=id)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("设备固件-新增固件产品型号")
@allure.description("")
def test_product_model_add_001(login_start,productModel_add_setup):
        Authorization =login_start
        method=data["product_model_add"][0]["Method"]
        apiurl=data["product_model_add"][0]["ApiUrl"]
        headers=data["product_model_add"][0]["Headers"]
        params=data["product_model_add"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("设备固件-编辑固件产品型号")
@allure.description("")
def test_product_model_update_001(login_start,productModel_update_setup):
        Authorization =login_start
        method=data["product_model_update"][0]["Method"]
        apiurl=data["product_model_update"][0]["ApiUrl"]
        headers=data["product_model_update"][0]["Headers"]
        params=data["product_model_update"][0]["Params"]
        params['id']=productModel_update_setup
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

        #调用自定义的方法执行清除操作
        productModel_add_teardown(login_start)

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("设备固件-删除固件产品型号")
@allure.description("")
def test_product_model_del_001(login_start,productModel_update_setup):
        Authorization =login_start
        method=data["product_model_del"][0]["Method"]
        apiurl=data["product_model_del"][0]["ApiUrl"]
        headers=data["product_model_del"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        id=productModel_update_setup #获取要删除的产品型号的id
        #发送请求
        response=send_requests(method,apiurl,headers=headers,appendurl=id)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("设备管理")
@allure.title("设备固件-固件产品型号列表")
@allure.description("")
def test_product_model_list_001(login_start):
        Authorization =login_start
        method=data["product_model_list"][0]["Method"]
        apiurl=data["product_model_list"][0]["ApiUrl"]
        headers=data["product_model_list"][0]["Headers"]
        params=data["product_model_list"][0]["Params"]

        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

if __name__=="__main__":
        pytest.main(["-s","-v","test_deviceManage.py::test_deviceIst_sleep_001"])