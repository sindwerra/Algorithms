# coding=utf-8

'''
编写一个类,只能用两个栈结构实现队列,支持队列的基本操作(push，pop)。
给定一个操作序列ope及它的长度n，其中元素为正数代表push操作，为0代表pop操作，
保证操作序列合法且一定含pop操作，请返回pop的结果序列。
测试样例：
[1,2,3,0,4,0],6
返回：[1,2]
'''

# -*- coding:utf-8 -*-

class TwoStack:
    def twoStack(self, ope, n):
        # write code here
        a, b = [], []
        res = []
        for s in ope:
            if s != 0:
                a.append(s)
            else:
                while a:
                    b.append(a.pop())
                res.append(b.pop())
                while b:
                    a.append(b.pop())
        return res
