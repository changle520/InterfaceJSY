import hashlib

def password_md5(passwd):
    md5_obj = hashlib.md5()
    md5_obj.update(passwd.encode(encoding="utf-8"))
    return md5_obj.hexdigest()

password_md5("123456Bb")

