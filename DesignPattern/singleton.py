# coding=utf-8


'''
单例的Python实现方式的总结，下面第一种是官方给出的单例实现方法
'''


def singleton(cls):
    instance = cls()
    instance.__call__ = lambda : instance
    return instance


@singleton
class singleNode:
    def __init__(self):
        print 'We are singleton'

'''
这是lintcode上面的实现方法，通过getInstance这个classmethod实现
'''

class anotherNode:
    instance = None

    @classmethod
    def getInstance(cls):
        if cls.instance == None:
            cls.instance = anotherNode()
        return cls.instance

    def __init__(self):
        print 'We are normal class'

# 测试

a = singleNode()
b = singleNode()
c = anotherNode.getInstance()
d = anotherNode.getInstance()


assert a == b

assert c == d
print c == d

print 'test passed'
