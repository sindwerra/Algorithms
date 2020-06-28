# coding=utf-8

'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
'''

# 核心就是利用ord函数计算值，这样不用调用dict或是list数据结构了

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for a in s:
            result = result * 26 + ord(a) - ord('A') + 1

        return result
