# coding=utf-8

'''
Given an input string, reverse the string word by word.
A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces
and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

Related problem: Rotate Array
'''

'''
牛客网上面讲的方法，先把整个字符串反转之后
再把每个单词单个反转一下就好
Beat 80.92%
公司：Amazon, Microsoft, Uber
'''

class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        s.reverse()
        st, ed = 0, len(s) - 1
        left, right = st, ed
        while st <= ed:
            if s[st] == ' ':
                right = st
                a, b = left, right
                while a <= b - 1:
                    s[a], s[b - 1] = s[b - 1], s[a]
                    a += 1
                    b -= 1
                left = st + 1
            st += 1

        while left <= ed:
            s[left], s[ed] = s[ed], s[left]
            left += 1
            ed -= 1
