# coding=utf-8
# 其实就是简单的斐波那契数列相加就完了，比切钢条的问题还要简单

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [1, 1]
        i = 2
        while i <= n:
            result.append(result[i - 1] + result[i - 2])
            i +=1

        return result[n]
