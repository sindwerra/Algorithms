'''
对于一个数组，请设计一个高效算法计算需要排序的最短子数组的长度。
给定一个int数组A和数组的大小n，请返回一个二元组，代表所求序列的长度。
(原序列位置从0开始标号,若原序列有序，返回0)。保证A中元素均为正整数。
测试样例：
[1,4,6,5,9,10],6
返回：2
'''

'''
从左到右找最右边一个当前值大于之前最大值的地方
再从右到左找最左边一个当前值小于之前最小值的地方
两个值代表的区间就是需要排序的最短子数组的长度
原理实在不懂...
'''

# -*- coding:utf-8 -*-

import sys

class Subsequence:
    def shortestSubsequence(self, A, n):
        # write code here
        large, small = -sys.maxint, sys.maxint
        left, right = None, None
        for s in range(n):
            if A[s] >= large:
                large = A[s]
            else:
                right = s

        for s in range(n - 1, -1, -1):
            if A[s] <= small:
                small = A[s]
            else:
                left = s

        if not left and not right:
            return 0
        elif not left:
            return right + 1
        elif not right:
            return n - left
        else:
            return right - left + 1
