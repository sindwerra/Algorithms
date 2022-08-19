# coding=utf-8

'''
Write a function to find the
longest common prefix string amongst an array of strings.
'''

'''
总共有五种方法做，不过前两种代价太高忽略
下面这种是纵向扫描从每一个字符串的首字符开始逐个检查
还可以通过先检查头两个字符串的公共前缀然后再沿数组逐个检查
最后Trie也可以做到
不过下面代码写的太丑了
Beat 75.11%
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        n = len(strs)
        if not n:
            return res
        st = 0
        while True:
            flag = True
            if st >= len(strs[0]):
                break
            tmp = strs[0][st]
            for s in strs:
                if st >= len(s):
                    flag = False
                    break
                if tmp != s[st]:
                    flag = False
                    break
            if flag:
                res += tmp
            else:
                break
            st += 1
        return res

'''
下面这个版本更干净一点
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        res = ''
        for i in range(len(strs[0])):
            tmp = strs[0][i]
            flag = False
            for s in strs:
                if i >= len(s) or s[i] != tmp:
                    flag = True
                    break
            if flag:
                break
            res += tmp
        return res
