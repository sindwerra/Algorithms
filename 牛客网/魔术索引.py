# coding=utf-8

'''
在数组A[0..n-1]中，有所谓的魔术索引，满足条件A[i]=i。给定一个升序数组，元素值各不相同，
编写一个方法，判断在数组A中是否存在魔术索引。请思考一种复杂度优于o(n)的方法。
给定一个int数组A和int n代表数组大小，请返回一个bool，代表是否存在魔术索引。
测试样例：
[1,2,3,4,5]
返回：false
'''

# 说是动态规划，其实只要值比index大才往前跳，算法可以改进

# -*- coding:utf-8 -*-
class MagicIndex:
    def findMagicIndex(self, A, n):
        # write code here
        st = 0
        while st <= n - 1:
            if A[st] == st:
                return True
            elif A[st] > st:
                st += (A[st] - st + 1)
            else:
                st += 1
        return False
