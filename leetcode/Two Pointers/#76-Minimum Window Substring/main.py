# coding=utf-8

'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in 
complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique 
minimum window in S.
'''

'''
九章强化上面的双指针做法，用256的数组会超时，这里用的普通dict，速度非常慢，主要是判断contain的这个函数非常耗时
Beat 2.25%
公司：LinkedIn, Snapchat, Uber, Facebook
'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_check = {}
        s_check = {}
        n = len(s)

        for char in t:
            if t_check.has_key(char):
                t_check[char] += 1
            else:
                t_check[char] = 1
        
        ptr = 0
        length = sys.maxint
        count = 0
        result = ''
        for i in xrange(n):
            while ptr < n and not self.contain(s_check, t_check):
                if not s_check.has_key(s[ptr]):
                    s_check[s[ptr]] = 1
                else:
                    s_check[s[ptr]] += 1
                ptr += 1
                count += 1
            
            if self.contain(s_check, t_check) and count < length:
                length = count
                result = s[i : i + count]
            elif ptr >= n and not self.contain(s_check, t_check):
                break
            
            s_check[s[i]] -= 1
            count -= 1
            if s_check[s[i]] == 0:
                del s_check[s[i]]

        return result

    def contain(self, s_check, t_check):
        for key, value in t_check.items():
            if not s_check.has_key(key):
                return False
            if s_check[key] < value:
                return False
        
        return True