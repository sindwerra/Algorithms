# coding=utf-8

'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''

'''
正则表达式实现，这道题和通配符实现很类似，但是有一个更麻烦的点存在
即关于星号的匹配问题，因为这里的星号是要基于前面的字母模式来匹配而
不是一个星号就可以代表匹配模式的，所以这也就意味着星号的处理更加复杂
详情看gitbook
Beat 84.22%
公司：Google, Uber, Airbnb, Facebook, Twitter
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
            if p[i - 1] == '*':
                if p[i - 2] == '*':
                    return False
                dp[0][i] = dp[0][i - 2]
            else:
                dp[0][i] = False

        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                if s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = (dp[i][j - 2] or (dp[i][j - 1]) or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.')))
                        
        return dp[n][m]
            