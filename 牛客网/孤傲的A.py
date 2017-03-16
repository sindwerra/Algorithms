# coding=utf-8

'''
A(A也是他的编号)是一个孤傲的人，在一个n个人(其中编号依次为1到n)的队列中，
他于其中的标号为b和标号c的人都有矛盾，所以他不会和他们站在相邻的位置。
现在问你满足A的要求的对列有多少种？
给定人数n和三个人的标号A,b和c，请返回所求答案，保证人数小于等于11且大于等于3。
测试样例：
6,1,2,3
288
'''

# -*- coding:utf-8 -*-

class LonelyA:
    def getWays(self, n, A, b, c):
        # write code here
        res = 1
        cur = n
        while cur > 1:
            res *= cur
            cur -= 1
        one, two = res / n, res / (n * (n - 1))
        return res - 4 * one + 2 * two
