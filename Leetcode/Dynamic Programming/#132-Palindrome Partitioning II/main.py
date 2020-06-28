# coding=utf-8

'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''

'''
难啊，这题实质上是两个DP结合在一起，首先用longest palindromic substring的做法得到一个ref的区间
矩阵，接着利用这个区间矩阵在string从头到尾验证一每一个区间是不是对称，利用类似LIS的方法求得最小值
Beat 47.80%
'''

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ref = [([False] * n) for _ in xrange(n)]

        for i in xrange(n):
            for j in xrange(i, -1, -1):
                if i == j:
                    ref[j][i] = True
                elif j + 1 == i:
                    ref[j][i] = (s[j] == s[i])
                elif s[j] == s[i]:
                    ref[j][i] = ref[j + 1][i - 1]
                else:
                    ref[j][i] = False
        
        res = [0] * n
        
        for i in xrange(n):
            q = i + 1
            for j in xrange(i):
                if ref[j][i]:
                    q = min(q, res[j - 1] + 1)
            res[i] = min(q, res[i - 1] + 1)
        
        return res[n - 1] - 1
            