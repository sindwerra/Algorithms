# coding=utf-8

# '''
# Implement strStr().
#
# Returns the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.
# '''

# 这是单指针版，速度top 30%，双指针的代码会复杂一些

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        nl = len(needle)
        if nl > len(haystack): return -1

        for s in xrange(len(haystack) - nl + 1):
            if needle == haystack[s:s + nl]: return s

        return -1
