# coding=utf-8

'''
Given a string, find the length of the longest substring
without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence
and not a substring.
'''

'''
此题不但需要哈希表维护每个字母最晚出现的位置，
还需要双指针st, cur来记录当前无重复子串的信息
Beat 76.73%
公司：Amazon, Adobe, Bloomberg, Yelp
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = {}
        n = len(s)
        st, cur, res = 0, 0, 0
        while cur < n:
            if not tmp.has_key(s[cur]):        # 字典没有这个字母，录入一个带当前位置
                tmp[s[cur]] = [cur]            # cur的列表
            else:
                dis = cur - st                 # 发现了重复字母，先得到当前子串长度
                if tmp[s[cur]][-1] + 1 > st:   # 防止'abba'这种情况的发生
                    st = tmp[s[cur]][-1] + 1   # st指针只能往前跳，不能往回倒退
                tmp[s[cur]].append(cur)        # 更新当前字母最晚出现的位置
                if dis > res:                  # 比当前最长长度还长
                    res = dis
            cur += 1
        return max(res, n - st)                # 思考没有一个重复字母出现的情况
