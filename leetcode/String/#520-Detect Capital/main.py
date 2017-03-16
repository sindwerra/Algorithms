# coding=utf-8

'''
Given a word, you need to judge whether the usage of capitals
in it is right or not.

We define the usage of capitals in a word to be right
when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more
than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a
right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
Note: The input will be a non-empty word consisting of
uppercase and lowercase latin letters.
'''

'''
要不全部没有出现，要不出现一次且在第一个位置，要不全部都是大写
不是这三种情况就是False
Beat 82.32%
公司：Google
'''

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        store = []
        for s in range(len(word)):
            if ord('A') <= ord(word[s]) <= ord('Z'):
                store.append(s)
        return len(store) == 0 or (len(store) == 1 and not store[0]) or len(store) == len(word)
