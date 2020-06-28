# coding=utf-8

'''
Given a string, we can "shift" each of its letter to its successive letter,
for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets,
group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
A solution is:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
'''

'''
同一模式的字符串规律是每两个字符串之间ascII码的差是一样的（如果为负的话加26全部变为正
避免配对错误），再用tuple将这些差值存到字典里当key即可
Beat 71.23%
公司：Google，Uber
'''

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        store = {}
        std = ord('a')
        for str in strings:
            tmp = []
            if len(str) > 1:
                for s in range(1, len(str)):
                    a = (ord(str[s]) - std + 1) % 26 - (ord(str[s - 1]) - std + 1) % 26
                    if a < 0:
                        a += 26
                    tmp.append(a)
                tmp = tuple(tmp)
            else:
                tmp = tuple('1')
            if store.has_key(tmp):
                store[tmp].append(str)
            else:
                store[tmp] = [str]
        return store.values()
