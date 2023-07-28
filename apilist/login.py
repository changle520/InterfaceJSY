
import logging
import json
from common.request import Request
from common.logger import Logging
from conf.jishiyu import url,username,password,headers_conf
from common.hashlibSHA1 import password_md5
Logging()

rq=Request()

def login():
    login_api="jsy-api-ops-pc/ops/pc/user/auth/login"
    login_url="{}/{}".format(url,login_api)
    headers_conf['SYSTEM_ID']="2"
    passwd=password_md5(password)
    kwargs={
    "clientId": 1001,
    "loginType": 1,
    "username": username,
    "password": passwd
}


    #发送请求
    try:
        response=rq.request('POST',login_url,headers=headers_conf,data=json.dumps(kwargs)).json()
        token=response["data"]["token"]
        Authorization="Bearer " +token
        return [{"response":response},{"Authorization":Authorization}]


    except Exception as error:
        logging.info("登录不成功:{}".format(error))



if __name__ == '__main__':

    print(login()[1])


