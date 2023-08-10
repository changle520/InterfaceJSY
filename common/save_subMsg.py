import logging
from common.logger import Logging
import os

Logging()

#获取当前目录
current_path = os.path.dirname(os.path.abspath(__file__))
#获取上一级目录
parent_path = os.path.dirname(current_path)
filename=parent_path+'\\test_data\\submsg.txt'
def save_submsg(msg):
    '''保存订阅的消息'''
    print("保存:",msg)
    with open(filename,"w",encoding='utf-8') as f1:
        f1.write(msg)
        logging.info('保存成功')



def read_submsg():
    '''读取文件中的订阅消息、用作断言'''
    with open(filename,"r",encoding='utf-8') as f1:
       msg=f1.read()
    return msg


if __name__=="__main__":
    save_submsg("22222222222")
    print(read_submsg())
    print(filename)