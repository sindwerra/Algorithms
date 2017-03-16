# coding=utf-8

'''
Given a positive integer, return its corresponding column
title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
'''

'''
妈个逼
Beat 59.29
公司：Microsoft, Facebook, Zenefits
'''

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n > 0:
            n -= 1
            bit = n % 26
            res = chr(ord('A') + bit) + res
            n += 1
            n -= bit
            n /= 26
        return res
