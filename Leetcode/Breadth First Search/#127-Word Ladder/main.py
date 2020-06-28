# coding=utf-8

'''
Given two words (beginWord and endWord), and a dictionary's word list, find the 
length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of 
strings). Please reload the code definition to get the latest changes.
'''

'''
这题对时间复杂度的要求太高了，由此也可以看出是个典型的BFS题，重点在于找one edit distance的
词的时候应该用暴力检索26个字母然后替换每个index的方法来找词，可以节省时间，这种方法不是很抽象
两个for循环可以单独拿出来做一个函数这样看起来更干净
Beat 15.68%
公司：Amazon, LinkedIn, Snapchat, Facebook, Yelp
'''

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        # write your code here
        dict = set(dict)
        if not start:
            return 0
        
        if start == end:
            return 1
        
        q = collections.deque([[start, 1]])

        while q:
            base, step = q.pop()
            if base == end:
                return step

            # 找词并添加，每次发现一个词后从dict这个set中删除
                
            for i in xrange(len(base)):
                left, right = base[:i], base[i + 1:]
                for j in xrange(ord('a'), ord('{')):
                    if base[i] == chr(j):
                        continue
                    nextWord = left + chr(j) + right
                    if nextWord not in dict:
                        continue
                    q.appendleft([nextWord, step + 1])
                    dict.remove(nextWord)
                
        return 0


        

