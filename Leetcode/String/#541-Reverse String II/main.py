# coding=utf-8

'''
Given a string and an integer k, you need to reverse the first k characters for every 
2k characters counting from the start of the string. If there are less than k characters left, 
reverse all of them. If there are less than 2k but greater than or equal to k characters, 
then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
'''

'''
没什么难度，主要注意k和2k的处理
公司：Google
'''

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        lst = list(s.strip())
        n = len(lst)
        
        count = 0
        for i in xrange(n):
            count += 1
            if count % k == 0 and count / k == 1:
                st, ed = i - k + 1, i
                while st < ed:
                    lst[st], lst[ed] = lst[ed], lst[st]
                    st += 1
                    ed -= 1
                continue
            if count % k == 0 and count / k == 2:
                count = 0
                continue
        
        if count < k:
            st, ed = n - count, n - 1
            while st < ed:
                lst[st], lst[ed] = lst[ed], lst[st]
                st += 1
                ed -= 1 
        
        return ''.join(lst)