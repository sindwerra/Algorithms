# coding=utf-8

'''
Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those
letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

'''
妈的太智障了，既然奇数只能取一个的话，肯定就是把所有奇数中的偶数部分先都拿出来啊啊啊啊啊！！！
Beat 64.44%
公司：Google，Amazon(OA九题之一)
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        jisho = {}
        for key in s:
            tmp = jisho.setdefault(key, 0)
            tmp += 1
            jisho[key] = tmp

        res, flag = 0, True
        for val in jisho.values():
            if val % 2:
                res += (val - 1)
                flag = False
            else:
                res += val
        return res if flag else res + 1
