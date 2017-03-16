# coding=utf-8

'''
Given an array of integers A and let n to be its length.

Assume Bk to be an array obtained by rotating the
array A k positions clock-wise, we define a "rotation function"
F on A as follow:

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

Calculate the maximum value of F(0), F(1), ..., F(n-1).

Note:
n is guaranteed to be less than 105.
'''

# 和Rabin-Karp算法对pattern字符串预处理的思维基本一样
# 每次旋转其实只变化了一个数的值，其他值只要在之前的基础上再加上一个倍数就够了
# Beat 95.39%

class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        base = sum(A)
        res, cur = 0, 0
        for i in xrange(n):
            res += (A[i] * i)
        cur = res
        for s in xrange(1, n):
            tmp = (cur - A[n - s] * (n - 1)) + base - A[n - s]
            cur = tmp
            if tmp > res: res = tmp
        return res
