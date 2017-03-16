# coding=utf-8

'''
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
'''

'''
可用动态规划，manacher算法解
Beat 97.94%
公司：Amazon, Microsoft, Bloomberg
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = '#' + '#'.join(s) + '#'
        n = len(string)
        p = [0] * n
        maxBorder, maxCenter = 0, 0
        res = [0, 0]
        for i in range(n):
            if maxBorder > i:
                p[i] = min(p[2 * maxCenter - i], maxBorder - i)
            else:
                p[i] = 1
            while i - p[i] >= 0 and i + p[i] < n and string[i - p[i]] == string[i + p[i]]:
                p[i] += 1
            if maxBorder < p[i] + i:
                maxBorder = p[i] + i
                maxCenter = i
                if maxBorder - maxCenter > res[1] - res[0]:
                    res = [maxCenter, maxBorder]
        return ''.join([x for x in string[2 * res[0] - res[1] + 1 : res[1]] if x != '#'])


'''
没有优化的manacher算法，将字符串预处理后每一个位直接暴力往两边扩开找
O(n^2)
Beat 50.81%
'''
