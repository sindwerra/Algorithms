'''
有一个有序数组arr，其中不含有重复元素，请找到满足arr[i]==i条件的最左的位置。
如果所有位置上的数都不满足条件，返回-1。
给定有序数组arr及它的大小n，请返回所求值。
测试样例：
[-1,0,2,3],4
返回：2
'''

'''
普通情况是，当arr[mid]的值等于mid时，应该ed=mid，继续向左查找
当arr[mid]的值小于mid时，应该st=mid+1向右查找
当arr[mid]的值大于mid时，应该st=mid+1向左查找
另外注意单个元素的数组情况
'''

# -*- coding:utf-8 -*-

class Find:
    def findPos(self, arr, n):
        # write code here
        if not n:
            return -1
        if arr[0] > n - 1:
            return -1
        if arr[n - 1] < 0:
            return -1
        st, ed = 0, n - 1
        while st < ed:
            mid = st + (ed - st) / 2
            if arr[mid] == mid:
                ed = mid
            elif arr[mid] > mid:
                ed = mid - 1
            else:
                st = mid + 1

        if arr[st] == st:
            return st
        else:
            return -1
