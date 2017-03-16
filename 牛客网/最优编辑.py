# coding=utf-8

'''
对于两个字符串A和B，我们需要进行插入、删除和修改操作将A串变为B串，
定义c0，c1，c2分别为三种操作的代价，请设计一个高效算法，
求出将A串变为B串所需要的最少代价。
给定两个字符串A和B，及它们的长度和三种操作代价，请返回将A串变为B串所需要的最小代价。
保证两串长度均小于等于300，且三种代价值均小于等于100。
测试样例：
"abc",3,"adc",3,5,3,100
返回：8
'''

'''
edit distance的变体题目，三种操作的代价不是等价的，不过思路还是一样的
要搞清楚是A变B，所以插入，删除，替换都是相对A变B来说的
'''

# -*- coding:utf-8 -*-

class MinCost:
    def findMinCost(self, A, n, B, m, c0, c1, c2):
        # write code here
        res = [([0] * (n + 1)) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if not i:
                    res[i][j] = j * c1
                elif not j:
                    res[i][j] = i * c0
                elif A[j - 1] == B[i - 1]:
                    res[i][j] = res[i - 1][j - 1]
                else:
                    res[i][j] = min(res[i - 1][j - 1] + c2, res[i - 1][j] + c0, res[i][j - 1] + c1)
        return res[m][n]
