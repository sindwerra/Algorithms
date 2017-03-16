# coding=utf-8

'''
DC的情况解这个题太慢，动归的解法要快，参考的maximum product subarray那个题
首先把价格数组做一个差值处理然后再找其中的最大和子数组就行，用一个cur变量就可以
Beat 84.87%
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1: return 0
        res = [0] * (n - 1)
        tmp = [(prices[x] - prices[x-1]) for x in range(1, n)]
        cur = 0
        for s in range(n - 1):
            res[s] = max(tmp[s], tmp[s] + cur)
            cur = res[s]
        a = max(res)
        return a if a > 0 else 0
