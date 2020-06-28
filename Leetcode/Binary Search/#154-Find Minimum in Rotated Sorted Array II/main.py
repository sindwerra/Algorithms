# coding=utf-8

'''
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
'''

'''
由于含有重复元素，第一个while循环要在mid不满足mid大于ed和mid小于st两个条件时停止
此时再用for循环在ed到st的范围里寻找最小值或重复最小值中最早出现的点，因为ed到st
范围一般在这种情况下都很小，所以时间复杂度不会显著增加，Beat 88.02%
感觉时间复杂度还有点问题其实
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] < nums[-1]: return nums[0]   # 数组没有旋转的情况
        st, ed = 0, len(nums) - 1
        mid = (ed + 1) / 2

        while mid > st and mid < ed:
            if nums[mid] > nums[ed]:
                st = mid
                mid = (st + ed) / 2
            elif nums[mid] < nums[st]:
                ed = mid
                mid = (st + ed) / 2
            else:
                break    # 当数组前后端与中端数没有异常顺序时停止循环

        for s in xrange(ed, st - 1, -1):
            if nums[s] == nums[mid]:    # 有可能当前的mid就是最小值，只是不是第一个出现的最小值
                mid = s
            elif nums[s] < nums[mid]:   # 有可能ed到st的范围里还有更小的数[3,1,3,3]
                mid = s
            else:
                return min(nums[st], nums[ed], nums[mid])  # 当当前数大于mid值时返回最小值即可

        return nums[0]    # 数组只有一个数的情况

'''
牛客网介绍的一种通用方法，有没有重复的数的数组都可以用
中间数小于起始数时，必然最小值在左半边，且有可能就是中间值
中间数大于起始数时，最小值在右半边，中间值不是最小值可以mid + 1
中间值大于起始值小于终点值时，这时是如果是有重复值的数组是无法判断最小值在哪里的，
只能通过遍历来找最小值了
'''

class Solution(object):
    def findMin(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """

        st, ed = 0, len(arr) - 1
        while st <= ed:
            mid = st + (ed - st) / 2
            if arr[mid] < arr[st]:
                ed = mid
            elif arr[mid] > arr[ed]:
                st = mid + 1
            else:
                return min(arr[st : ed + 1])
        return None
