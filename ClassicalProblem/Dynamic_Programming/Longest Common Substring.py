# coding=utf-8

'''
给出两个字符串，找到最长公共子串，并返回其长度。
就是把LCS的思路稍微细化一下就好
'''

class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        n, m = len(A), len(B)
        res = [([0] * (m + 1)) for _ in range(n + 1)]
        lar = 0
        for i in range(n):
            for j in range(m):
                if A[i] == B[j]:
                    if i - 1 < 0 or j - 1 < 0:
                        res[i + 1][j + 1] = 1
                    elif A[i - 1] == B[j - 1]:
                        res[i + 1][j + 1] = res[i][j] + 1
                    else:
                        res[i + 1][j + 1] = 1
                if lar < res[i + 1][j + 1]:
                    lar = res[i + 1][j + 1]
        return lar
