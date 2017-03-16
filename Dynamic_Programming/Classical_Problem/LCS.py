# coding=utf-8

'''
给定两个字符串A和B，返回两个字符串的最长公共子序列的长度。例如，
A="1A2C3D4B56”，B="B1D23CA45B6A”，”123456"或者"12C4B6"都是最长公共子序列。
给定两个字符串A和B，同时给定两个串的长度n和m，请返回最长公共子序列的长度。
保证两串长度均小于等于300。
测试样例：
"1A2C3D4B56",10,"B1D23CA45B6A",12
返回：6
'''

# CLRS上的LCS问题

class LCS:
    def findLCS(self, A, n, B, m):
        # write code here
        res = [([0] * (m + 1)) for _ in xrange(n + 1)]
        for i in xrange(n):
            for j in xrange(m):
                if A[i] == B[j]:
                    res[i + 1][j + 1] = res[i][j] + 1
                else:
                    res[i + 1][j + 1] = max(res[i + 1][j], res[i][j + 1])
        return res[n][m]
