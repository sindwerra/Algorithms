# coding=utf-8

# '''
# 对于两个32位整数a和b，请设计一个算法返回a和b中较大的。但是不能用任何比较判断。
# 若两数相同，返回任意一个。
# 给定两个整数a和b，请返回较大的数。
# 测试样例：
# 1,2
# 返回：2
# '''

def getMax(a, b):
        # write code here
        c = a ^ b

# 将数转换为二进制字符串

        a = bin(a)[2:]
        b = bin(b)[2:]
        c = bin(c)[2:]

# 需要将转换的二进制数长度补齐为32位

        # if len(a) < 32:
        a = '0' * (32 - len(a)) + a

        # if len(b) < 32:
        b = '0' * (32 - len(b)) + b

        # if len(c) < 32:
        c = '0' * (32 - len(c)) + c

# 二进制转十进制不需要在字符串加‘0b’

        for s in xrange(32):
            if c[s] == '1':
                if a[s] == '1': return int(a, 2)
                else: return int(b, 2)
        return int(a, 2)


one = 32424
two = 28934

if __name__ == '__main__':
    print getMax(one, two)
