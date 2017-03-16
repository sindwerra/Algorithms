# coding=utf-8

'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''

'''
强行背的答案，如果前一个字母比后一个字母小则减去这个字母的值
大则加上，且最后一个字母永远是加的
公司：Microsoft, Bloomberg, Uber, Facebook, Yahoo
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        chart = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        res = 0
        for i in range(len(s) - 1):
            if chart[s[i]] < chart[s[i + 1]]:
                res -= chart[s[i]]
            else:
                res += chart[s[i]]
        return res + chart[s[-1]]
