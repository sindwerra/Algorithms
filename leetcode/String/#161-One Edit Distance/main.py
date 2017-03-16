# coding=utf-8

'''
Given two strings S and T, determine if they are both one edit distance apart.
'''

'''
这道题要求的是一个edit distance，没有也不行
根据CC150上的提示来做的，插入和删除其实是一样的，只是换了个视角看而已
而如果只有一个替换距离很明显两个string应该是一样长，也就是说一样长的string不一样
只有可能是因为替换操作，所以这种情况单独检查每个位是否不一样就好，超过一个就不是了
插入和删除的可能只发生在两个string长度只差一的时候，这个时候如果遍历到某点两字符不一样则屏蔽
较长string的这个字符再对比两string是否相等（我自己想的做法），如果不同可以直接返回false
CC150上对这个处理则是直接将较长string的index再额外加一，这时两个string会同时遍历到底，
再考察后续是否还有字符不同，还有不同则返回false
这道题CC150的方法判错非常快，判对就必定是O(n)
自己的想法则是判对判错是依赖于同一个条件，平均性更好，不过最坏情况可能到O(n^2)
公司：Snapchat, Uber, Facebook, Twitter
'''

'''
自己的想法，代码多但是速度快
Beat 93.63%
'''

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n, m = len(s), len(t)
        if abs(n - m) > 1:
            return False
        one, two = list(s), list(t)
        if n == m:
            if one == two:
                return False
            for index in range(n):
                if one[index] != two[index]:
                    one[index] = two[index]
                    if one == two:
                        return True
                    else:
                        return False
        elif n > m:
            for index in range(n):
                if index > m - 1:
                    return one[:index] == two
                if one[index] != two[index]:
                    if one[:index] + one[index + 1:] == two:
                        return True
                    else:
                        False
        else:
            for index in range(m):
                if index > n - 1:
                    return one == two[:index]
                if one[index] != two[index]:
                    if one == two[:index] + two[index + 1:]:
                        return True
                    else:
                        return False

'''
CC150的方法，待实现
'''
