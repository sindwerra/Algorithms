# coding=utf-8

'''
给出一个数组A包含n个元素，表示n本书以及各自的页数。现在有个k个人复印书籍，
每个人只能复印连续一段编号的书，比如A[1],A[2]由第一个人复印，但是不能A[1],
A[3]由第一个人复印，求最少需要的时间复印所有书。

样例
A = [3,2,4],k = 2

返回5，第一个人复印前两本书
'''

'''
一个很经典的按值划分的题目，按照一个博客上的思路来解得，总体上说是限定一个值使得
pages里面按照一定方法划分的所有子数组的和都不大于这个数且这些子数组的数量不超过k
就是此题的意思，这里要寻找的就是这个子数组的数量是多大来推出结果，二分的上限是
整个数组的和，下限是数组的最大值
'''

class Solution:
    # @param pages: a list of integers
    # @param k: an integer
    # @return: an integer
    def copyBooks(self, pages, k):
        # write your code here
        if not pages:
            return 0
            
        st, ed = max(pages), sum(pages)

        while st + 1 < ed:
            mid = st + (ed - st) / 2
            if self.check(pages, mid) <= k:
                ed = mid
            else:
                st = mid
        
        if self.check(pages, st) <= k:
            return st
        return ed

    def check(self, pages, count):
        tmp = 0
        result = 1

        for page in pages:
            tmp += page
            if tmp > count:
                result += 1
                tmp = page
        
        return result