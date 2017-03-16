# coding=utf-8

'''
Given a list of words and two words word1 and word2,
return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2
are both in the list.
'''

'''
换下标，Beat 80.97%
公司：LinkedIn
'''

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        one, two = '', ''
        res = sys.maxint
        for s in range(len(words)):
            if words[s] == word1:
                one = s
            elif words[s] == word2:
                two = s
            if one != '' and two != '':
                res = min(res, abs(two - one))
        return res
