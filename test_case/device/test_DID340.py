import pytest
import allure
from common.readYaml import ReadFileData
from common.save_subMsg import read_submsg
from common.logger import Logging
from mqtt.execute import run
from mqtt.get_msg import get_msg_sub
import logging
Logging()


#实例化读取配置文件的类,获取配置文件
readFileData=ReadFileData()
data=readFileData.get_data('test_data/ParamYaml','mqtt_config.yml')



#   //以下是测试用例//
@allure.feature("DID340显示屏测试")
@allure.story("获取属性")
@allure.title("获取设备端属性")
@allure.description("")
def test_get_property_001():
      run("get_property")
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==1
      assert msg_data['Data']['ServerConfig']['Secret']==data['DID340']['secret']

@allure.feature("DID340显示屏测试")
@allure.story("设置属性")
@allure.title("设置设备端属性")
@allure.description("")
def test_set_property_001():
      run("set_property")
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("DID340显示屏测试")
@allure.story("上报属性")
@allure.title("上报设备属性")
@allure.description("")
def test_post_property_001():
      run("post_property")
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("DID340显示屏测试")
@allure.story("通话申请")
@allure.title("设备申请通话")
@allure.description("")
def test_post_call_001():
      run("post_call")
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("DID340显示屏测试")
@allure.story("气象信息")
@allure.title("获取气象信息")
@allure.description("")
def test_GetWeather_post_001():
      run("GetWeather_post")
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("DID340显示屏测试")
@allure.story("实时数据上报")
@allure.title("设备端上报实时数据")
@allure.description("")
def test_LiveData_post_001():
      run("LiveData_post")
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("DID340显示屏测试")
@allure.story("运行累计数据上报")
@allure.title("运行累计数据上报")
@allure.description("")
def test_RunStatistics_post_001():
      run("RunStatistics_post")
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200




if "__name__"=="__main__":
    pytest.main(['-s','-v','test_DID340.py'])