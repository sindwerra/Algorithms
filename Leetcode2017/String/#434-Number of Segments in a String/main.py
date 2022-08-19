# coding=utf-8

'''
Count the number of segments in a string, where a segment is defined to
 be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
'''

'''
这题就搞笑的，迭代的话会快点，不过有些情况要注意
Beat 44.40%
'''

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
