'''
对于一个有序数组arr，再给定一个整数num，请在arr中找到num这个数出现的最左边的位置。
给定一个数组arr及它的大小n，同时给定num。请返回所求位置。若该元素在数组中未出现，请返回-1。
测试样例：
[1,2,3,3,4],5,3
返回：2
'''

'''
因为是找最左位置，在找到一个符合标准的位置后还需要继续往左寻找直到st和ed重合为止
'''

# -*- coding:utf-8 -*-

class LeftMostAppearance:
    def findPos(self, arr, n, num):
        # write code here
        if not n:
            return -1
        res = -1
        st, ed = 0, n - 1
        while st <= ed:
            mid = st + (ed - st) / 2
            if arr[mid] == num:
                ed = mid - 1
            elif num < arr[mid]:
                ed = mid - 1
            else:
                st = mid + 1
        return st
