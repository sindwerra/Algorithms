# coding=utf-8

'''
You are given a string, s, and a list of words, words, 
that are all of the same length. Find all starting 
indices of substring(s) in s that is a concatenation of 
each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''

'''
没太多难度，逐个比对就是
'''

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or not s:
            return []

        base = len(words[0])
        length = 0
        store = {}
        for word in words:
            if word in store:
                store[word] += 1
            else:
                store[word] = 1
            length += base
        
        n = len(s)
        cur = 0
        res = []
        i = 0

        while i < n:
            while cur < n and cur - i + 1 < length:
                cur += 1
            
            if cur - i + 1 < length:
                break
            
            if self.check(s[i : cur + 1], store, base, length):
                res.append(i)
            
            i += 1
        
        return res

    def check(self, string, store, base, length):
        start = 0
        tmp = copy.copy(store)
        while start < length:
            cur_word = string[start : start + base]
            if cur_word not in tmp:
                return False
            tmp[cur_word] -= 1
            if tmp[cur_word] < 0:
                return False
            
            start += base
        
        return True