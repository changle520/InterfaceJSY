import pytest
import allure
from common.readYaml import ReadFileData
from common.save_subMsg import read_submsg
from common.logger import Logging
from mqtt.execute import run
from mqtt.get_msg import get_msg_sub
from common.get_time import get_datetime
import logging
Logging()


#实例化读取配置文件的类,获取配置文件
readFileData=ReadFileData()
data=readFileData.get_data('test_data/ParamYaml','mqtt_config.yml')

productKey = data['DID400']['productKey']
deviceName = data['DID400']['deviceName']


#   //以下是测试用例//
@allure.feature("DID400显示屏测试")
@allure.story("获取属性")
@allure.title("获取远程连接配置")
@allure.description("")
def test_get_property_001():
      msg = data['msg']['get_property'][0]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==1

@allure.feature("DID400显示屏测试")
@allure.story("获取属性")
@allure.title("获取设备信息")
@allure.description("")
def test_get_property_002():
      msg = data['msg']['get_property'][1]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==1

@allure.feature("DID400显示屏测试")
@allure.story("获取属性")
@allure.title("获取当前所有在播列表")
@allure.description("")
def test_get_property_003():
      msg = data['msg']['get_property'][2]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==1

@allure.feature("DID400显示屏测试")
@allure.story("获取属性")
@allure.title("获取息屏配置")
@allure.description("")
def test_get_property_004():
      msg = data['msg']['get_property'][3]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==1

@allure.feature("DID400显示屏测试")
@allure.story("获取属性")
@allure.title("获取电梯信息配置")
@allure.description("")
def test_get_property_005():
      msg = data['msg']['get_property'][4]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==1

@allure.feature("DID400显示屏测试")
@allure.story("获取属性")
@allure.title("获取屏幕电话配置")
@allure.description("")
def test_get_property_006():
      msg = data['msg']['get_property'][5]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==1

@allure.feature("DID400显示屏测试")
@allure.story("设置属性")
@allure.title("设置电话")
@allure.description("")
def test_set_property_001():
      msg = data['msg']['set_property_DID400'][0]
      run("set_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("DID400显示屏测试")
@allure.story("设置属性")
@allure.title("设置音量")
@allure.description("")
def test_set_property_002():
      msg = data['msg']['set_property_DID400'][1]
      run("set_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("DID400显示屏测试")
@allure.story("设置属性")
@allure.title("设置息屏时间")
@allure.description("")
def test_set_property_003():
      msg = data['msg']['set_property_DID400'][2]
      run("set_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("DID400显示屏测试")
@allure.story("公告发布")
@allure.title("发布公告到屏上")
@allure.description("")
def test_set_property_004():
      msg = data['msg']['set_property_DID400'][3]
      run("set_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("DID400显示屏测试")
@allure.story("上报属性")
@allure.title("上报设备属性")
@allure.description("")
def test_post_property_001():
      msg = data['msg']['post_property']
      run("post_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("DID400显示屏测试")
@allure.story("气象信息")
@allure.title("获取气象信息")
@allure.description("")
def test_GetWeather_post_001():
      msg = data['msg']['GetWeather_post']
      run("GetWeather_post",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("DID400显示屏测试")
@allure.story("升级测试")
@allure.title("升级到0616版本")
@allure.description("")
def test_service_upgrade_001():
      msg = data['msg']['service_upgrade_DID400']
      run("service_upgrade_DID340",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("DID400显示屏测试")
@allure.story("重启测试")
@allure.title("重启")
@allure.description("")
def test_service_reboot_001():
      msg = data['msg']['service_reboot']
      run("service_reboot_DID340",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("DID400显示屏测试")
@allure.story("新增广告")
@allure.title("屏上添加常规广告")
@allure.description("")
def test_addnormaladvertlist_001():
      msg = data['msg']['addnormaladvertlist_DID400']
      run("addnormaladvertlist",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("DID400显示屏测试")
@allure.story("上传日志")
@allure.title("本地日志上传至阿里云")
@allure.description("")
def test_log2aliyun_001():
      msg = data['msg']['log2aliyun']
      run("log2aliyun",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("DID400显示屏测试")
@allure.story("广告下刊")
@allure.title("下刊屏上的广告")
@allure.description("")
def test_deladvertlist_001():
      msg = data['msg']['deladvertlist_DID400']
      run("deladvertlist",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("DID400显示屏测试")
@allure.story("开启上报播放的广告信息")
@allure.title("开启上报当前播放的广告信息")
@allure.description("")
def test_startreportinfo_001():
      msg = data['msg']['startreportinfo']
      run("startreportinfo",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("DID400显示屏测试")
@allure.story("播放统计")
@allure.title("统计播放次数")
@allure.description("")
def test_PlayStatistics_001():
      msg = data['msg']['PlayStatistics']
      run("PlayStatistics",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

if "__name__"=="__main__":
    pytest.main(['-s','-v','test_DID400.py'])