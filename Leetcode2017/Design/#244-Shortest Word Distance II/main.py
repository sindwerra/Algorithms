# coding=utf-8

'''
This is a follow up of Shortest Word Distance.
The only difference is now you are given the list of words
and your method will be called repeatedly many times with different parameters.
 How would you optimize it?

Design a class which receives a list of words in the constructor,
and implements a method that takes two words word1 and word2 and
return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1
and word2 are both in the list.
'''

'''
设计题，用字典先在init里面把对应下标存起来，再在调用时查找最小距离就好
Beat 51.57%
公司：LinkedIn
'''

class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.store = {}
        for s in range(len(words)):
            if self.store.has_key(words[s]):
                self.store[words[s]].append(s)
            else:
                self.store[words[s]] = [s]


    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = sys.maxint
        for a in self.store[word1]:
            for b in self.store[word2]:
                res = min(res, abs(b - a))
        return res



# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
