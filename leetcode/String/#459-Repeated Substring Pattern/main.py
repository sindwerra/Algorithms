# coding=utf-8

'''
Given a non-empty string check if it can be constructed by
taking a substring of it and appending multiple copies of
the substring together. You may assume the given string consists
of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times.
(And the substring "abcabc" twice.)
'''

'''
从一个字母的重复检查开始直到半个字符串长度的重复检查为止
另外str的长度不能被重复pattern的长度整除则可以直接跳过
Beat 45.97%
公司: Amazon, Google
'''

class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        scale, n = 1, len(str)
        while scale <= n / 2:
            if n % scale:
                scale += 1
                continue
            else:
                pat = str[:scale]
                flag = True
                tmp = scale
                while tmp < n:
                    if pat != str[tmp:tmp + scale]:
                        flag = False
                        break
                    tmp += scale
                if flag and tmp == n:
                    return True
                scale += 1

        return False
