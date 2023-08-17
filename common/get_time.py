import calendar
import time

def get_time():
    '''获取当前时间戳,毫秒级'''
    curt = time.time()
    t=round(curt*1000)
    return str(t)

if __name__=="__main__":
    print(get_time())