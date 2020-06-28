# coding=utf-8

'''
Given an integer, write a function to determine if it is a power of two.
'''

'''
递归检查
'''

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

'''
迭代检查每个2进制位
'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0: return False
        elif n == 1: return True
        else:
            tmp = bin(n)[3:]
            for s in tmp:
                if s == '1':
                    return False
            return True
