# coding=utf-8

'''
这里记录一种动态规划的解法，本题也是区间类的动态规划，但是用记忆化搜索的方式不能AC，
只能转化为矩阵递推的做法才能AC
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        res = [([False] * n) for _ in xrange(n)]
        
        dis = 1
        start, end = 0, 0
        for i in xrange(n):
            for j in xrange(i, -1, -1):
                if i == j:
                    res[j][i] = True
                elif j + 1 == i:
                    res[j][i] = (s[j] == s[i])
                elif s[j] == s[i]:
                    res[j][i] = res[j + 1][i - 1]
                else:
                    res[j][i] = False
        
        dis = 1
        start, end = 0, 0
        for i in xrange(n):
            for j in xrange(i, n):
                if res[i][j] and (j - i + 1 > dis):
                    dis = j - i + 1
                    start, end = i, j
        
        return s[start : end + 1]