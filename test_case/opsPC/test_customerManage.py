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
@allure.story("客户管理")
@allure.title("物业单位账号列表")
@allure.description("")
def test_customer_wy_list_001(login_start):
        Authorization =login_start
        method=data["customer_wy_list"][0]["Method"]
        apiurl=data["customer_wy_list"][0]["ApiUrl"]
        params=data["customer_wy_list"][0]["Params"]
        headers=data["customer_wy_list"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("物业单位客户-启用")
@allure.description("")
def test_customer_wy_enable_001(login_start):
        Authorization =login_start
        method=data["customer_wy_enable"][0]["Method"]
        apiurl=data["customer_wy_enable"][0]["ApiUrl"]
        params=data["customer_wy_enable"][0]["Params"]
        headers=data["customer_wy_enable"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("物业单位客户-禁用")
@allure.description("")
def test_customer_wy_enable_002(login_start):
        Authorization =login_start
        method=data["customer_wy_enable"][1]["Method"]
        apiurl=data["customer_wy_enable"][1]["ApiUrl"]
        params=data["customer_wy_enable"][1]["Params"]
        headers=data["customer_wy_enable"][1]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("物业单位客户-新增")
@allure.description("")
def test_customer_wy_add_001(login_start):
        Authorization =login_start
        method=data["customer_wy_add"][0]["Method"]
        apiurl=data["customer_wy_add"][0]["ApiUrl"]
        params=data["customer_wy_add"][0]["Params"]
        headers=data["customer_wy_add"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==10011
        assert response['msg']=="手机号已存在"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("物业单位客户-编辑")
@allure.description("")
def test_customer_wy_update_001(login_start):
        Authorization =login_start
        method=data["customer_wy_update"][0]["Method"]
        apiurl=data["customer_wy_update"][0]["ApiUrl"]
        params=data["customer_wy_update"][0]["Params"]
        headers=data["customer_wy_update"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("物业单位客户-重置密码")
@allure.description("")
def test_customer_wy_reset_001(login_start):
        Authorization =login_start
        method=data["customer_wy_reset"][0]["Method"]
        apiurl=data["customer_wy_reset"][0]["ApiUrl"]
        params=data["customer_wy_reset"][0]["Params"]
        headers=data["customer_wy_reset"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("监管单位账号列表")
@allure.description("")
def test_customer_supervise_list_001(login_start):
        Authorization =login_start
        method=data["customer_supervise_list"][0]["Method"]
        apiurl=data["customer_supervise_list"][0]["ApiUrl"]
        params=data["customer_supervise_list"][0]["Params"]
        headers=data["customer_supervise_list"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("监管单位客户-禁用")
@allure.description("")
def test_customer_supervise_enable_001(login_start):
        Authorization =login_start
        method=data["customer_supervise_enable"][0]["Method"]
        apiurl=data["customer_supervise_enable"][0]["ApiUrl"]
        params=data["customer_supervise_enable"][0]["Params"]
        headers=data["customer_supervise_enable"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("监管单位客户-查看详情")
@allure.description("")
def test_customer_supervise_info_001(login_start):
        Authorization =login_start
        method=data["customer_supervise_info"][0]["Method"]
        apiurl=data["customer_supervise_info"][0]["ApiUrl"]
        headers=data["customer_supervise_info"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("监管单位客户-新增")
@allure.description("")
def test_customer_supervise_add_001(login_start):
        Authorization =login_start
        method=data["customer_supervise_add"][0]["Method"]
        apiurl=data["customer_supervise_add"][0]["ApiUrl"]
        headers=data["customer_supervise_add"][0]["Headers"]
        params=data["customer_supervise_add"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==10011
        assert response['msg']=="手机号已存在"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("监管单位客户-编辑")
@allure.description("")
def test_customer_supervise_update_001(login_start):
        Authorization =login_start
        method=data["customer_supervise_update"][0]["Method"]
        apiurl=data["customer_supervise_update"][0]["ApiUrl"]
        headers=data["customer_supervise_update"][0]["Headers"]
        params=data["customer_supervise_update"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("监管单位客户-重置密码")
@allure.description("")
def test_customer_supervise_reset_001(login_start):
        Authorization =login_start
        method=data["customer_supervise_reset"][0]["Method"]
        apiurl=data["customer_supervise_reset"][0]["ApiUrl"]
        headers=data["customer_supervise_reset"][0]["Headers"]
        params=data["customer_supervise_reset"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("维保单位客户-账号列表")
@allure.description("")
def test_customer_mt_list_001(login_start):
        Authorization =login_start
        method=data["customer_mt_list"][0]["Method"]
        apiurl=data["customer_mt_list"][0]["ApiUrl"]
        headers=data["customer_mt_list"][0]["Headers"]
        params=data["customer_mt_list"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("维保单位客户-启用")
@allure.description("")
def test_customer_mt_enable_001(login_start):
        Authorization =login_start
        method=data["customer_mt_enable"][0]["Method"]
        apiurl=data["customer_mt_enable"][0]["ApiUrl"]
        headers=data["customer_mt_enable"][0]["Headers"]
        params=data["customer_mt_enable"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("维保单位客户-禁用")
@allure.description("")
def test_customer_mt_enable_002(login_start):
        Authorization =login_start
        method=data["customer_mt_enable"][1]["Method"]
        apiurl=data["customer_mt_enable"][1]["ApiUrl"]
        headers=data["customer_mt_enable"][1]["Headers"]
        params=data["customer_mt_enable"][1]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("维保单位客户-查看详情")
@allure.description("")
def test_customer_mt_info_001(login_start):
        Authorization =login_start
        method=data["customer_mt_info"][0]["Method"]
        apiurl=data["customer_mt_info"][0]["ApiUrl"]
        headers=data["customer_mt_info"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("维保单位客户-新增")
@allure.description("")
def test_customer_mt_add_001(login_start):
        Authorization =login_start
        method=data["customer_mt_add"][0]["Method"]
        apiurl=data["customer_mt_add"][0]["ApiUrl"]
        headers=data["customer_mt_add"][0]["Headers"]
        params=data["customer_mt_add"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==10802
        assert response['msg']=="该小区电梯已被分配，无法选择"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("维保单位客户-编辑")
@allure.description("")
def test_customer_mt_update_001(login_start):
        Authorization =login_start
        method=data["customer_mt_update"][0]["Method"]
        apiurl=data["customer_mt_update"][0]["ApiUrl"]
        headers=data["customer_mt_update"][0]["Headers"]
        params=data["customer_mt_update"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("维保单位客户-重置密码")
@allure.description("")
def test_customer_mt_reset_001(login_start):
        Authorization =login_start
        method=data["customer_mt_reset"][0]["Method"]
        apiurl=data["customer_mt_reset"][0]["ApiUrl"]
        headers=data["customer_mt_reset"][0]["Headers"]
        params=data["customer_mt_reset"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("广告平台-账号列表")
@allure.description("")
def test_customer_ad_list_001(login_start):
        Authorization =login_start
        method=data["customer_ad_list"][0]["Method"]
        apiurl=data["customer_ad_list"][0]["ApiUrl"]
        headers=data["customer_ad_list"][0]["Headers"]
        params=data["customer_ad_list"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("广告平台-账号禁用")
@allure.description("")
def test_customer_ad_enable_001(login_start):
        Authorization =login_start
        method=data["customer_ad_enable"][0]["Method"]
        apiurl=data["customer_ad_enable"][0]["ApiUrl"]
        headers=data["customer_ad_enable"][0]["Headers"]
        params=data["customer_ad_enable"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("广告平台-账号启用")
@allure.description("")
def test_customer_ad_enable_002(login_start):
        Authorization =login_start
        method=data["customer_ad_enable"][1]["Method"]
        apiurl=data["customer_ad_enable"][1]["ApiUrl"]
        headers=data["customer_ad_enable"][1]["Headers"]
        params=data["customer_ad_enable"][1]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("广告平台-查看账号详情")
@allure.description("")
def test_customer_ad_info_001(login_start):
        Authorization =login_start
        method=data["customer_ad_info"][0]["Method"]
        apiurl=data["customer_ad_info"][0]["ApiUrl"]
        headers=data["customer_ad_info"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("广告平台-账号重置密码")
@allure.description("")
def test_customer_ad_reset_001(login_start):
        Authorization =login_start
        method=data["customer_ad_reset"][0]["Method"]
        apiurl=data["customer_ad_reset"][0]["ApiUrl"]
        headers=data["customer_ad_reset"][0]["Headers"]
        params=data["customer_ad_reset"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("客户管理")
@allure.title("广告平台-编辑账号")
@allure.description("")
def test_customer_ad_update_001(login_start):
        Authorization =login_start
        method=data["customer_ad_update"][0]["Method"]
        apiurl=data["customer_ad_update"][0]["ApiUrl"]
        headers=data["customer_ad_update"][0]["Headers"]
        params=data["customer_ad_update"][0]["Params"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

if __name__=="__main__":
        pytest.main(["-s","-v","test_alarm.py"])