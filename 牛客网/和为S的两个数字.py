# coding=utf-8

'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，
使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
'''

# 双指针解决

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array) <= 1: return []
        res = [sys.maxint, sys.maxint]
        st, ed = 0, len(array) - 1
        while st < ed:
            if array[ed] + array[st] > tsum:
                ed -= 1
            elif array[ed] + array[st] < tsum:
                st += 1
            else:
                if array[ed] * array[st] < res[0] * res[1]:
                    res[0] = array[st]
                    res[1] = array[ed]
                st += 1
                ed -= 1
        return res if res[0] <> sys.maxint else []
