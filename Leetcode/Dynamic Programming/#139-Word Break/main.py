# coding=utf-8

'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more 
dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). 
Please reload the code definition to get the latest changes.
'''

'''
这特么... 从range DP，矩阵递推，BFS，DFS全试过了，结果思路其实很简单...
就是一个朴素的接龙DP，关键点在于每次拿一个区间内的s去dict里面一一比对，如果有
这个字段就去找之前去除这个字段的参考数组是不是True，如果是True就代表可以组合成
当前点的词
Beat 36.08%
公司：Google, Uber, Facebook, Amazon, Yahoo, Bloomberg, Pocket Gems
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        res = [False] * (n + 1)
        res[0] = True

        for i in xrange(1, n + 1):
            for j in xrange(1, i + 1):
                if s[j - 1 : i] in wordDict and res[j - 1]:
                    res[i] = True
                    break
        
        return res[n]