import json
from datetime import datetime

class DateEncoder(json.JSONEncoder):
    '''
    日期格式转json
    '''
    def default(self,obj):
        if isinstance(obj,datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)