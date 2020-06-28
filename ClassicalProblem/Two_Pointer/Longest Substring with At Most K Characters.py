# coding=utf-8

'''
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.
'''

'''
还是九章上面的标准模板套的， 但是速度很慢
Beat 4.39%
公司：Google
'''


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        result = 0
        jisho = collections.Counter()
        n = len(s)

        if n <= k:
            return n

        ptr = 0
        length = -sys.maxint
        count = 0
        for i in xrange(n):
            while ptr < n and len(jisho.keys()) <= k:
                jisho[s[ptr]] += 1
                ptr += 1
                count += 1

            if len(jisho.keys()) <= k:
                if count > length:
                    length = count
            if len(jisho.keys()) > k:
                if count - 1 > length:
                    length = count - 1


            jisho[s[i]] -= 1
            count -= 1
            if jisho[s[i]] == 0:
                del jisho[s[i]]
        
        return length if length != -sys.maxint else 0

