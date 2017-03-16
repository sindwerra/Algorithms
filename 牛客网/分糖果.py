# coding=utf-8

'''
n颗相同的糖果，分给m个人，每人至少一颗，问有多少种分法。
给定n和m，请返回方案数，保证n小于等于12，且m小于等于n。
测试样例：
10,3
返回：36
'''

'''
以例子来说，十颗糖，九个空，三个人，两块板，所以C92
'''

# -*- coding:utf-8 -*-

class Distribution:
    def getWays(self, n, m):
        # write code here
        n -= 1
        m -= 1
        step = n - m
        res = 1
        while n > 1:
            res *= n
            n -= 1
        while m > 1:
            res /= m
            m -= 1
        while step > 1:
            res /= step
            step -= 1
        return res
