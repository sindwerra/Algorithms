# coding=utf-8

'''
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
'''

'''
通配符问题，其实大多数情况都能想到是匹配，就是有一个状态即星号的匹配比较难想，
但实际上也就是三个状态或以下就行了
Beat 40.08%
公司：Google, Snapchat, Two Sigma, Facebook, Twitter
'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)
        
        dp = [([False] * (m + 1)) for _ in xrange(n + 1)]
        dp[0][0] = True
        for i in xrange(1, m + 1):
            dp[0][i] = (dp[0][i - 1] and p[i - 1] == '*')
        
        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                if s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = (dp[i - 1][j] or dp[i][j - 1] or dp[i - 1][j - 1])
        
        return dp[n][m]