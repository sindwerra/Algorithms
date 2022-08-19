# coding=utf-8

'''
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
s = "100[Leetcode2017]", return what ?
'''

# 吞了翔一样的感觉... 其实原理很简单，就跟用栈做四则运算一样直到见到右括号然后倒出元素运算
# 不过得小心数字可以是多位数的...
# Beat 30.53%

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        store = []
        for a in s:
            if a == ']':
                tmp = ''
                while len(store) > 0 and not store[-1].isnumeric():
                    if store[-1] <> '[':
                        tmp = store.pop() + tmp
                    else:
                        store.pop()

                number = ''
                while len(store) > 0 and store[-1].isnumeric():
                    number = store.pop() + number

                tmp = int(number) * tmp
                store.append(tmp)
                continue
            store.append(a)

        res = ''
        while len(store) <> 0:
            res = store.pop() + res
        return res
