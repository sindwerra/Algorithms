# coding=utf-8

'''
Say you have an array for which the ith element is the price of a given
stock on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (ie, buy one and sell one share of the stock multiple
times). However, you may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
'''

'''
这题太简单了，所有差价是正数的值全部加起来就行了
Beat 51.46%
公司：Bloomberg
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        tmp = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        res = 0
        for price in tmp:
            if price > 0:
                res += price
        return res
