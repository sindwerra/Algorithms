# coding=utf-8

'''
Given a positive integer num, write a function which returns True
if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
'''

'''
不要遍历到n就行，想想n的开方的范围，Beat 49.62%
'''

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: return True
        third = num / 3
        for s in xrange(third + 2):
            if s * s == num:
                return True
            elif s * s > num:
                return False
        return False
        
