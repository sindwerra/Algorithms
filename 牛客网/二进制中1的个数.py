# coding=utf-8

'''
题目描述

输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

# Python中的取非值是取得绝对反值

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n >= 0:
            return bin(n).count('1')
        else:
            return 32 - bin(n).count('0')
