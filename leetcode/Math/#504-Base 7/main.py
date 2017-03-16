# coding=utf-8

'''
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
'''

'''
跟excel column sheet那道题类似
Beat 58.02%
'''

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return '0'
        res = ''
        sign = -1 if num < 0 else 1
        num = abs(num)
        while num > 0:
            bit = num % 7
            res = str(bit) + res
            num -= bit
            num /= 7
        return res if sign == 1 else '-' + res
