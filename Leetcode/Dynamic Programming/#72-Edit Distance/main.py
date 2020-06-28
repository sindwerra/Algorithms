# coding=utf-8

'''
Given two words word1 and word2, find the minimum number of steps required
to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
'''

'''
又一道经典的动态规划题，在规律上基本和LCS是一样的，不同的是多的一圈边框是有其意义的
（参考空字符串和'sunday'的编辑代价），左边框和上边框必须单独拉出来处理才行
一般情况的话，当A[i]==B[j]时，则直接参考A[i-1]==B[j-1]的情况
不相等时，则取res[i-1][j](delete),res[i][j-1](insert)或者res[i-1][j-1](replace)
三种情况里面的最小值加一
另外牛客网还有三种操作代价不同的变体，不过基本是一样的概念
Beat 83.49%

'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n, m = len(word1), len(word2)
        res = [([0] * (n + 1)) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if not i:
                    res[i][j] = j
                elif not j:
                    res[i][j] = i
                elif word1[j - 1] == word2[i - 1]:
                    res[i][j] = res[i - 1][j - 1]
                else:
                    res[i][j] = min(res[i - 1][j], res[i][j - 1], res[i - 1][j - 1])  +1
        return res[i][j]
