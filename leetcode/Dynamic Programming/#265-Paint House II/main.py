# coding=utf-8

'''
There are a row of n houses, each house can be painted with one of the k colors.
The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented
by a n x k cost matrix. For example, costs[0][0] is the cost of painting
house 0 with color 0; costs[1][2] is the cost of painting house 1
with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Follow up:
Could you solve it in O(nk) runtime?
'''

'''
跟Paint House基本一样，只是用循环来append每个最小值就行
Beat 49.38%，还可以改进
公司：Facebook
'''

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs: return 0
        res = costs[0][:]
        n, m = len(costs), len(costs[0])
        for s in range(1, n):
            tmp = []
            for k in range(m):
                tmp.append(costs[s][k] + min(res[:k] + res[k + 1:]))
            res = tmp[:]
        return min(res)
