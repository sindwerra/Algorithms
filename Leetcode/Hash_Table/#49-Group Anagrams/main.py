# coding=utf-8

'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
'''

'''
这题纯粹想多了，以为暴力法有问题，其实就是暴力法...
另外有python tricks这道题，还可以用defaultdict等一些其他数据结构
Beat 98.02%
公司：Amazon, Bloomberg, Uber, Facebook, Yelp
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        store = {}
        for s in strs:
            tmp = ''.join(sorted(s))
            if store.has_key(tmp):
                store[tmp].append(s)
            else:
                store[tmp] = [s]
        res = []
        for s in store:
            res.append(store[s])
        return res
