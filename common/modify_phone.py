def modify_phone(params):
    '''

    :param str: 要脱敏处理的电话号码
    :return:
    '''
    str_params=str(params)
    rlt=list(str_params)
    for i in range(len(str_params)):
        if i in (3,4,5,6):
            rlt[i]='*'
    return ''.join(rlt)

if __name__ == '__main__':
    print(modify_phone(12345678912))
