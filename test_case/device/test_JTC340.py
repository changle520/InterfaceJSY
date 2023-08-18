import pytest
import allure
from common.readYaml import ReadFileData
from common.save_subMsg import read_submsg
from common.logger import Logging
from common.get_time import get_datetime
from mqtt.execute import run
from mqtt.get_msg import get_msg_sub
import logging
Logging()


#实例化读取配置文件的类,获取配置文件
readFileData=ReadFileData()
data=readFileData.get_data('test_data/ParamYaml','mqtt_config.yml')

productKey = data['JTC340']['productKey']
deviceName = data['JTC340']['deviceName']

#以下是测试用例
@allure.feature("JTC340梯联测试")
@allure.story("获取属性")
@allure.title("获取设备信息")
@allure.description("")
def test_get_property_001():
      msg = data['msg']['get_property_JTC340'][0]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("JTC340梯联测试")
@allure.story("获取属性")
@allure.title("获取服务配置")
@allure.description("")
def test_get_property_002():
      msg = data['msg']['get_property_JTC340'][1]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200
      assert msg_data['Data']['ServerConfig']['ServerAddress'] == "test.hzjishiyu.com"
      assert msg_data['Data']['ServerConfig']['ServerPort'] == 1883

@allure.feature("JTC340梯联测试")
@allure.story("获取属性")
@allure.title("获取检测参数配置")
@allure.description("")
def test_get_property_003():
      msg = data['msg']['get_property_JTC340'][2]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("JTC340梯联测试")
@allure.story("获取属性")
@allure.title("获取楼层信息")
@allure.description("")
def test_get_property_004():
      msg = data['msg']['get_property_JTC340'][3]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("JTC340梯联测试")
@allure.story("获取属性")
@allure.title("获取供电管理信息")
@allure.description("")
def test_get_property_005():
      msg = data['msg']['get_property_JTC340'][4]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("JTC340梯联测试")
@allure.story("获取属性")
@allure.title("获取自检信息")
@allure.description("")
def test_get_property_006():
      msg = data['msg']['get_property_JTC340'][5]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("JTC340梯联测试")
@allure.story("获取属性")
@allure.title("获取其他参数配置：运行累计上报时间、维保状态")
@allure.description("")
def test_get_property_007():
      msg = data['msg']['get_property_JTC340'][6]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200
      assert msg_data['Data']['OtherConfig']['RunReportTime']!=None
      assert msg_data['Data']['OtherConfig']['IsRepair']!=None

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("轿厢意外移动-上报")
@allure.description("")
def test_ErrorEvent_post_001():

    msg = data['msg']['ErrorEvent_post'][0]
    #获取当前时间的字符串格式并赋值给msg
    ErrorTime=get_datetime()
    msg['Params']['Value']['ErrorTime']=ErrorTime
    run("ErrorEvent_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("开门走梯-上报")
@allure.description("")
def test_ErrorEvent_post_002():
    msg = data['msg']['ErrorEvent_post'][1]
    #获取当前时间的字符串格式并赋值给msg
    ErrorTime=get_datetime()
    msg['Params']['Value']['ErrorTime']=ErrorTime

    run("ErrorEvent_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("区域外停梯-上报")
@allure.description("")
def test_ErrorEvent_post_003():
    msg = data['msg']['ErrorEvent_post'][2]
    #获取当前时间的字符串格式并赋值给msg
    ErrorTime=get_datetime()
    msg['Params']['Value']['ErrorTime']=ErrorTime

    run("ErrorEvent_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("冲顶-上报")
@allure.description("")
def test_ErrorEvent_post_004():
    msg = data['msg']['ErrorEvent_post'][3]
    #获取当前时间的字符串格式并赋值给msg
    ErrorTime=get_datetime()
    msg['Params']['Value']['ErrorTime']=ErrorTime

    run("ErrorEvent_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("蹲底-上报")
@allure.description("")
def test_ErrorEvent_post_005():
    msg = data['msg']['ErrorEvent_post'][4]
    #获取当前时间的字符串格式并赋值给msg
    ErrorTime=get_datetime()
    msg['Params']['Value']['ErrorTime']=ErrorTime

    run("ErrorEvent_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("开门故障-上报")
@allure.description("")
def test_ErrorEvent_post_006():
    msg = data['msg']['ErrorEvent_post'][5]
    #获取当前时间的字符串格式并赋值给msg
    ErrorTime=get_datetime()
    msg['Params']['Value']['ErrorTime']=ErrorTime

    run("ErrorEvent_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("关门故障-上报")
@allure.description("")
def test_ErrorEvent_post_007():
    msg = data['msg']['ErrorEvent_post'][6]
    #获取当前时间的字符串格式并赋值给msg
    ErrorTime=get_datetime()
    msg['Params']['Value']['ErrorTime']=ErrorTime

    run("ErrorEvent_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("反复开关门故障-上报")
@allure.description("")
def test_ErrorEvent_post_008():
    msg = data['msg']['ErrorEvent_post'][7]
    #获取当前时间的字符串格式并赋值给msg
    ErrorTime=get_datetime()
    msg['Params']['Value']['ErrorTime']=ErrorTime

    run("ErrorEvent_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("主电源断电-上报")
@allure.description("")
def test_ErrorEvent_post_009():
    msg = data['msg']['ErrorEvent_post'][8]
    #获取当前时间的字符串格式并赋值给msg
    ErrorTime=get_datetime()
    msg['Params']['Value']['ErrorTime']=ErrorTime

    run("ErrorEvent_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("轿厢意外移动-解除")
@allure.description("")
def test_ErrorClose_post_001():
    msg = data['msg']['ErrorClose_post'][0]
    #获取当前时间的字符串格式并赋值给msg
    CloseTime=get_datetime()
    msg['Params']['Value']['CloseTime']=CloseTime

    run("ErrorClose_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("开门走梯-解除")
@allure.description("")
def test_ErrorClose_post_002():
    msg = data['msg']['ErrorClose_post'][1]
    #获取当前时间的字符串格式并赋值给msg
    CloseTime=get_datetime()
    msg['Params']['Value']['CloseTime']=CloseTime

    run("ErrorClose_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("区域外停梯-解除")
@allure.description("")
def test_ErrorClose_post_003():
    msg = data['msg']['ErrorClose_post'][2]
    #获取当前时间的字符串格式并赋值给msg
    CloseTime=get_datetime()
    msg['Params']['Value']['CloseTime']=CloseTime

    run("ErrorClose_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("冲顶-解除")
@allure.description("")
def test_ErrorClose_post_004():
    msg = data['msg']['ErrorClose_post'][3]
    #获取当前时间的字符串格式并赋值给msg
    CloseTime=get_datetime()
    msg['Params']['Value']['CloseTime']=CloseTime

    run("ErrorClose_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("蹲底-解除")
@allure.description("")
def test_ErrorClose_post_005():
    msg = data['msg']['ErrorClose_post'][4]
    #获取当前时间的字符串格式并赋值给msg
    CloseTime=get_datetime()
    msg['Params']['Value']['CloseTime']=CloseTime

    run("ErrorClose_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("开门故障-解除")
@allure.description("")
def test_ErrorClose_post_006():
    msg = data['msg']['ErrorClose_post'][5]
    #获取当前时间的字符串格式并赋值给msg
    CloseTime=get_datetime()
    msg['Params']['Value']['CloseTime']=CloseTime

    run("ErrorClose_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("关门故障-解除")
@allure.description("")
def test_ErrorClose_post_007():
    msg = data['msg']['ErrorClose_post'][6]
    #获取当前时间的字符串格式并赋值给msg
    CloseTime=get_datetime()
    msg['Params']['Value']['CloseTime']=CloseTime

    run("ErrorClose_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("反复开关门故障-解除")
@allure.description("")
def test_ErrorClose_post_008():
    msg = data['msg']['ErrorClose_post'][7]
    #获取当前时间的字符串格式并赋值给msg
    CloseTime=get_datetime()
    msg['Params']['Value']['CloseTime']=CloseTime

    run("ErrorClose_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("主电源断电-解除")
@allure.description("")
def test_ErrorClose_post_009():
    msg = data['msg']['ErrorClose_post'][8]
    #获取当前时间的字符串格式并赋值给msg
    CloseTime=get_datetime()
    msg['Params']['Value']['CloseTime']=CloseTime

    run("ErrorClose_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("NTP授时请求")
@allure.title("NTP授时请求")
@allure.description("")
def test_ntp_post_001():
    msg = data['msg']['ntp_post']
    run("ntp_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("实时数据上报")
@allure.title("设备端上报实时数据")
@allure.description("")
def test_LiveData_post_001():
      msg = data['msg']['LiveData_post']
      run("LiveData_post",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("JTC340梯联测试")
@allure.story("运行累计数据上报")
@allure.title("运行累计数据上报")
@allure.description("")
def test_RunStatistics_post_001():
      msg = data['msg']['RunStatistics_post']
      run("RunStatistics_post",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象,productKey,deviceName
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("JTC340梯联测试")
@allure.story("设备升级")
@allure.title("设备升级到0616版本")
@allure.description("")
def test_service_upgrade_001():
      msg = data['msg']['service_upgrade']
      run("service_upgrade",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象,productKey,deviceName
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("JTC340梯联测试")
@allure.story("属性设置")
@allure.title("设置梯联属性")
@allure.description("")
def test_set_property_JTC340_001():
      msg = data['msg']['set_property_JTC340']
      run("set_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象,productKey,deviceName
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-困人告警")
@allure.title("困人-平层内区域困人上报")
@allure.description("")
def test_LockEvent_post_001():
    msg = data['msg']['LockEvent_post'][0]
    #获取当前时间的字符串格式并赋值给msg
    LockTime=get_datetime()
    msg['Params']['Value']['LockTime']=LockTime

    run("LockEvent_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-困人告警")
@allure.title("困人-平层内区域困人解除")
@allure.description("")
def test_LockClose_post_001():
    msg = data['msg']['LockClose_post'][0]
    #获取当前时间的字符串格式并赋值给msg
    LockTime=get_datetime()
    msg['Params']['Value']['CloseTime']=LockTime

    run("LockClose_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-困人告警")
@allure.title("困人-平层外区域困人上报")
@allure.description("")
def test_LockEvent_post_002():
    msg = data['msg']['LockEvent_post'][1]
    #获取当前时间的字符串格式并赋值给msg
    LockTime=get_datetime()
    msg['Params']['Value']['LockTime']=LockTime

    run("LockEvent_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-困人告警")
@allure.title("困人-平层外区域困人解除")
@allure.description("")
def test_LockClose_post_002():
    msg = data['msg']['LockClose_post'][1]
    #获取当前时间的字符串格式并赋值给msg
    LockTime=get_datetime()
    msg['Params']['Value']['CloseTime']=LockTime

    run("LockClose_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-困人告警")
@allure.title("困人-区域外困人上报")
@allure.description("")
def test_LockEvent_post_003():
    msg = data['msg']['LockEvent_post'][2]
    #获取当前时间的字符串格式并赋值给msg
    LockTime=get_datetime()
    msg['Params']['Value']['LockTime']=LockTime

    run("LockEvent_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-困人告警")
@allure.title("困人-区域外困人解除")
@allure.description("")
def test_LockClose_post_003():
    msg = data['msg']['LockClose_post'][2]
    #获取当前时间的字符串格式并赋值给msg
    LockTime=get_datetime()
    msg['Params']['Value']['CloseTime']=LockTime

    run("LockClose_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-设备故障")
@allure.title("门传感器异常-上报")
@allure.description("")
def test_SelfError_post_001():
    msg = data['msg']['SelfError_post'][0]
    #获取当前时间的字符串格式并赋值给msg
    OccurTime=get_datetime()
    msg['Params']['Value']['OccurTime']=OccurTime

    run("SelfError_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-设备故障")
@allure.title("人体传感器异常-上报")
@allure.description("")
def test_SelfError_post_002():
    msg = data['msg']['SelfError_post'][1]
    #获取当前时间的字符串格式并赋值给msg
    OccurTime=get_datetime()
    msg['Params']['Value']['OccurTime']=OccurTime

    run("SelfError_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-设备故障")
@allure.title("楼层传感器异常-上报")
@allure.description("")
def test_SelfError_post_003():
    msg = data['msg']['SelfError_post'][2]
    #获取当前时间的字符串格式并赋值给msg
    OccurTime=get_datetime()
    msg['Params']['Value']['OccurTime']=OccurTime

    run("SelfError_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-设备故障")
@allure.title("蓄电池电压低-上报")
@allure.description("")
def test_SelfError_post_004():
    msg = data['msg']['SelfError_post'][3]
    #获取当前时间的字符串格式并赋值给msg
    OccurTime=get_datetime()
    msg['Params']['Value']['OccurTime']=OccurTime

    run("SelfError_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-事件告警")
@allure.title("反复开关门-上报")
@allure.description("")
def test_AlarmEvent_post_001():
    msg = data['msg']['AlarmEvent_post'][0]
    #获取当前时间的字符串格式并赋值给msg
    AlarmTime=get_datetime()
    msg['Params']['Value']['AlarmTime']=AlarmTime

    run("AlarmEvent_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-事件告警")
@allure.title("长时间挡门-上报")
@allure.description("")
def test_AlarmEvent_post_002():
    msg = data['msg']['AlarmEvent_post'][1]
    #获取当前时间的字符串格式并赋值给msg
    AlarmTime=get_datetime()
    msg['Params']['Value']['AlarmTime']=AlarmTime

    run("AlarmEvent_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-事件告警")
@allure.title("反复开关门-解除")
@allure.description("")
def test_AlarmClose_post_001():
    msg = data['msg']['AlarmClose_post'][0]
    #获取当前时间的字符串格式并赋值给msg
    CloseTime=get_datetime()
    msg['Params']['Value']['CloseTime']=CloseTime

    run("AlarmClose_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-事件告警")
@allure.title("长时间挡门-解除")
@allure.description("")
def test_AlarmClose_post_002():
    msg = data['msg']['AlarmClose_post'][1]
    #获取当前时间的字符串格式并赋值给msg
    CloseTime=get_datetime()
    msg['Params']['Value']['CloseTime']=CloseTime

    run("AlarmClose_post",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("重启设备")
@allure.title("重启梯联")
@allure.description("")
def test_service_reboot_001():
    msg = data['msg']['service_reboot']
    run("service_reboot",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("属性上报")
@allure.title("上报检测参数")
@allure.description("")
def test_post_property_001():
    msg = data['msg']['post_property_JTC340'][0]
    run("post_property",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("属性上报")
@allure.title("上报楼层参数")
@allure.description("")
def test_post_property_002():
    msg = data['msg']['post_property_JTC340'][1]
    run("post_property",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("属性上报")
@allure.title("上报远程连接配置")
@allure.description("")
def test_post_property_003():
    msg = data['msg']['post_property_JTC340'][2]
    run("post_property",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("属性上报")
@allure.title("上报自检参数配置")
@allure.description("")
def test_post_property_004():
    msg = data['msg']['post_property_JTC340'][3]
    run("post_property",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("属性上报")
@allure.title("上报电源状态配置")
@allure.description("")
def test_post_property_005():
    msg = data['msg']['post_property_JTC340'][4]
    run("post_property",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("属性上报")
@allure.title("上报其他参数配置")
@allure.description("")
def test_post_property_006():
    msg = data['msg']['post_property_JTC340'][5]
    run("post_property",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("属性上报")
@allure.title("上报静态IP地址")
@allure.description("")
def test_post_property_007():
    msg = data['msg']['post_property_JTC340'][6]
    run("post_property",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("获取日志")
@allure.title("获取梯联本地日志")
@allure.description("")
def test_service_getlog_001():
    msg = data['msg']['service_getlog']
    run("service_getlog",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

if "__name__"=="__main__":
    pytest.main(['-s','-v','test_JTC340.py'])