# coding=utf-8

'''
题目描述

给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
'''

# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        n = len(A)
        B = []
        for i in xrange(n):
            B.append(1)
            for j in xrange(n):
                if j <> i:
                    B[i] *= A[j]
        return B
