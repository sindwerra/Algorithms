# coding=utf-8

'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，
则最小的4个数字是1,2,3,4,。
'''

# 选择排序的思路做就行

# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        n = len(tinput)
        if k > n: return []
        for i in xrange(k):
            for j in xrange(i + 1, n):
                if tinput[j] < tinput[i]:
                    tinput[j], tinput[i] = tinput[i], tinput[j]
        return tinput[:k]
