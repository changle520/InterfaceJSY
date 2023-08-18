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
def elevator_add_setup(login_start):
        """
        此初始化方法用于新增一个电梯，并获取电梯ID
        """
        Authorization = login_start
        method = data["elevator_add"][0]["Method"]
        apiurl = data["elevator_add"][0]["ApiUrl"]
        params = data["elevator_add"][0]["Params"]
        headers = data["elevator_add"][0]["Headers"]
        # 往请求头里面添加Authorization
        headers.update(Authorization)
        #新增电梯
        response = send_requests(method, apiurl, headers=headers, data=params)

        #查看电梯列表，获取新增电梯的ID
        villageId=data["elevator_add"][0]["Params"]["villageId"] #获取新增电梯的项目名称
        eleLocation=data["elevator_add"][0]["Params"]["eleLocation"] #获取新增电梯的位置

        method = data["elevator_list"][0]["Method"]
        apiurl = data["elevator_list"][0]["ApiUrl"]
        params = {"villageId":villageId,"eleLocation":eleLocation}
        headers = data["elevator_list"][0]["Headers"]
        # 往请求头里面添加Authorization
        headers.update(Authorization)
        # 发送请求
        response = send_requests(method, apiurl, headers=headers, params=params)
        id=response["data"]["content"][0]["id"]
        return id   #新增电梯的ID

@pytest.fixture(scope='function',autouse=False)
def elevator_del_setup(login_start):
        """新增电梯的初始化方法"""
        print("执行初始化操作")
        yield
        print("执行清除操作")
        elevator_del_teardown(login_start)



def elevator_del_teardown(login_start):
        """
        此清除方法用于删除新增的电梯
        """
        Authorization = login_start
        #查找电梯列表，获取ID
        villageId = data["elevator_add"][0]["Params"]["villageId"]  # 获取新增电梯的项目名称
        eleLocation = data["elevator_add"][0]["Params"]["eleLocation"]  # 获取新增电梯的位置

        method = data["elevator_list"][0]["Method"]
        apiurl = data["elevator_list"][0]["ApiUrl"]
        params = {"villageId": villageId, "eleLocation": eleLocation}
        headers = data["elevator_list"][0]["Headers"]
        # 往请求头里面添加Authorization
        headers.update(Authorization)
        # 发送请求
        response = send_requests(method, apiurl, headers=headers, params=params)
        id = response["data"]["content"][0]["id"]

        #删除电梯
        method = data["elevator_del"][0]["Method"]
        apiurl = data["elevator_del"][0]["ApiUrl"]
        params = data["elevator_del"][0]["Params"]
        # 修改id为新增电梯的id
        params['ids'][0] = id
        headers = data["elevator_del"][0]["Headers"]
        # 往请求头里面添加Authorization
        headers.update(Authorization)
        # 发送请求
        response = send_requests(method, apiurl, headers=headers, data=params)

# //以下是测试用例//
@allure.feature("运维管理平台")
@allure.story("基础资料")
@allure.title("新增电梯资料-传入正确的参数值")
@allure.description("")
def test_elevator_add_001(login_start,elevator_del_setup):
        Authorization = login_start
        method = data["elevator_add"][0]["Method"]
        apiurl = data["elevator_add"][0]["ApiUrl"]
        params = data["elevator_add"][0]["Params"]
        headers = data["elevator_add"][0]["Headers"]
        # 往请求头里面添加Authorization
        headers.update(Authorization)
        # 发送请求
        response = send_requests(method, apiurl, headers=headers, data=params)
        # 断言
        assert response['code'] == 0
        assert response['msg'] == "success"

@allure.feature("运维管理平台")
@allure.story("基础资料")
@allure.title("新增电梯资料-不传入参数")
@allure.description("")
def test_elevator_add_002(login_start):
        Authorization = login_start
        method = data["elevator_add"][0]["Method"]
        apiurl = data["elevator_add"][0]["ApiUrl"]
        headers = data["elevator_add"][0]["Headers"]
        # 往请求头里面添加Authorization
        headers.update(Authorization)
        # 发送请求
        response = send_requests(method, apiurl, headers=headers)
        # 断言
        assert response['code'] == 400
        assert response['msg'] == "Bad Request!"

@allure.feature("运维管理平台")
@allure.story("基础资料")
@allure.title("电梯列表查询-参数值为空")
@allure.description("")
def test_elevator_list_001(login_start):
        Authorization =login_start
        method=data["elevator_list"][0]["Method"]
        apiurl=data["elevator_list"][0]["ApiUrl"]
        params=data["elevator_list"][0]["Params"]
        headers=data["elevator_list"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("基础资料")
@allure.title("电梯列表查询-待安装的电梯")
@allure.description("")
def test_elevator_list_002(login_start):
        Authorization =login_start
        method=data["elevator_list"][1]["Method"]
        apiurl=data["elevator_list"][1]["ApiUrl"]
        params=data["elevator_list"][1]["Params"]
        headers=data["elevator_list"][1]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("基础资料")
@allure.title("电梯列表查询-试运行的电梯")
@allure.description("")
def test_elevator_list_003(login_start):
        Authorization =login_start
        method=data["elevator_list"][2]["Method"]
        apiurl=data["elevator_list"][2]["ApiUrl"]
        params=data["elevator_list"][2]["Params"]
        headers=data["elevator_list"][2]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("基础资料")
@allure.title("电梯列表查询-正常运行的电梯")
@allure.description("")
def test_elevator_list_004(login_start):
        Authorization =login_start
        method=data["elevator_list"][3]["Method"]
        apiurl=data["elevator_list"][3]["ApiUrl"]
        params=data["elevator_list"][3]["Params"]
        headers=data["elevator_list"][3]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("基础资料")
@allure.title("电梯列表查询-异常的电梯")
@allure.description("")
def test_elevator_list_005(login_start):
        Authorization =login_start
        method=data["elevator_list"][4]["Method"]
        apiurl=data["elevator_list"][4]["ApiUrl"]
        params=data["elevator_list"][4]["Params"]
        headers=data["elevator_list"][4]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,params=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("基础资料")
@allure.title("删除电梯-电梯没有绑定设备")
@allure.description("")
def test_elevator_del_001(login_start,elevator_add_setup):
        Authorization =login_start
        id=elevator_add_setup
        method=data["elevator_del"][0]["Method"]
        apiurl=data["elevator_del"][0]["ApiUrl"]
        params=data["elevator_del"][0]["Params"]
        #修改id为新增电梯的id
        params['ids'][0]=id
        headers=data["elevator_del"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("基础资料")
@allure.title("删除电梯-电梯已经绑定设备")
@allure.description("")
def test_elevator_del_002(login_start):
        Authorization =login_start
        id=elevator_add_setup
        method=data["elevator_del"][1]["Method"]
        apiurl=data["elevator_del"][1]["ApiUrl"]
        params=data["elevator_del"][1]["Params"]
        headers=data["elevator_del"][1]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==10306
        assert response['msg']=='当前电梯已绑定设备'

@allure.feature("运维管理平台")
@allure.story("基础资料")
@allure.title("删除电梯-传入错误的参数值")
@allure.description("")
def test_elevator_del_003(login_start):
        Authorization =login_start
        id=elevator_add_setup
        method=data["elevator_del"][2]["Method"]
        apiurl=data["elevator_del"][2]["ApiUrl"]
        params=data["elevator_del"][2]["Params"]
        headers=data["elevator_del"][2]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==542
        assert response['msg']=='数据不存在'

@allure.feature("运维管理平台")
@allure.story("基础资料")
@allure.title("删除电梯-不传入参数")
@allure.description("")
def test_elevator_del_004(login_start):
        Authorization =login_start
        id=elevator_add_setup
        method=data["elevator_del"][3]["Method"]
        apiurl=data["elevator_del"][3]["ApiUrl"]
        headers=data["elevator_del"][3]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers)
        #断言
        assert response['code']!=0


@allure.feature("运维管理平台")
@allure.story("基础资料")
@allure.title("编辑电梯资料-传入正确的参数值")
@allure.description("")
def test_elevator_update_001(login_start):
        Authorization =login_start
        method=data["elevator_update"][0]["Method"]
        apiurl=data["elevator_update"][0]["ApiUrl"]
        params=data["elevator_update"][0]["Params"]
        headers=data["elevator_update"][0]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==0
        assert response['msg']=="success"

@allure.feature("运维管理平台")
@allure.story("基础资料")
@allure.title("编辑电梯资料-传入不存在的电梯ID")
@allure.description("")
def test_elevator_update_002(login_start):
        Authorization =login_start
        method=data["elevator_update"][1]["Method"]
        apiurl=data["elevator_update"][1]["ApiUrl"]
        params=data["elevator_update"][1]["Params"]
        headers=data["elevator_update"][1]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers,data=params)
        #断言
        assert response['code']==542
        assert response['msg']=="数据不存在"

@allure.feature("运维管理平台")
@allure.story("基础资料")
@allure.title("编辑电梯资料-不传入参数")
@allure.description("")
def test_elevator_update_003(login_start):
        Authorization =login_start
        method=data["elevator_update"][2]["Method"]
        apiurl=data["elevator_update"][2]["ApiUrl"]
        headers=data["elevator_update"][2]["Headers"]
        #往请求头里面添加Authorization
        headers.update(Authorization)
        #发送请求
        response=send_requests(method,apiurl,headers=headers)
        #断言
        assert response['code']!=0

if __name__=="__main__":
        pytest.main(["-s","-v","test_elevatorResource.py"])
        # pytest.main(["-s","test_elevatorResource.py::test_elevator_add_001"])