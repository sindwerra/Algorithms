# coding=utf-8

'''
A message containing letters from A-Z is being encoded to numbers using 
the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number 
of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''

'''
这个题其实就是上楼梯问题的变体而已，加了两个限制条件而已，前一位和当前位的数在10-26的
区间内也可以组成一个数，其实相当于满足一定条件下f[n]=f[n - 2] + f[n - 1]
当然还要考虑'0'的情况，Beat 95.07%
公司：Microsoft, Uber, Facebook
'''

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if not n:
            return 0
        
        result = [0] * n
        result[0] = 1 if s[0] != '0' else 0

        for i in xrange(1, n):
            tmp = 0
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                tmp += result[i - 2] if i - 2 >= 0 else 1
            if s[i] != '0':
                tmp += result[i - 1]
            result[i] = tmp
        
        return result[n - 1]