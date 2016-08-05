# coding=utf-8

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0: return False
        elif n == 1: return True
        elif n % 2 == 0: return self.isPowerOfTwo(n / 2)
        else: return False
