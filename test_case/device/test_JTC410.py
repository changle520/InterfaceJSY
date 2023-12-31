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
data=readFileData.get_data('test_data/ParamYaml','mqtt_config_410.yml')

productKey = data['JTC410']['productKey']
deviceName = data['JTC410']['deviceName']

#以下是测试用例
@allure.feature("JTC410梯联测试")
@allure.story("获取属性")
@allure.title("获取设备信息")
@allure.description("")
def test_get_property_001():
      msg = data['msg']['get_property'][0]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("JTC410梯联测试")
@allure.story("获取属性")
@allure.title("获取服务配置")
@allure.description("")
def test_get_property_002():
      msg = data['msg']['get_property'][1]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200
      assert msg_data['Data']['ServerConfig']['ServerAddress'] == "test.hzjishiyu.com"
      assert msg_data['Data']['ServerConfig']['ServerPort'] == 1883

@allure.feature("JTC410梯联测试")
@allure.story("获取属性")
@allure.title("获取故障开关配置")
@allure.description("")
def test_get_property_003():
      msg = data['msg']['get_property'][2]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200
      assert msg_data['Data']['ErrorConfig']['ClosedDoor'] in [0,1]
      assert msg_data['Data']['ErrorConfig']['OpenDoor'] in [0,1]
      assert msg_data['Data']['ErrorConfig']['ReapeatedDoor'] in [0,1]
      assert msg_data['Data']['ErrorConfig']['ElevatorBottom'] in [0,1]
      assert msg_data['Data']['ErrorConfig']['AccidentalMove'] in [0,1]
      assert msg_data['Data']['ErrorConfig']['OutsidePark'] in [0,1]
      assert msg_data['Data']['ErrorConfig']['ClosedDoor'] in [0,1]
      assert msg_data['Data']['ErrorConfig']['MainPowerOutage'] in [0,1]
      assert msg_data['Data']['ErrorConfig']['ElevatorOverspeed'] in [0,1]
      assert msg_data['Data']['ErrorConfig']['EmergencyStop'] in [0,1]
      assert msg_data['Data']['ErrorConfig']['OpenDoorWalk'] in [0,1]
      assert msg_data['Data']['ErrorConfig']['NoFault'] in [0,1]
      assert msg_data['Data']['ErrorConfig']['SafetyCircuitError'] in [0,1]
      assert msg_data['Data']['ErrorConfig']['UnknownError'] in [0,1]


@allure.feature("JTC410梯联测试")
@allure.story("获取属性")
@allure.title("获取事件开关配置")
@allure.description("")
def test_get_property_004():
      msg = data['msg']['get_property'][3]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("JTC410梯联测试")
@allure.story("获取属性")
@allure.title("获取楼层表信息")
@allure.description("")
def test_get_property_005():
      msg = data['msg']['get_property'][4]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("JTC410梯联测试")
@allure.story("获取属性")
@allure.title("获取电源配置")
@allure.description("")
def test_get_property_006():
      msg = data['msg']['get_property'][5]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("JTC410梯联测试")
@allure.story("获取属性")
@allure.title("获取自检参数配置")
@allure.description("")
def test_get_property_007():
      msg = data['msg']['get_property'][6]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200


@allure.feature("JTC410梯联测试")
@allure.story("获取属性")
@allure.title("获取其他参数配置：运行累计上报时间、维保状态")
@allure.description("")
def test_get_property_008():
      msg = data['msg']['get_property'][7]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200
      assert msg_data['Data']['OtherConfig']['RunReportTime']!=None
      assert msg_data['Data']['OtherConfig']['IsRepair']!=None

@allure.feature("JTC410梯联测试")
@allure.story("获取属性")
@allure.title("获取静态IP")
@allure.description("")
def test_get_property_009():
      msg = data['msg']['get_property'][8]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200
      assert msg_data['Data']['StaticIp']['IP']!=None
      assert msg_data['Data']['StaticIp']['DeviceIP']!=None

@allure.feature("JTC410梯联测试")
@allure.story("获取属性")
@allure.title("实时数据获取操作、用例待更新")
@allure.description("")
@pytest.mark.xfail
def test_get_property_010():
      msg = data['msg']['get_property'][9]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200
      assert msg_data['Data']['StaticIp']['IP']!=None
      assert msg_data['Data']['StaticIp']['DeviceIP']!=None

@allure.feature("JTC410梯联测试")
@allure.story("获取属性")
@allure.title("获取当前运行状态数据、用例待更新")
@allure.description("")
@pytest.mark.xfail
def test_get_property_011():
      msg = data['msg']['get_property'][10]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200
      assert msg_data['Data']['StaticIp']['IP']!=None
      assert msg_data['Data']['StaticIp']['DeviceIP']!=None

@allure.feature("JTC410梯联测试")
@allure.story("获取属性")
@allure.title("获取当前楼层气压数据、用例待更新")
@allure.description("")
@pytest.mark.xfail
def test_get_property_012():
      msg = data['msg']['get_property'][11]
      run("get_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200
      assert msg_data['Data']['StaticIp']['IP']!=None
      assert msg_data['Data']['StaticIp']['DeviceIP']!=None

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("电梯急停故障-上报")
@allure.description("")
def test_ErrorEvent_post_010():
    msg = data['msg']['ErrorEvent_post'][9]
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

@allure.feature("JTC410梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("电梯超速故障-上报")
@allure.description("")
def test_ErrorEvent_post_011():
    msg = data['msg']['ErrorEvent_post'][10]
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

@allure.feature("JTC410梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("电梯无故障-上报")
@allure.description("")
def test_ErrorEvent_post_012():
    msg = data['msg']['ErrorEvent_post'][11]
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

@allure.feature("JTC410梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("安全回路断路-上报")
@allure.description("")
def test_ErrorEvent_post_013():
    msg = data['msg']['ErrorEvent_post'][12]
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

@allure.feature("JTC410梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("未知故障-上报")
@allure.description("")
def test_ErrorEvent_post_014():
    msg = data['msg']['ErrorEvent_post'][13]
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("急停-解除")
@allure.description("")
def test_ErrorClose_post_010():
    msg = data['msg']['ErrorClose_post'][9]
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

@allure.feature("JTC410梯联测试")
@allure.story("电梯事件上报-故障告警")
@allure.title("超速-解除")
@allure.description("")
def test_ErrorClose_post_011():
    msg = data['msg']['ErrorClose_post'][10]
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
@allure.story("设备升级")
@allure.title("设备升级到()版本")
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

@allure.feature("JTC410梯联测试")
@allure.story("属性设置")
@allure.title("设置故障开关-全关")
@allure.description("")
def test_set_property_001():
      msg = data['msg']['set_property'][0]
      run("set_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象,productKey,deviceName
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("JTC410梯联测试")
@allure.story("属性设置")
@allure.title("设置故障开关-全开")
@allure.description("")
def test_set_property_002():
      msg = data['msg']['set_property'][1]
      run("set_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象,productKey,deviceName
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("JTC410梯联测试")
@allure.story("属性设置")
@allure.title("设置事件开关-全开")
@allure.description("")
def test_set_property_003():
      msg = data['msg']['set_property'][2]
      run("set_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象,productKey,deviceName
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("JTC410梯联测试")
@allure.story("属性设置")
@allure.title("设置事件开关-全关")
@allure.description("")
def test_set_property_004():
      msg = data['msg']['set_property'][3]
      run("set_property",msg,productKey,deviceName)
      #从文件中获取订阅到的消息并转换为字典对象,productKey,deviceName
      msg_str=read_submsg()
      msg_data=get_msg_sub(msg_str)

      #断言
      logging.info(f"实际订阅结果:{msg_data}")
      assert msg_data['Code']==200

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
@allure.story("电梯事件上报-事件告警")
@allure.title("一键报警事件-上报")
@allure.description("")
def test_AlarmEvent_post_003():
    msg = data['msg']['AlarmEvent_post'][2]
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

@allure.feature("JTC410梯联测试")
@allure.story("电梯事件上报-事件告警")
@allure.title("电动车检测-上报")
@allure.description("")
def test_AlarmEvent_post_004():
    msg = data['msg']['AlarmEvent_post'][3]
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

@allure.feature("JTC410梯联测试")
@allure.story("电梯事件上报-事件告警")
@allure.title("钢瓶检测-上报")
@allure.description("")
def test_AlarmEvent_post_005():
    msg = data['msg']['AlarmEvent_post'][4]
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

@allure.feature("JTC410梯联测试")
@allure.story("电梯事件上报-事件告警")
@allure.title("进入停止服务-上报")
@allure.description("")
def test_AlarmEvent_post_005():
    msg = data['msg']['AlarmEvent_post'][4]
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

@allure.feature("JTC410梯联测试")
@allure.story("电梯事件上报-事件告警")
@allure.title("进入检修运行模式-上报")
@allure.description("")
def test_AlarmEvent_post_006():
    msg = data['msg']['AlarmEvent_post'][5]
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

@allure.feature("JTC410梯联测试")
@allure.story("电梯事件上报-事件告警")
@allure.title("恢复自动运行模式-上报")
@allure.description("")
def test_AlarmEvent_post_007():
    msg = data['msg']['AlarmEvent_post'][6]
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

@allure.feature("JTC410梯联测试")
@allure.story("电梯事件上报-事件告警")
@allure.title("当前服务模式-上报")
@allure.description("")
def test_AlarmEvent_post_008():
    msg = data['msg']['AlarmEvent_post'][7]
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
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

@allure.feature("JTC410梯联测试")
@allure.story("属性上报")
@allure.title("上报故障开关参数")
@allure.description("")
def test_post_property_001():
    msg = data['msg']['post_property'][0]
    run("post_property",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC410梯联测试")
@allure.story("属性上报")
@allure.title("上报事件开关参数")
@allure.description("")
def test_post_property_002():
    msg = data['msg']['post_property'][1]
    run("post_property",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC410梯联测试")
@allure.story("属性上报")
@allure.title("上报楼层表信息")
@allure.description("")
def test_post_property_003():
    msg = data['msg']['post_property'][2]
    run("post_property",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC410梯联测试")
@allure.story("属性上报")
@allure.title("上报服务连接配置")
@allure.description("")
def test_post_property_004():
    msg = data['msg']['post_property'][3]
    run("post_property",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC410梯联测试")
@allure.story("属性上报")
@allure.title("上报自检参数配置")
@allure.description("")
def test_post_property_005():
    msg = data['msg']['post_property'][4]
    run("post_property",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC410梯联测试")
@allure.story("属性上报")
@allure.title("上报电源配置")
@allure.description("")
def test_post_property_006():
    msg = data['msg']['post_property'][5]
    run("post_property",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC410梯联测试")
@allure.story("属性上报")
@allure.title("上报其他参数配置")
@allure.description("")
def test_post_property_007():
    msg = data['msg']['post_property'][6]
    run("post_property",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC410梯联测试")
@allure.story("属性上报")
@allure.title("上报当前楼层气压信息")
@allure.description("")
def test_post_property_008():
    msg = data['msg']['post_property'][7]
    run("post_property",msg,productKey,deviceName)
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC410梯联测试")
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