# coding=utf-8

'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

click to show clarification.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or
trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
'''

'''
这题难度可能来自于in-place吧，不过python这题不可能in-place的
Beat 20.46%
公司：Microsoft, Snapchat, Apple, Bloomberg, Yelp
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = list(s.strip())
        tmp = ''
        store = []
        for ent in s:
            if ent != ' ':
                tmp += ent
            if ent == ' ' and tmp:
                store.append(tmp)
                tmp = ''
        if tmp:
            store.append(tmp)
        store.reverse()
        return ' '.join(store)
