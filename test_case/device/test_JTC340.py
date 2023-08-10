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


@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-告警事件")
@allure.title("设备端上报告警事件")
@allure.description("")
def test_AlarmEvent_post_001():
    run("AlarmEvent_post")
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200


@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-告警事件解除")
@allure.title("设备端上报告警事件解除")
@allure.description("")
def test_AlarmClose_post_001():
    run("AlarmClose_post")
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-困人事件")
@allure.title("设备端上报困人事件")
@allure.description("")
def test_LockEvent_post_001():
    run("LockEvent_post")
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200


@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-困人事件解除")
@allure.title("设备端上报困人事件解除")
@allure.description("")
def test_LockClose_post_001():
    run("LockClose_post")
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-电梯故障")
@allure.title("设备端上报电梯故障")
@allure.description("")
def test_ErrorEvent_post_001():
    run("ErrorEvent_post")
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯事件上报-电梯故障解除")
@allure.title("设备端上报电梯故障解除")
@allure.description("")
def test_ErrorClose_post_001():
    run("ErrorClose_post")
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

@allure.feature("JTC340梯联测试")
@allure.story("电梯异常上报")
@allure.title("电梯异常上报")
@allure.description("")
def test_SelfError_post_001():
    run("SelfError_post")
    # 从文件中获取订阅到的消息并转换为字典对象
    msg_str = read_submsg()
    msg_data = get_msg_sub(msg_str)

    # 断言
    logging.info(f"实际订阅结果:{msg_data}")
    assert msg_data['Code'] == 200

if "__name__"=="__main__":
    pytest.main(['-s','-v','test_JTC340.py'])