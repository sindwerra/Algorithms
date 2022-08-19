# coding=utf-8

'''
Given a string, sort it in decreasing order based
on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr"
is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

'''

# 好像是谷歌和亚马逊面试题，其实就是哈希表思路，题干没有要求相对稳定性，所以dict可以解决
# 另外python的字典按值排序必须好好记下来！

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ref = {}
        for a in s:
            if ref.has_key(a):
                ref[a] += 1
            else:
                ref[a] = 1

        tmp = sorted(ref.items(), key=operator.itemgetter(1), reverse=True)
        res = ''
        for pair in tmp:
            res += (pair[1] * pair[0])
        return res
