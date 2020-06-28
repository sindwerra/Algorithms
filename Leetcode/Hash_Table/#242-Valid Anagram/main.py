# coding=utf-8

'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

# 速度比较慢的算法，如果用散列表会快很多

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sl = list(s)
        tl = list(t)
        sl.sort()
        tl.sort()

        if len(sl) != len(tl): return False

        a = 0
        while a < len(sl):
            if sl[a] != tl[a]: return False
            a += 1

        return True
