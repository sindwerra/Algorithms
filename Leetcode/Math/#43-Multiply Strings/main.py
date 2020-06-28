# coding=utf-8

'''
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert
the inputs to integer directly.
'''

'''
还是用ASCII码做，Beat 92.97%
公司:Facebook, Twitter
'''

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res, mtcd, mlpl = 0, num1[::-1], num2[::-1]
        base, count = 0, 1
        for s in mtcd:
            base += ((ord(s) - ord('0')) * count)
            count *= 10
        count = 1
        for k in mlpl:
            res += ((ord(k) - ord('0')) * base * count)
            count *= 10
        return str(res)
