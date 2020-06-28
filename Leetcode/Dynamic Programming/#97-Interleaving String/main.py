# coding=utf-8

'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''

'''
一道区间类DP，跟所有DP一样，实现极其简单，就是逻辑难以想到，基本思路就是
dp[i][j]的值就相当于s3只考虑长度前i+j个长度时是否可以由s1[i]和s2[j]构成
构成这个答案的只有两种可能性，一种是dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]
为真，抑或是dp[i][j - 1] && s2[j - 1] == s3[i + j - 1]
Beat 77.04%
'''

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n = len(s1)
        if not n:
            return s2 == s3
        
        m = len(s2)
        if not m:
            return s1 == s3
        
        if n + m != len(s3):
            return False
        
        dp = [([False] * (m + 1)) for _ in xrange(n + 1)]
        dp[0][0] = True
        for i in xrange(1, m + 1):
            dp[0][i] = (dp[0][i - 1] and s2[i - 1] == s3[i - 1])
        for i in xrange(1, n + 1):
            dp[i][0] = (dp[i - 1][0] and s1[i - 1] == s3[i - 1])
        
        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        
        return dp[n][m]