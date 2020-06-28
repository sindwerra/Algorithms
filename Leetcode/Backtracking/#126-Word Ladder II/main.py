# coding=utf-8

'''
Given two words (beginWord and endWord), and a dictionary's word list, find all 
shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). 
Please reload the code definition to get the latest changes.
'''

'''
应该是迄今为止做的最难的几道题之一了，按照九章的思路，首先需要一个从终点开始遍历整个字典的BFS
在遍历过程中如果终点本身不在字典里面则返回空列表，BFS之后返回一个哈希表记录了从终点开始遍历到
这些字符串的距离是多少，此时又有beginWord如果在原字典里而又不在返回的哈希表里说明终点到不了
起点，一样返回空列表，最后进行DFS，如果beginWord在原字典里则直接用返回哈希表里面的对应距离
作为起始距离，如果不在则用maxint代替,DFS时找到的新词如果在哈希表中的距离小于当前基准词的距离
才继续DFS下去（这代表离endWord变近了）
Beat 12.85%
公司：Amazon， Yelp
'''

import copy

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        
        if endWord not in wordList:
            return []
        
        tmp_list = copy.copy(wordList)

        jisho = self.BFS(endWord, beginWord, tmp_list)
        if beginWord in wordList and beginWord not in jisho:
            return []

        tmp, result = [beginWord], []

        if beginWord in wordList:
            self.helper(beginWord, jisho[beginWord], jisho, wordList, tmp, result, endWord)
        else:
            self.helper(beginWord, sys.maxint, jisho, wordList, tmp, result, endWord)

        return result
    
    def helper(self, string, distance, jisho, wordList, tmp, result, endWord):
        if string == endWord:
            ref = tmp[:]
            result.append(ref)
            return 
        
        for i in xrange(len(string)):
            left, right = string[ : i], string[i + 1 : ]
            for j in xrange(ord('a'), ord('{')):
                if chr(j) == string[i]:
                    continue
                nextWord = left + chr(j) + right
                if nextWord in wordList and jisho[nextWord] < distance:
                    tmp.append(nextWord)
                    self.helper(nextWord, jisho[nextWord], jisho, wordList, tmp, result, endWord)
                    tmp.pop()


    def BFS(self, A, B, wordList):
        q = collections.deque([[A, 1]])
        wordList.remove(A)
        result = {}
        while q:
            base, step = q.pop()
            result[base] = step
            for i in xrange(len(base)):
                left, right = base[ : i], base[i + 1 : ]
                for j in xrange(ord('a'), ord('{')):
                    if chr(j) == base[i]:
                        continue
                    nextWord = left + chr(j) + right
                    if nextWord in wordList:
                        q.appendleft([nextWord, step + 1])
                        wordList.remove(nextWord)
        return result

