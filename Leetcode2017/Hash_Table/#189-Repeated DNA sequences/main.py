# coding=utf-8

'''
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, 
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to 
identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) 
that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
'''

'''
用rabin karp居然还超时... 最后用哈希表朴素搜索还过了，速度还很快，那有什么
意义呢这道题？
Beat 86.83%
公司：LinkedIn
'''

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n < 10:
            return []

        store = {}
        res = set([])

        for i in xrange(n - 9):
            if s[i : i + 10] in store:
                res.add(s[i : i + 10])
            store[s[i : i + 10]] = 1
        
        return list(res)