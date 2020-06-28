# coding=utf-8

# '''
# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection
# between a letter in pattern and a non-empty word in str.
#
# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters separated by a single space.
# '''

# 此题有一个很恶心的对应关联问题，即pattern对应的词不能在后面再被其他新的pattern对应，
# 于是当有一个新的pattern出现时，检查新pattern对应的value是否在之前的对应里出现过就变得
# 很麻烦，新pattern和新value之间也不能进行双向关联（因为value有可能也会成为pattern出现
# 而作为pattern出现的value其实是一个新pattern，现在的脚本只有8.11%快，此题其实是
# 205题的一个特殊化版本，范围更狭窄了，所以当用和205一样的算法时显得没有速度优势

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        store = str.split()
        if len(pattern) != len(store): return False
        zidian = {}
        for s in xrange(len(pattern)):
            if zidian.has_key(pattern[s]):
                if zidian[pattern[s]] != store[s]: return False
            else:
                # 暂时想出来的唯一可以查找value是否重复的方法，拖慢算法的主要
                # 来源就是这里

                if store[s] not in zidian.values(): zidian[pattern[s]] = store[s]
                else: return False

        return True
