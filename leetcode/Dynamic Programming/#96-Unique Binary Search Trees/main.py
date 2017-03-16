# coding=utf-8

'''
Given n, how many structurally unique BST's (binary search trees)
that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

'''
这是动态规划的做法
Beat 48.39%
公司：Snapchat
'''

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1, 1, 2]
        for i in range(3, n + 1):
            tmp = 0
            for s in range(1, i + 1):
                if s == 1:
                    tmp += res[i - s]
                elif s == i:
                    tmp += res[s - 1]
                else:
                    tmp += (res[s - 1] * res[i - s])
            res.append(tmp)
        return res[n]
