# coding=utf-8

'''
There are a row of n houses, each house can be painted with one of
the three colors: red, blue or green. The cost of painting each
house with a certain color is different.
You have to paint all the houses such that no two adjacent houses
have the same color.

The cost of painting each house with a certain color
is represented by a n x 3 cost matrix. For example,
costs[0][0] is the cost of painting house 0 with color red;
costs[1][2] is the cost of painting house 1 with color green,
and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

公司：LinkedIn
'''

'''
用一个list每次track每行各个entry的最小值，只要跟之前一行的值做运算就行
Beat 92.62%
'''

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if not n: return 0
        res = costs[0][:]
        for s in range(1, n):
            tmp = []
            tmp.append(costs[s][0] + min(res[1], res[2]))
            tmp.append(costs[s][1] + min(res[0], res[2]))
            tmp.append(costs[s][2] + min(res[0], res[1]))
            res = tmp[:]
        return min(res)
