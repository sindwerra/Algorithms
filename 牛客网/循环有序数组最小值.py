'''
对于一个有序循环数组arr，返回arr中的最小值。
有序循环数组是指，有序数组左边任意长度的部分放到右边去，右边的部分拿到左边来。
比如数组[1,2,3,3,4]，是有序循环数组，[4,1,2,3,3]也是。
给定数组arr及它的大小n，请返回最小值。
测试样例：
[4,1,2,3,3],5
返回：1
'''

'''
LeetCode有一样的题
'''

# -*- coding:utf-8 -*-

class MinValue:
    def getMin(self, arr, n):
        # write code here
        st, ed = 0, n - 1
        while st <= ed:
            mid = st + (ed - st) / 2
            if arr[mid] < arr[st]:
                ed = mid
            elif arr[mid] > arr[ed]:
                st = mid + 1
            else:
                return min(arr[st : ed + 1])
        return None
