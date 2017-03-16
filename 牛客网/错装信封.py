'''
有n个信封，包含n封信，现在把信拿出来，再装回去，要求每封信不能装回它原来的信封，
问有多少种装法?
给定一个整数n，请返回装发个数，为了防止溢出，请返回结果Mod 1000000007的值。
保证n的大小小于等于300。
测试样例：
2
返回：1
'''

# -*- coding:utf-8 -*-

class CombineByMistake:
    def countWays(self, n):
        # write code here
        res = [1, 0]
        for s in range(2, n + 1):
            res.append((s - 1) * (res[-2] + res[-1]))
        return res[n] % 1000000007
