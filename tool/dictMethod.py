
"""
requests.structures
~~~~~~~~~~~~~~~~~~~

Data structures that power Requests.
"""

from collections import OrderedDict
from collections.abc import Mapping, MutableMapping, Iterable


class CaseInsensitiveDict(MutableMapping):
    """A case-insensitive ``dict``-like object.

    Implements all methods and operations of
    ``MutableMapping`` as well as dict's ``copy``. Also
    provides ``lower_items``.

    All keys are expected to be strings. The structure remembers the
    case of the last key to be set, and ``iter(instance)``,
    ``keys()``, ``items()``, ``iterkeys()``, and ``iteritems()``
    will contain case-sensitive keys. However, querying and contains
    testing is case insensitive::

        cid = CaseInsensitiveDict()
        cid['Accept'] = 'application/json'
        cid['aCCEPT'] == 'application/json'  # True
        list(cid) == ['Accept']  # True

    For example, ``headers['content-encoding']`` will return the
    value of a ``'Content-Encoding'`` response header, regardless
    of how the header name was originally stored.

    If the constructor, ``.update``, or equality comparison
    operations are given keys that have equal ``.lower()``s, the
    behavior is undefined.
    """

    def __init__(self, data=None, **kwargs):
        # 初始化的时候进入，初始化一个 OrderedDict()
        self._store = OrderedDict()
        if data is None:
            data = {}
        self.update(data, **kwargs)  # 把属性加入到 self 的__dict__里，也是一个字典操作。

    def __setitem__(self, key, value):
        # key.lower() 把字符串转换成小写
        # 这句话在属性赋值的时候会被调用。实现的无视字母大小写进行赋值
        self._store[key.lower()] = (key, value)
        # setattr(self,key.lower(),(key, value))

    def __getitem__(self, key):
        return self._store[key.lower()][1]

    def __delitem__(self, key):
        del self._store[key.lower()]

    def __iter__(self):
        return (casedkey for casedkey, mappedvalue in self._store.values())  # 调用父类的__iter__

    def __len__(self):
        return len(self._store)

    def lower_items(self):
        """Like iteritems(), but with all lowercase keys."""
        return (
            (lowerkey, keyval[1])
            for (lowerkey, keyval)
            in self._store.items()
        )

    def __eq__(self, other):
        if isinstance(other, Mapping):
            other = CaseInsensitiveDict(other)
        else:
            return NotImplemented
        # Compare insensitively
        return dict(self.lower_items()) == dict(other.lower_items())

    # Copy is required
    def copy(self):
        return CaseInsensitiveDict(self._store.values())

    def __repr__(self):
        # print 的时候会进入
        print(isinstance(self.items(), Iterable))  # 输入可迭代对象，此时
        ##内部实际
        # dict(iterable)
        #     d = {}
        #     for k, v in iterable: #会调用__iter__
        #         d[k] = v
        return str(dict(self.items()))


if __name__ == '__main__':
    dic= {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh-TW;q=0.6",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "user-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        }
    dic1 = CaseInsensitiveDict(dic)
    for key in dic1:
        print (key)

    print(dic1.get("UseR-agEnt"))
