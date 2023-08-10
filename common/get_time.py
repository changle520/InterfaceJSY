import calendar
import time

def get_time():
    '''获取当前时间戳'''
    utc_time = calendar.timegm(time.gmtime())
    return str(utc_time)

