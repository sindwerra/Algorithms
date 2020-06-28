# coding=utf-8

'''
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = “eceba”,

T is "ece" which its length is 3.
'''

'''
照搬的K个数的做法，速度还是太慢了
Beat 1.59%
公司：Google
'''

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        jisho = collections.Counter()
        n = len(s)

        if n <= 2:
            return n

        ptr = 0
        length = -sys.maxint
        count = 0
        for i in xrange(n):
            while ptr < n and len(jisho.keys()) <= 2:
                jisho[s[ptr]] += 1
                ptr += 1
                count += 1

            if len(jisho.keys()) <= 2:
                if count > length:
                    length = count
            if len(jisho.keys()) > 2:
                if count - 1 > length:
                    length = count - 1


            jisho[s[i]] -= 1
            count -= 1
            if jisho[s[i]] == 0:
                del jisho[s[i]]
        
        return length if length != -sys.maxint else 0

