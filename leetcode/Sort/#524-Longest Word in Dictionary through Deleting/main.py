# coding=utf-8

'''
Given a string and a string dictionary, find the longest string in the dictionary 
that can be formed by deleting some characters of the given string. If there 
are more than one possible results, return the longest word with the smallest 
lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
'''

'''
还是一个掌握了比较器写法就很好做的题，这道题可以选择按照规则排序了d之后逐个比对的方法
也可以按照LCS的方法直接逐个寻找
Beat 45.38%
公司：Google
'''

class Solution(object):
    def comparator(self, A, B):
        if len(A) > len(B):
            return -1
        elif len(A) < len(B):
            return 1
        else:
            return cmp(A, B)

    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(self.comparator)
        n = len(s)

        for word in d:
            if self.compare(s, word, n):
                return word
        
        return ''

    def compare(self, string, word, limit):
        word_len = len(word)
        string_st, word_st = 0, 0

        while word_st < word_len and string_st < limit:
            if word[word_st] == string[string_st]:
                word_st += 1
            string_st += 1

        if word_st >= word_len:
            return True
        return False