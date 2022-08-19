# coding=utf-8

# '''
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character
# while preserving the order of characters. No two characters may map to
# the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
#
# Note:
# You may assume both s and t have the same length.
# '''

# 此题是题290的更宽泛版本，包含的情况要多于290，因为两个参数都是str变量，是以单个char
# 来产生关联的，导致pattern和value的值一样的情况有很多，此题用现有算法就已经是非常快的了
# Beat 90.17%

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        store = {}
        for a in xrange(len(s)):
            if store.has_key(s[a]):
                if store[s[a]] != t[a]: return False
            else:
                # 还是这个if语句非常耗时

                if t[a] in store.values(): return False
                else: store[s[a]] = t[a]

        return True
