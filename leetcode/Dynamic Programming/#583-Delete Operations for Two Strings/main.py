# coding=utf-8

'''
Given two words word1 and word2, find the minimum number of steps required 
to make word1 and word2 the same, where in each step you can delete one character 
in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make 
"eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
'''

'''
有两种动态规划的方法，一种是类似edit distance那样去动态规划找最小代价
另一种是用LCS的思维去找最长公共子序列，来反推最小代价，这里是用的edit distance
Beat 100%
公司：Google
'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)

        result = [([0] * (n + 1)) for _ in xrange(m + 1)]

        for i in xrange(m + 1):
            for j in xrange(n + 1):
                if not i:
                    result[i][j] = j
                elif not j:
                    result[i][j] = i
                elif word1[j - 1] == word2[i - 1]:
                    result[i][j] = result[i - 1][j - 1]
                else:
                    result[i][j] = min(result[i - 1][j], result[i][j - 1]) + 1
        
        return result[m][n]