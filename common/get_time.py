import time
from datetime import datetime

def get_time():
    '''获取当前时间戳,毫秒级'''
    curt = time.time()
    t=round(curt*1000)
    return str(t)

def get_datetime():
    '''获取当前时间并转换成字符串格式'''
    now=datetime.now()
    dtime=now.strftime('%Y-%m-%d %H:%M:%S')
    return dtime


if __name__=="__main__":
    print(get_time())
    print(get_datetime())