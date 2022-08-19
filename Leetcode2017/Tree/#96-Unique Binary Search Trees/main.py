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
直接用卡特兰数做出来的，应该用动态规划
Beat 85.30%
'''

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 1
        for s in range(n + 2, 2 * n + 1):
            res *= s
        for s in range(2, n + 1):
            res /= s
        return res


'''
动态规划做法
'''

class Solution:
    # @paramn n: An integer
    # @return: An integer
    def numTrees(self, n):
        # write your code here
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
