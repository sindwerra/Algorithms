# coding=utf-8

'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
'''

'''
仍然是套模板，不过这里检测的是从start一直到当前index i的字符是否为对称，不对称就跳过
这里有个关于如何检查多个分段对称字符合成一个的点很难想通，但实际上解决起来很暴力
Beat 66.75%
公司：Bloomberg
'''

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res, tmp = [], []
        self.helper(0, len(s), s, tmp, res)
        return res
    
    def helper(self, start, end, s, tmp, lst):
        if start >= end:
            ref = tmp[:]
            lst.append(ref)
            return 
        
        for i in xrange(start, end):
            if not self.isPalindrome(s[start : i + 1]):
                continue
            tmp.append(s[start : i + 1])
            self.helper(i + 1, end, s, tmp, lst)
            tmp.pop()
    
    def isPalindrome(self, string):
        st, ed = 0, len(string) - 1
        while st < ed:
            if string[ed] != string[st]:
                return False
            ed -= 1
            st += 1
        return True