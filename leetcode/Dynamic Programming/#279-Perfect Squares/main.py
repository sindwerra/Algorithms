# coding=utf-8

'''
Given a positive integer n, find the least number of perfect square numbers 
(for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
'''

'''
就是动归做，但是要注意检查的上限是当前数的根号就行了
Beat 63.05%
公司：Google
'''

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0] * (n + 1)
        for i in xrange(1, n + 1):
            q = i
            for j in xrange(1, int(i ** 0.5) + 1):
                q = min(q, 1 + res[i - j * j])
            res[i] = q
        return res[n]
        