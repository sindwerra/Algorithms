# coding=utf-8

'''
Given a string s and a non-empty string p, find all the start indices of p's 
anagrams in s.

Strings consists of lowercase English letters only and the length of both 
strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

'''
任何字符串匹配的题rabin karp一定是解法之一
Beat 59.93%
公司：Amazon
'''

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n, m = len(s), len(p)
        
        pattern = [0] * 26
        target = [0] * 26
        result = []
        base = ord('a')
        
        if m > n or not n or not m:
            return []

        for i in xrange(m):
            pattern[ord(p[i]) - base] += 1
            target[ord(s[i]) - base] += 1
        for i in xrange(n - m + 1):
            if self.equal(pattern, target):
                result.append(i)
            if i < n - m:
                target[ord(s[i]) - base] -= 1
                target[ord(s[i + m]) - base] += 1
        
        return result

    def equal(self, pattern, target):
        for i in xrange(26):
            if pattern[i] != target[i]:
                return False
        return True