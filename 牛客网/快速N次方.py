'''
如果更快的求一个整数k的n次方。如果两个整数相乘并得到结果的时间复杂度为O(1)，
得到整数k的N次方的过程请实现时间复杂度为O(logN)的方法。
给定k和n，请返回k的n次方，为了防止溢出，请返回结果Mod 1000000007的值。
'''

'''
N次方的幂数可以用bit位表示同时通过整除2来确定是否需要乘以当前的base
'''

# -*- coding:utf-8 -*-

class QuickPower:
    def getPower(self, k, N):
        # write code here
        res, base = 1, k
        while N:
            if N % 2:
                res = base * res % 1000000007
            base = base * base % 1000000007
            N = N >> 1
        return res % 1000000007
