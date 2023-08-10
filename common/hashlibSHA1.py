import hashlib

def password_md5(passwd):
    md5_obj = hashlib.md5()
    md5_obj.update(passwd.encode(encoding="utf-8"))
    return md5_obj.hexdigest()

rlt=password_md5("DID330&300133121210002&3c9951a811d745fbbda6f2a0843ccf19")
print(rlt)

