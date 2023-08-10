import time
from paho.mqtt import client as mqtt_client
from common.readYaml import ReadFileData
import logging
from common.logger import Logging
from common.hashlibSHA1 import password_md5
from common.get_time import get_time
from mqtt.get_msg import get_msg_pub,get_msg_sub
from common.save_subMsg import save_submsg
Logging()
#实例化读取配置文件的类,获取配置文件
readFileData=ReadFileData()
data=readFileData.get_data('test_data/ParamYaml','mqtt_config.yml')

#从配置文件读取连接服务器的信息
broker=data['server']["broker"]
port=data['server']["port"]
keepalive=data['server']["keepalive"] #与代理通信之间允许的最长时间段(以S为单位)
client_id=data['DID330']["client_id"]   #客户端id
username=data['DID330']["username"]
password=data['DID330']["password"]
password_md5=password_md5(password)


def connect_mqtt():
    '''连接mqtt代理服务器'''
    def on_connect(client,userdata,flags,rc):
        '''连接回调函数'''
        #响应状态码为0表示连接成功
        if rc==0:
            logging.info("连接成功")
            print("Connected to MQTT OK!")
        else:
            logging.info(f"连接失败:{rc}")
            print(f"Failed to connect,return code %d\n",rc)

    #连接mqtt代理服务器，并获取连接引用
    client=mqtt_client.Client(client_id,clean_session=True)
    client.username_pw_set(username,password_md5)
    client.on_connect = on_connect
    client.connect(broker,port,keepalive)

    #打印日志消息
    logging.info(f"连接信息-broker:{broker}")
    logging.info(f"连接信息-port:{port}")
    logging.info(f"连接信息-keepalive:{keepalive}")
    logging.info(f"连接信息-client_id:{client_id}")

    return client

def publish(client,topic,name):
    '''发布消息'''

    for num in range(2):
        '''每隔2秒发布一次'''
        time.sleep(2)
        msg=get_msg_pub(name)
        result=client.publish(topic,msg,qos=2)
        status=result[0]
        if status==0:
            logging.info(f"发布成功，发布的主题:{topic},发布的消息:{msg}")

        else:
            logging.info(f"发布失败，发布的主题:{topic},返回的状态码:{status}")

def subscribe(client,topic):
    '''订阅主题并接收消息'''
    def on_message(client, userdata, msg):
        '''订阅消息回调函数'''
        rlt=msg.payload.decode()
        # rlt_data=get_msg_sub(rlt)
        logging.info(f"订阅的主题:{topic},订阅的消息返回:{rlt}")
        print(rlt)
        if rlt:
            save_submsg(rlt)
        # 订阅指定消息主题
    client.subscribe(topic,qos=2)
    client.on_message = on_message
# 取消订阅
def unsubscribe(topic,client):
    client.unsubscribe(topic)
    logging.info(f"取消订阅：{topic}")

# 断开连接
def disconnect(client):
    client.loop_stop()  # 停止线程
    logging.info("停止线程")
    client.disconnect()  # 断开连接
    logging.info("断开连接")

def sub_pub_byName(client,name):
    '''根据name执行订阅、发布'''
    curtime = get_time()  # 获取当前时间戳
    topic_pub = data['topic'][name]['pub'] + curtime  # 发布的消息主题
    topic_sub = data['topic'][name]['sub'] + curtime  # 订阅的消息主题
    subscribe(client,topic_sub)
    publish(client,topic_pub,name)



def run(name):
    '''执行动作：连接服务器、订阅、发布消息
        name:根据传入的name值获取对应的发布主题和订阅主题
    '''
    client=connect_mqtt()
    #运行一个线程来自动调用loop()处理网络事件，非阻塞
    client.loop_start()
    sub_pub_byName(client,name)
    disconnect(client)

if __name__=="__main__":
        run("get_property")