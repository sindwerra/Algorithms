# coding=utf-8

'''
Given two non-negative integers num1 and num2 represented as string,
 return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs
to integer directly.
'''

'''
ASCII码转就行，Beat 86.55%
公司：Google, Airbnb
'''

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res, step = '', 0
        a, b = num1[::-1], num2[::-1]
        cur = 0
        base = ord('0')
        n, m = len(a), len(b)
        while cur < n or cur < m:
            if cur >= n:
                digit = ord(b[cur]) - base + step
            elif cur >= m:
                digit = ord(a[cur]) - base + step
            else:
                digit = ord(a[cur]) - base + ord(b[cur]) - base + step
            res += chr((digit) % 10 + base)
            step = digit / 10
            cur += 1
        if step:
            res += str(step)
        return res[::-1]
