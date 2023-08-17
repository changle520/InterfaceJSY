from common.readYaml import ReadFileData
import json

#实例化读取配置文件的类,获取配置文件
readFileData=ReadFileData()
data=readFileData.get_data('test_data/ParamYaml','mqtt_config.yml')

def get_msg_pub(message):
    '''获取发布消息的msg'''
    msg =message
    # mqtt只能传输字符串数据
    return json.dumps(msg)

def get_msg_sub(msg):
    '''获取订阅消息返回的msg，并转换成对象'''
    return json.loads(msg)